from pathlib import Path
import base64,gzip,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode()
terms=['SALARY','salary','localStorage','openMonthlySheet','reloadMonthlySheet','vdPdfViewer','CTRLKEY','function csave','saveSalary','renderSalary']
out=['# Targeted code inspection','']
for term in terms:
 out.append('## '+term)
 for m in list(re.finditer(re.escape(term),s,re.I))[:12]:
  a=max(0,m.start()-500);b=min(len(s),m.end()+1000)
  out.append('```text\n'+s[a:b].replace('```','` ` `')+'\n```')
Path('CODE_NOTES.md').write_text('\n'.join(out),encoding='utf-8')
print('written')