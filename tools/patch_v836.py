from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')

# 1. Report exports: admin chooses exact weekly/monthly sheet (gid) instead of exporting whole workbook.
old="""function exportWeeklyReport(){downloadGoogleSheetXlsx('1dnHvYauhrTaux2uNsh5hfy5qRr_KJygomD_RD0Ul7qk','Bao_cao_tuan_Ban_Xay_dung_Dang.xlsx')}
function exportMonthlyReport(){downloadGoogleSheetXlsx('1o7qxYI_F0N4B7X1o2uKvNUxcPwLlBwGr','Bao_cao_thang_Ban_Xay_dung_Dang.xlsx')}"""
new=r'''function exportSelectedGoogleSheet(id,gid,name){
 if(!ensureAdminExport())return;
 const url=`https://docs.google.com/spreadsheets/d/${id}/export?format=xlsx&gid=${encodeURIComponent(gid)}`;
 const a=document.createElement('a');a.href=url;a.target='_blank';a.rel='noopener';a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>a.remove(),1000)
}
function reportPeriodPrompt(kind){
 const label=kind==='week'?'tuần (ví dụ: 34)':'tháng (ví dụ: 8)';
 const v=prompt(`Nhập ${label} cần xuất:`,'')?.trim();if(!v)return null;
 return v.replace(/^0+/,'')||'0'
}
function findSheetOptionByPeriod(selectors,period){
 for(const id of selectors){const e=document.getElementById(id);if(!e)continue;const opts=[...e.options];const re=new RegExp(`(^|\\D)0?${period}(\\D|$)`,'i');const o=opts.find(x=>re.test((x.textContent||'').replace(/tháng|tuần/gi,' ')));if(o)return {gid:o.value,text:o.textContent.trim()}}
 return null
}
function exportWeeklyReport(){
 if(!ensureAdminExport())return;const p=reportPeriodPrompt('week');if(!p)return;const hit=findSheetOptionByPeriod(['weekSheetSelect','weeklySheetSelect','reportWeekSelect'],p);
 if(!hit)return alert(`Không tìm thấy sheet Tuần ${p} trong danh sách báo cáo. Hãy chọn đúng tuần trên màn hình rồi thử lại.`);
 exportSelectedGoogleSheet('1dnHvYauhrTaux2uNsh5hfy5qRr_KJygomD_RD0Ul7qk',hit.gid,`Bao_cao_tuan_${p}_Ban_Xay_dung_Dang.xlsx`)
}
function exportMonthlyReport(){
 if(!ensureAdminExport())return;const p=reportPeriodPrompt('month');if(!p)return;const hit=findSheetOptionByPeriod(['monthSheetSelect','monthlySheetSelect','reportMonthSelect'],p);
 if(!hit)return alert(`Không tìm thấy sheet Tháng ${p} trong danh sách báo cáo. Hãy chọn đúng tháng trên màn hình rồi thử lại.`);
 exportSelectedGoogleSheet('1o7qxYI_F0N4B7X1o2uKvNUxcPwLlBwGr',hit.gid,`Bao_cao_thang_${p}_Ban_Xay_dung_Dang.xlsx`)
}'''
if old in s:s=s.replace(old,new,1)

# 2. Meeting form: relabel fields to match desired structure without adding complexity.
s=s.replace('Nội dung/chương trình họp','I. NỘI DUNG CUỘC HỌP',1)
s=s.replace('Ý kiến thảo luận, nội dung đã thống nhất','1. Đánh giá kết quả thực hiện nhiệm vụ tuần/tháng trước',1)
s=s.replace('Kết luận chung của Trưởng Ban/chủ trì','2. Triển khai nhiệm vụ tuần/tháng sau và kết luận giao nhiệm vụ',1)
s=s.replace('Nhiệm vụ/Văn bản giao','Nhiệm vụ giao',1)

# 3. Replace Word body structure: I with items 1/2; assignments included in item 2; no document-number attachment language.
start=s.find("  const intro=`Ngày ${fmtVNDate(x.date)}")
end=s.find("  children.push(p('Thông báo này là căn cứ",start)
if start>=0 and end>start:
 body=r'''  const intro=`Ngày ${fmtVNDate(x.date)}, tại ${x.place||'[CẦN BỔ SUNG]'}, Ban Xây dựng Đảng xã Thư Lâm tổ chức cuộc họp do ${x.chair||'[CẦN BỔ SUNG]'} chủ trì. Thành phần: ${x.attend||'[CẦN BỔ SUNG]'}. Sau khi nghe các nội dung và ý kiến tại cuộc họp, Trưởng Ban/chủ trì kết luận như sau:`;children.push(p(intro));
  children.push(p('I. NỘI DUNG CUỘC HỌP',{bold:true,indent:false}));
  children.push(p('1. Đánh giá kết quả thực hiện nhiệm vụ tuần/tháng trước',{bold:true,indent:false}));
  children.push(p(x.discuss||x.agenda||'[CẦN BỔ SUNG]'));
  children.push(p('2. Triển khai nhiệm vụ tuần/tháng sau và kết luận giao nhiệm vụ',{bold:true,indent:false}));
  if(x.general)children.push(p(x.general));
  const tasks=x.tasks||[];
  if(tasks.length){tasks.forEach((t,i)=>{const task=taskText(t,['task','name','content','work']);const owner=taskText(t,['owner','person','assignee']);const prod=taskText(t,['product','result']);const due=taskText(t,['due','deadline']);let line=`${i+1}) ${task||'[CẦN BỔ SUNG]'}`;if(owner)line+=`; người/bộ phận thực hiện: ${owner}`;if(prod)line+=`; kết quả/sản phẩm: ${prod}`;if(due)line+=`; thời hạn: ${fmtVNDate(due)}`;children.push(p(line+'.'))})}
  else if(!x.general)children.push(p('[CẦN BỔ SUNG nhiệm vụ triển khai và kết luận giao nhiệm vụ]'));
'''
 s=s[:start]+body+s[end:]

# 4. Draft preview follows same simple structure.
# Keep source data untouched; only presentation/export changes.
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.36">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=836'",x);idx.write_text(x,encoding='utf-8')
print('V8.36 report period selection and meeting structure applied')