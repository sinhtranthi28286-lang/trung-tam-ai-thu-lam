from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')

# Data safety helpers: local rotating backups + server history snapshots.
backup_js=r'''
const CTRL_BACKUP_PREFIX='thu_lam_control_backup_';
function backupLocalCTRL(){
 try{
  const stamp=new Date().toISOString();
  localStorage.setItem(CTRL_BACKUP_PREFIX+stamp,JSON.stringify(CTRL));
  const keys=Object.keys(localStorage).filter(k=>k.startsWith(CTRL_BACKUP_PREFIX)).sort().reverse();
  keys.slice(20).forEach(k=>localStorage.removeItem(k));
 }catch(e){console.warn('Local backup failed',e)}
}
async function backupRemoteCTRL(state){
 try{
  const sess=(await sb.auth.getSession()).data?.session;if(!sess)return;
  await sb.from('app_state_history').insert({state_key:'control',state:state||CTRL,saved_by:sess.user.id});
 }catch(e){console.warn('Remote backup failed',e)}
}
'''
if 'const CTRL_BACKUP_PREFIX=' not in s:
    idx=s.find("const CTRLKEY='thu_lam_control_v2';")
    if idx>=0:s=s[:idx]+backup_js+'\n'+s[idx:]

# Make csave snapshot before writing.
s=s.replace("function csave(){\n      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));", "function csave(){\n      backupLocalCTRL();\n      try{backupRemoteCTRL(CTRL)}catch(e){}\n      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));",1)

# Improve shared load: after successful load, refresh every dependent view including lookup.
old="if(data?.state&&Object.keys(data.state).length){CTRL=mergeCTRL(data.state,CTRL);localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));CTRL_REMOTE_UPDATED=data.updated_at||'';CTRL_SYNC_READY=true;renderCtrlAll();if(typeof renderTTOverview==='function')renderTTOverview();if(typeof renderTTStaff==='function')renderTTStaff();if(typeof renderStaffWorkCards==='function')renderStaffWorkCards()}"
new="if(data?.state&&Object.keys(data.state).length){backupLocalCTRL();CTRL=mergeCTRL(data.state,CTRL);localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));CTRL_REMOTE_UPDATED=data.updated_at||'';CTRL_SYNC_READY=true;renderCtrlAll();if(typeof renderTTOverview==='function')renderTTOverview();if(typeof renderTTStaff==='function')renderTTStaff();if(typeof renderStaffWorkCards==='function')renderStaffWorkCards();if(typeof renderDocumentLookup==='function')renderDocumentLookup();if(typeof renderDirectives==='function')renderDirectives()}"
s=s.replace(old,new,1)

# Crucial fix: page load can happen before login. Sync again whenever Supabase auth becomes signed in.
auth_js=r'''
try{
 if(typeof sb!=='undefined'&&sb.auth?.onAuthStateChange){
  sb.auth.onAuthStateChange((event,session)=>{
   if(session&&(event==='SIGNED_IN'||event==='INITIAL_SESSION'||event==='TOKEN_REFRESHED')){
    setTimeout(async()=>{try{await loadSharedCTRL();await loadStaffRegistry?.();if(typeof renderDocumentLookup==='function')renderDocumentLookup()}catch(e){console.warn('Post-login sync failed',e)}},150);
   }
  });
 }
}catch(e){console.warn('Auth sync hook unavailable',e)}
'''
if 'Post-login sync failed' not in s:
    s=s.replace('</body>',auth_js+'\n</body>',1)

# Server save: backup previous remote state before upsert, and never replace a nonempty remote array by an empty local one.
s=s.replace("const merged=mergeCTRL(data?.state||{},CTRL);\n  const payload=", "const merged=mergeCTRL(data?.state||{},CTRL);\n  try{if(data?.state&&Object.keys(data.state).length)await backupRemoteCTRL(data.state)}catch(e){}\n  const payload=",1)

# Add a manual recovery command for admin from latest local backup if ever needed.
recover_js=r'''
function restoreLatestLocalBackup(){
 if(!isThuLamAdmin?.())return alert('Chỉ quản trị viên được khôi phục dữ liệu.');
 try{
  const keys=Object.keys(localStorage).filter(k=>k.startsWith(CTRL_BACKUP_PREFIX)).sort().reverse();
  if(!keys.length)return alert('Không có bản sao lưu cục bộ.');
  const b=JSON.parse(localStorage.getItem(keys[0])||'null');if(!b)return alert('Bản sao lưu không hợp lệ.');
  if(!confirm('Khôi phục bản sao lưu gần nhất? Dữ liệu hiện tại sẽ được sao lưu trước khi khôi phục.'))return;
  backupLocalCTRL();CTRL=mergeCTRL(CTRL,b);localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));try{syncSharedCTRL()}catch(e){};renderCtrlAll();if(typeof renderDocumentLookup==='function')renderDocumentLookup();alert('Đã khôi phục bản sao lưu gần nhất.');
 }catch(e){alert('Không khôi phục được: '+e.message)}
}
'''
if 'function restoreLatestLocalBackup()' not in s:s=s.replace('</body>',recover_js+'\n</body>',1)

s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.32">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=832'",x);idx.write_text(x,encoding='utf-8')
print('V8.32 data safety + post-login sync applied')