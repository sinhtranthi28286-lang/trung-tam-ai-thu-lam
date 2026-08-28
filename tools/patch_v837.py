from pathlib import Path
import base64,gzip,math,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')
# V8.36 incorrectly searched for non-existent select elements. Export exactly the currently displayed Google Sheet tab (gid), and let admin type period only for filename/confirmation.
pat=re.compile(r"function findSheetOptionByPeriod\(selectors,period\)\{.*?function exportMonthlyReport\(\)\{.*?\n\}",re.S)
rep=r'''function currentReportGid(kind){
 const frameIds=kind==='week'?['weeklyFrame','weekFrame','reportFrame','sheetFrame']:['monthlyFrame','monthFrame','monthlySheetFrame'];
 for(const id of frameIds){const f=document.getElementById(id);if(f&&f.src){const m=f.src.match(/[?&]gid=(\d+)/);if(m)return m[1]}}
 const panes=[...document.querySelectorAll('iframe')].filter(f=>f.offsetParent!==null&&/docs\.google\.com\/spreadsheets/.test(f.src||''));
 for(const f of panes){const m=(f.src||'').match(/[?&]gid=(\d+)/);if(m)return m[1]}
 return kind==='week'?'636727831':'1471249299'
}
function exportWeeklyReport(){
 if(!ensureAdminExport())return;const p=reportPeriodPrompt('week');if(!p)return;
 const gid=currentReportGid('week');
 exportSelectedGoogleSheet('1dnHvYauhrTaux2uNsh5hfy5qRr_KJygomD_RD0Ul7qk',gid,`Bao_cao_tuan_${p}_Ban_Xay_dung_Dang.xlsx`)
}
function exportMonthlyReport(){
 if(!ensureAdminExport())return;const p=reportPeriodPrompt('month');if(!p)return;
 const gid=currentReportGid('month');
 exportSelectedGoogleSheet('1o7qxYI_F0N4B7X1o2uKvNUxcPwLlBwGr',gid,`Bao_cao_thang_${p}_Ban_Xay_dung_Dang.xlsx`)
}'''
s,n=pat.subn(rep,s,count=1)
if n!=1: raise SystemExit('Could not replace V8.36 report export block')
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.37">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode();chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text();x=re.sub(r"f\+'\?v=\d+'","f+'?v=837'",x);idx.write_text(x)
print('V8.37 fixed report export')