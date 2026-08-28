from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')

# Admin-only guard on meeting notice exports.
s=s.replace("async function exportCurrentMeetingNoticeWord(){const snap=meetingFieldSnapshot();", "async function exportCurrentMeetingNoticeWord(){if(!isThuLamAdmin?.())return alert('Chỉ Quản trị viên được xuất Thông báo kết luận.');const snap=meetingFieldSnapshot();",1)
s=s.replace("async function exportSavedMeetingNoticeWord(id){const x=", "async function exportSavedMeetingNoticeWord(id){if(!isThuLamAdmin?.())return alert('Chỉ Quản trị viên được xuất Thông báo kết luận.');const x=",1)

# Mark meeting Word buttons as admin-only (saved list button is generated dynamically too).
s=s.replace('class="btn light" type="button" onclick="exportCurrentMeetingNoticeWord()"','class="btn light admin-export-only" type="button" onclick="exportCurrentMeetingNoticeWord()"',1)
s=s.replace('<button class="btn light" onclick="exportSavedMeetingNoticeWord(\'${x.id}\')">📄 Word</button>', '<button class="btn light admin-export-only" onclick="exportSavedMeetingNoticeWord(\'${x.id}\')">📄 Word</button>')

# Add export buttons to weekly and monthly report toolbars.
weekly_marker='<button class="btn light" onclick="openOriginalSheet()">↗ Mở toàn màn hình</button>'
if weekly_marker in s and 'exportWeeklyReport' not in s:
    s=s.replace(weekly_marker, weekly_marker+'\n      <button class="btn light admin-export-only" onclick="exportWeeklyReport()">⬇ Xuất báo cáo</button>',1)
monthly_marker='<button class="btn light" onclick="openMonthlySheet()">↗ Mở Google Sheet</button>'
if monthly_marker in s and 'exportMonthlyReport' not in s:
    s=s.replace(monthly_marker, monthly_marker+'\n      <button class="btn light admin-export-only" onclick="exportMonthlyReport()">⬇ Xuất báo cáo</button>',1)

# Export current Google Sheet as XLSX. Only trolyAI_tranthisinh/admin can do this.
js=r'''
function ensureAdminExport(){if(!isThuLamAdmin?.()){alert('Chỉ Quản trị viên được xuất báo cáo và Thông báo kết luận.');return false}return true}
function downloadGoogleSheetXlsx(id,name){
 if(!ensureAdminExport())return;
 const a=document.createElement('a');a.href=`https://docs.google.com/spreadsheets/d/${id}/export?format=xlsx`;a.target='_blank';a.rel='noopener';a.download=name||'Bao_cao.xlsx';document.body.appendChild(a);a.click();setTimeout(()=>a.remove(),1000)
}
function exportWeeklyReport(){downloadGoogleSheetXlsx('1dnHvYauhrTaux2uNsh5hfy5qRr_KJygomD_RD0Ul7qk','Bao_cao_tuan_Ban_Xay_dung_Dang.xlsx')}
function exportMonthlyReport(){downloadGoogleSheetXlsx('1o7qxYI_F0N4B7X1o2uKvNUxcPwLlBwGr','Bao_cao_thang_Ban_Xay_dung_Dang.xlsx')}
function applyAdminExportVisibility(){const ok=!!isThuLamAdmin?.();document.querySelectorAll('.admin-export-only').forEach(el=>el.style.display=ok?'':'none')}
window.addEventListener('load',()=>setTimeout(applyAdminExportVisibility,1800));
try{if(typeof sb!=='undefined'&&sb.auth?.onAuthStateChange)sb.auth.onAuthStateChange(()=>setTimeout(applyAdminExportVisibility,250))}catch(e){}
'''
if 'function exportWeeklyReport()' not in s:
    s=s.replace('</body>','<script>\n'+js+'\n</script>\n</body>',1)

# Ensure dynamically rendered meeting list re-applies visibility.
s=s.replace("body.innerHTML=arr.length?arr.map", "body.innerHTML=arr.length?arr.map",1)
# append visibility call at end of renderMeetingNotices if exact tail found
s=s.replace("'Chưa có Thông báo kết luận nào được lưu.</td></tr>'\n}", "'Chưa có Thông báo kết luận nào được lưu.</td></tr>';try{applyAdminExportVisibility()}catch(e){}\n}",1)

s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.35">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=835'",x);idx.write_text(x,encoding='utf-8')
print('V8.35 admin-only exports applied')