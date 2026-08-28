from pathlib import Path
import base64,gzip,math,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')

# 1) Shared CTRL state: work, salary updates, meeting tasks, directives metadata survive refresh/version updates and are shared across devices.
old="""function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }"""
new="""function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      try{syncSharedCTRL()}catch(e){console.warn('Không đồng bộ được dữ liệu dùng chung',e)}
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }"""
if old in s:s=s.replace(old,new,1)

shared_js=r'''
let CTRL_SYNC_BUSY=false, CTRL_SYNC_READY=false, CTRL_REMOTE_UPDATED='';
function ctrlMergeArray(remote,local,key='id'){
 const m=new Map(); (remote||[]).forEach(x=>m.set(String(x?.[key]??x?.name??JSON.stringify(x)),x));
 (local||[]).forEach(x=>m.set(String(x?.[key]??x?.name??JSON.stringify(x)),x)); return [...m.values()]
}
function mergeCTRL(remote,local){
 const r=(remote&&typeof remote==='object')?remote:{},l=(local&&typeof local==='object')?local:{};
 const o={...r,...l};
 ['work','reports','meetingTasks','directives'].forEach(k=>o[k]=ctrlMergeArray(r[k],l[k],'id'));
 o.salary=ctrlMergeArray(r.salary,l.salary,'name');
 if(!o.salary||o.salary.length<30)o.salary=SALARY_SOURCE;
 return o
}
async function syncSharedCTRL(){
 if(CTRL_SYNC_BUSY||typeof sb==='undefined')return; CTRL_SYNC_BUSY=true;
 try{
  const sess=(await sb.auth.getSession()).data?.session;if(!sess)return;
  const {data}=await sb.from('app_shared_state').select('state,updated_at').eq('state_key','control').maybeSingle();
  const merged=mergeCTRL(data?.state||{},CTRL);
  const payload={state_key:'control',state:merged,updated_at:new Date().toISOString(),updated_by:sess.user.id};
  const {error}=await sb.from('app_shared_state').upsert(payload,{onConflict:'state_key'});if(error)throw error;
  CTRL=merged;localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));CTRL_REMOTE_UPDATED=payload.updated_at;CTRL_SYNC_READY=true;
 }catch(e){console.warn('Shared CTRL save failed:',e)}finally{CTRL_SYNC_BUSY=false}
}
async function loadSharedCTRL(){
 if(typeof sb==='undefined')return;
 try{
  const sess=(await sb.auth.getSession()).data?.session;if(!sess)return;
  const {data,error}=await sb.from('app_shared_state').select('state,updated_at').eq('state_key','control').maybeSingle();if(error)throw error;
  if(data?.state&&Object.keys(data.state).length){CTRL=mergeCTRL(data.state,CTRL);localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));CTRL_REMOTE_UPDATED=data.updated_at||'';CTRL_SYNC_READY=true;renderCtrlAll();if(typeof renderTTOverview==='function')renderTTOverview();if(typeof renderTTStaff==='function')renderTTStaff();if(typeof renderStaffWorkCards==='function')renderStaffWorkCards()}
  else if(isThuLamAdmin?.()) await syncSharedCTRL();
 }catch(e){console.warn('Shared CTRL load failed:',e)}
}
window.addEventListener('load',()=>setTimeout(loadSharedCTRL,1200));
window.addEventListener('focus',()=>{if(CTRL_SYNC_READY)setTimeout(loadSharedCTRL,200)});
'''
needle="function openCtrl(p){ctrlModal.style.display='block';switchCtrl(p)}"
if 'function mergeCTRL(' not in s and needle in s:s=s.replace(needle,shared_js+'\n'+needle,1)

# Direct saves outside csave also sync remotely.
s=s.replace("localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));\n vdPeriod", "localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));try{syncSharedCTRL()}catch(e){}\n vdPeriod")
s=s.replace("localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));\n try{await deleteDirectiveFileBlob", "localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));try{syncSharedCTRL()}catch(e){}\n try{await deleteDirectiveFileBlob")

# 2) Shared file storage. Keep IndexedDB as offline fallback, but use Supabase Storage + app_files registry as primary.
for fn in ['saveDirectiveFileBlob','getDirectiveFileBlob','deleteDirectiveFileBlob']:
 s=re.sub(r'(?<!Local)\b(async\s+function\s+)'+fn+r'\s*\(',r'\1'+fn+'Local(',s,count=1)
