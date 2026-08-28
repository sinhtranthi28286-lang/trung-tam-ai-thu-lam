from pathlib import Path
import base64,gzip,math,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')

# 1) Remove raw JavaScript accidentally rendered as text at page bottom; reinsert inside a script tag.
auth_raw="""try{\n if(typeof sb!=='undefined'&&sb.auth?.onAuthStateChange){\n  sb.auth.onAuthStateChange((event,session)=>{\n   if(session&&(event==='SIGNED_IN'||event==='INITIAL_SESSION'||event==='TOKEN_REFRESHED')){\n    setTimeout(async()=>{try{await loadSharedCTRL();await loadStaffRegistry?.();if(typeof renderDocumentLookup==='function')renderDocumentLookup()}catch(e){console.warn('Post-login sync failed',e)}},150);\n   }\n  });\n }\n}catch(e){console.warn('Auth sync hook unavailable',e)}"""
recover_raw="""function restoreLatestLocalBackup(){\n if(!isThuLamAdmin?.())return alert('Chỉ quản trị viên được khôi phục dữ liệu.');\n try{\n  const keys=Object.keys(localStorage).filter(k=>k.startsWith(CTRL_BACKUP_PREFIX)).sort().reverse();\n  if(!keys.length)return alert('Không có bản sao lưu cục bộ.');\n  const b=JSON.parse(localStorage.getItem(keys[0])||'null');if(!b)return alert('Bản sao lưu không hợp lệ.');\n  if(!confirm('Khôi phục bản sao lưu gần nhất? Dữ liệu hiện tại sẽ được sao lưu trước khi khôi phục.'))return;\n  backupLocalCTRL();CTRL=mergeCTRL(CTRL,b);localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));try{syncSharedCTRL()}catch(e){};renderCtrlAll();if(typeof renderDocumentLookup==='function')renderDocumentLookup();alert('Đã khôi phục bản sao lưu gần nhất.');\n }catch(e){alert('Không khôi phục được: '+e.message)}\n}"""
# Remove raw occurrences only when they are outside script near </body>.
s=s.replace(auth_raw+'\n', '')
s=s.replace(recover_raw+'\n', '')
end_js='''<script>\n'''+auth_raw+'\n'+recover_raw+'''\n</script>\n'''
if 'Post-login sync failed' not in s or 'function restoreLatestLocalBackup()' not in s:
    s=s.replace('</body>',end_js+'</body>',1)
else:
    # If occurrences remain in existing scripts, ensure no duplicate raw tail is added.
    pass

# 2) Make remote server data authoritative for matching records; local data only fills records missing on server.
old="""function ctrlMergeArray(remote,local,key='id'){
 const m=new Map(); (remote||[]).forEach(x=>m.set(String(x?.[key]??x?.name??JSON.stringify(x)),x));
 (local||[]).forEach(x=>m.set(String(x?.[key]??x?.name??JSON.stringify(x)),x)); return [...m.values()]
}"""
new="""function ctrlMergeArray(remote,local,key='id'){
 const m=new Map();
 (local||[]).forEach(x=>m.set(String(x?.[key]??x?.name??JSON.stringify(x)),x));
 (remote||[]).forEach(x=>{const k=String(x?.[key]??x?.name??JSON.stringify(x));const l=m.get(k);m.set(k,l?{...l,...x}:x)});
 return [...m.values()]
}"""
s=s.replace(old,new,1)

# 3) Recover any directive already stored in the legacy Supabase xa_directives table when CTRL.directives is empty.
recover_directives=r'''
async function recoverLegacyDirectives(){
 try{
  if(typeof sb==='undefined')return;
  ensureDirectives?.();
  const {data,error}=await sb.from('xa_directives').select('*').order('id',{ascending:true});if(error||!data?.length)return;
  const existing=new Set((CTRL.directives||[]).map(x=>String(x.no||x.document_no||'').trim()+'|'+String(x.title||'').trim()));
  let changed=false;
  for(const d of data){
   const k=String(d.document_no||'').trim()+'|'+String(d.title||'').trim();if(existing.has(k))continue;
   CTRL.directives.push({id:'legacy-'+d.id,no:d.document_no||'',date:d.issued_date||'',title:d.title||'',area:d.category||'Văn bản chỉ đạo',summary:d.summary||'',fileUrl:d.file_url||'',source:'xa_directives'});existing.add(k);changed=true;
  }
  if(changed){localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));renderDirectives?.();renderDocumentLookup?.()}
 }catch(e){console.warn('Legacy directive recovery skipped',e)}
}
'''
if 'function recoverLegacyDirectives()' not in s:
    idx=s.find("function openCtrl(p){")
    if idx>=0:s=s[:idx]+recover_directives+'\n'+s[idx:]
# call after shared load and login
s=s.replace("await loadSharedCTRL();await loadStaffRegistry?.();if(typeof renderDocumentLookup==='function')renderDocumentLookup()", "await loadSharedCTRL();await recoverLegacyDirectives();await loadStaffRegistry?.();if(typeof renderDocumentLookup==='function')renderDocumentLookup()")

# 4) Keep saved salary values from Supabase visible even if stale local data exists.
# The remote-authoritative merge above handles this. Also refresh lookup after login.

# 5) Version and cache bump.
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.33">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=833'",x);idx.write_text(x,encoding='utf-8')
print('V8.33 cleanup/data recovery patch applied')