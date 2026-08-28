from pathlib import Path
import base64,gzip,math,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')
# Remove stray raw JS injected before </body> in V8.29 and re-add inside a script block.
start=s.find("function getMonthlySheetFrame(){")
if start>=0:
 end=s.find("</body>",start)
 if end>=0:
  block=s[start:end]
  s=s[:start]+s[end:]
  s=s.replace('</body>','<script>\n'+block+'\n</script>\n</body>',1)
# Add compatibility getters for legacy code that relies on element-id globals.
compat="""
<script>
['ttStaffRows','ttStaffSearch','wUpdateTask','wUpdateStatus','wUpdateProgress','wUpdateOutNo','wUpdateOutDate','wUpdateResult','wUpdateNote','wUpdateFile'].forEach(function(id){
 try{if(!(id in window))Object.defineProperty(window,id,{configurable:true,get:function(){return document.getElementById(id)}})}catch(e){}
});
</script>
"""
if 'Object.defineProperty(window,id' not in s:s=s.replace('</body>',compat+'</body>',1)
# Version
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.30">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=830'",x);idx.write_text(x,encoding='utf-8')
print('V8.30 audit cleanup applied')