file_js=r'''
function cloudFileSafeName(n){return String(n||'file').normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-zA-Z0-9._-]+/g,'_').slice(-120)}
async function saveDirectiveFileBlob(id,file){
 try{await saveDirectiveFileBlobLocal(id,file)}catch(e){}
 try{
  const sess=(await sb.auth.getSession()).data?.session;if(!sess)return true;
  const key=String(id),path=`trung-tam-ai/${encodeURIComponent(key)}/${Date.now()}_${cloudFileSafeName(file.name)}`;
  const old=(await sb.from('app_files').select('storage_path').eq('object_key',key).maybeSingle()).data;
  const up=await sb.storage.from('kho-nghiep-vu-so').upload(path,file,{upsert:true,contentType:file.type||undefined});if(up.error)throw up.error;
  const meta=await sb.from('app_files').upsert({object_key:key,storage_path:path,file_name:file.name,mime_type:file.type||'',updated_at:new Date().toISOString(),uploaded_by:sess.user.id},{onConflict:'object_key'});if(meta.error)throw meta.error;
  if(old?.storage_path&&old.storage_path!==path)try{await sb.storage.from('kho-nghiep-vu-so').remove([old.storage_path])}catch(e){}
  return true
 }catch(e){console.warn('Cloud file save failed; kept local fallback',e);return true}
}
async function getDirectiveFileBlob(id){
 try{
  const key=String(id),{data}=await sb.from('app_files').select('*').eq('object_key',key).maybeSingle();
  if(data?.storage_path){const r=await sb.storage.from('kho-nghiep-vu-so').download(data.storage_path);if(!r.error&&r.data)return {blob:r.data,name:data.file_name,type:data.mime_type}}
 }catch(e){console.warn('Cloud file read failed',e)}
 return getDirectiveFileBlobLocal(id)
}
async function deleteDirectiveFileBlob(id){
 try{
  const key=String(id),{data}=await sb.from('app_files').select('storage_path').eq('object_key',key).maybeSingle();
  if(data?.storage_path)await sb.storage.from('kho-nghiep-vu-so').remove([data.storage_path]);await sb.from('app_files').delete().eq('object_key',key)
 }catch(e){console.warn('Cloud file delete failed',e)}
 try{return await deleteDirectiveFileBlobLocal(id)}catch(e){return true}
}
async function migrateLocalFilesToCloud(){
 try{
  if(!isThuLamAdmin?.())return;const db=await vdOpenDB();const tx=db.transaction(VD_STORE,'readonly'),st=tx.objectStore(VD_STORE);const req=st.getAll();
  req.onsuccess=async()=>{for(const rec of req.result||[]){if(!rec?.blob)continue;try{const exists=(await sb.from('app_files').select('object_key').eq('object_key',String(rec.id)).maybeSingle()).data;if(!exists){const f=new File([rec.blob],rec.name||'file',{type:rec.type||rec.blob.type});await saveDirectiveFileBlob(rec.id,f)}}catch(e){}}}
 }catch(e){console.warn('Local file migration skipped',e)}
}
window.addEventListener('load',()=>setTimeout(migrateLocalFilesToCloud,2500));
'''
needle='const VD_DB_NAME='
if 'function cloudFileSafeName(' not in s:
 pos=s.find(needle)
 if pos>=0:s=s[:pos]+file_js+'\n'+s[pos:]

# 3) Fix broken monthly report buttons found by static audit.
monthly_js=r'''
function getMonthlySheetFrame(){return document.querySelector('#monthReportPage iframe,#monthlyReportPage iframe,#monthreport iframe')||[...document.querySelectorAll('iframe')].find(f=>String(f.src||'').includes('1o7qxYI_F0N4B7X1o2uKvNUxcPwLlBwGr'))}
function reloadMonthlySheet(){const f=getMonthlySheetFrame();if(!f)return alert('Không tìm thấy biểu Báo cáo tháng.');const u=f.src;f.src='about:blank';setTimeout(()=>f.src=u,60)}
function openMonthlySheet(){const f=getMonthlySheetFrame();const u=f?.src||'https://docs.google.com/spreadsheets/d/1o7qxYI_F0N4B7X1o2uKvNUxcPwLlBwGr/edit?gid=1471249299#gid=1471249299';window.open(u.replace(/\/preview.*$/,'/edit?gid=1471249299#gid=1471249299'),'_blank','noopener')}
'''
if 'function getMonthlySheetFrame()' not in s:s=s.replace('</body>',monthly_js+'\n</body>',1)

# 4) Avoid relying on browser implicit element-id globals for staff + work update controls.
robust=r'''
function $id(id){return document.getElementById(id)}
'''
if 'function $id(id)' not in s:s=s.replace('</body>',robust+'\n</body>',1)

# version
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.29">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=829'",x);idx.write_text(x,encoding='utf-8')
print('V8.29 stability/shared data patch applied')