from pathlib import Path
import base64,gzip,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode()
out=['# Targeted code inspection','']
patterns=[
 ('salary-source',r'const\s+SALARY_SOURCE\s*=.*?(?=\n(?:const|let|function)\s+[A-Za-z_$])'),
 ('salary-functions',r'(?:function\s+(?:renderSalary2|saveSalaryRow|salarySave|slSave|updateSalary)[\s\S]{0,7000})'),
 ('control-storage',r'const\s+CTRLKEY[\s\S]{0,5000}'),
 ('monthly-functions',r'function\s+(?:openMonthlySheet|reloadMonthlySheet|showCenterPage)[\s\S]{0,2500}'),
 ('directive-file-db',r'const\s+VD_DB_NAME[\s\S]{0,5000}')]
for name,pat in patterns:
 out.append('## '+name)
 ms=list(re.finditer(pat,s,re.I))[:10]
 if not ms:out.append('NOT FOUND')
 for m in ms:out.append('```text\n'+m.group(0).replace('```','` ` `')+'\n```')
Path('CODE_NOTES.md').write_text('\n'.join(out),encoding='utf-8')
print('written')