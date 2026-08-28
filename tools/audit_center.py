from pathlib import Path
import base64,gzip,re,json,subprocess,sys
from html.parser import HTMLParser
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
b64=''.join(p.read_text(encoding='utf-8').strip() for p in parts)
s=gzip.decompress(base64.b64decode(b64)).decode('utf-8')
Path('/tmp/app.html').write_text(s,encoding='utf-8')

class PHTML(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.scripts=[];self.in_script=False;self.buf=[];self.src=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  if tag=='script':
   if d.get('src'):self.src.append(d['src'])
   else:self.in_script=True;self.buf=[]
 def handle_endtag(self,tag):
  if tag=='script' and self.in_script:self.scripts.append(''.join(self.buf));self.in_script=False
 def handle_data(self,data):
  if self.in_script:self.buf.append(data)
p=PHTML();p.feed(s)
js='\n;\n'.join(p.scripts)
Path('/tmp/app.js').write_text(js,encoding='utf-8')
report=[]
def add(level,name,detail=''): report.append({'level':level,'name':name,'detail':detail})
# JS syntax
r=subprocess.run(['node','--check','/tmp/app.js'],capture_output=True,text=True)
add('PASS' if r.returncode==0 else 'FAIL','JavaScript syntax',r.stderr.strip()[:2000])
# duplicate ids
from collections import Counter
c=Counter(p.ids);dups={k:v for k,v in c.items() if v>1}
add('PASS' if not dups else 'WARN','Duplicate HTML IDs',json.dumps(dups,ensure_ascii=False))
# inline onclick function refs vs definitions/window assignments/builtins
refs=set(re.findall(r'on(?:click|change|input|submit|keydown)="\s*([A-Za-z_$][\w$]*)\s*\(',s))
defs=set(re.findall(r'(?:function\s+|(?:window\.)?)([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:function|\([^)]*\)\s*=>)',js))|set(re.findall(r'function\s+([A-Za-z_$][\w$]*)\s*\(',js))
missing=sorted(x for x in refs if x not in defs and x not in {'alert','confirm','open','close','print'})
add('PASS' if not missing else 'FAIL','Inline handlers defined',', '.join(missing[:100]))
# document id references
idrefs=set(re.findall(r'getElementById\([\'\"]([^\'\"]+)',js))
missing_ids=sorted(idrefs-set(p.ids))
add('PASS' if not missing_ids else 'WARN','getElementById targets exist',', '.join(missing_ids[:100]))
# persistence inventory
local_keys=sorted(set(re.findall(r'localStorage\.(?:getItem|setItem|removeItem)\([\'\"]([^\'\"]+)',js)))
indexed=sorted(set(re.findall(r'indexedDB\.open\([\'\"]([^\'\"]+)',js)))
sb_tables=sorted(set(re.findall(r"\.from\(['\"]([^'\"]+)",js)))
add('INFO','localStorage keys',', '.join(local_keys))
add('INFO','IndexedDB databases',', '.join(indexed))
add('INFO','Supabase tables referenced',', '.join(sb_tables))
# critical shared-use risks
critical=[]
for needle,label in [('thu_lam_control_v2','Công việc/kết luận/báo cáo điều khiển đang lưu localStorage'),('ThuLamDirectiveFiles','File văn bản đang lưu IndexedDB cục bộ')]:
 if needle in s:critical.append(label)
if re.search(r'SALARY.*localStorage|localStorage.*salary|salary.*localStorage',s,re.I|re.S):critical.append('Dữ liệu cập nhật nâng lương có dấu hiệu lưu cục bộ')
add('WARN' if critical else 'PASS','Shared-data persistence', '; '.join(critical))
# version / loader
m=re.search(r'thu-lam-version" content="([^"]+)',s);add('INFO','App version',m.group(1) if m else 'unknown')
# external scripts availability list
add('INFO','External scripts','; '.join(p.src))
# common risky globals referenced as implicit DOM globals
implicit=sorted(set(re.findall(r'\b(ttStaffRows|ttStaffSearch|wUpdateTask|wUpdateStatus|wUpdateProgress|wUpdateOutNo|wUpdateOutDate|wUpdateResult|wUpdateNote|wUpdateFile)\b',js)))
add('INFO','Implicit DOM globals used',', '.join(implicit))
# produce markdown
lines=['# Trung tâm AI — Audit report','']
for x in report:
 lines.append(f"- **{x['level']} — {x['name']}**" + (f": {x['detail']}" if x['detail'] else ''))
Path('AUDIT_REPORT.md').write_text('\n'.join(lines),encoding='utf-8')
print('\n'.join(lines))
if any(x['level']=='FAIL' for x in report):sys.exit(2)
