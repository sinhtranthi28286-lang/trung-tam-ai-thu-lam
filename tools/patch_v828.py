from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
b64=''.join(p.read_text(encoding='utf-8').strip() for p in parts)
s=gzip.decompress(base64.b64decode(b64)).decode('utf-8')
# trolyAI_tranthisinh is always administrator, including local fallback login.
# Replace staff-management admin checks with a robust helper based on current username/profile.
helper="""
function isThuLamAdmin(){
 try{
  const vals=[window.currentAppUsername,currentAppProfile?.username,currentAppProfile?.user_name,currentAppProfile?.login,localStorage.getItem('thu_lam_current_username'),localStorage.getItem('thu_lam_username')].filter(Boolean).map(x=>String(x).trim().toLowerCase());
  if(vals.includes('trolyai_tranthisinh')) return true;
 }catch(e){}
 return (typeof isAdmin!=='undefined'&&!!isAdmin);
}
"""
if 'function isThuLamAdmin()' not in s:
    pos=s.find('let STAFF_REGISTRY=[];')
    if pos>=0:s=s[:pos]+helper+s[pos:]
s=s.replace("typeof isAdmin!=='undefined'&&isAdmin", "isThuLamAdmin()")
# Capture username on local-login path wherever the known username is handled.
s=s.replace("currentAppProfile=localProfile;", "currentAppProfile=localProfile;window.currentAppUsername=String(localProfile?.username||localProfile?.user_name||localProfile?.login||'').trim();")
# Also infer admin from staff_name Trần Thị Sinh only when profile is local fallback and username field was omitted.
s=s.replace("function isThuLamAdmin(){\n try{", "function isThuLamAdmin(){\n try{\n  if(currentAppProfile&&String(currentAppProfile.staff_name||'').trim().toUpperCase()==='TRẦN THỊ SINH' && !currentAppProfile.auth_user_id) return true;")
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.28">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode(); chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html'); x=idx.read_text(encoding='utf-8'); x=re.sub(r"f\+'\?v=\d+'","f+'?v=828'",x); idx.write_text(x,encoding='utf-8')
print('V8.28 admin recognition applied')