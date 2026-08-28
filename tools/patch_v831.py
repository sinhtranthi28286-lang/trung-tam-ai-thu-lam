from pathlib import Path
import base64,gzip,math,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')
fix="""
<script>
function syncMonthlySheetTime(){
 const now=new Date();
 const text='Cập nhật: '+now.toLocaleString('vi-VN');
 const ids=['monthlySyncTime','monthSyncTime','monthlySheetTime','mrSyncTime'];
 ids.forEach(id=>{const el=document.getElementById(id);if(el)el.textContent=text});
 return text;
}
</script>
"""
if 'function syncMonthlySheetTime()' not in s:s=s.replace('</body>',fix+'</body>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.31">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=831'",x);idx.write_text(x,encoding='utf-8')
print('V8.31 monthly sync helper fixed')