# Targeted code inspection

## SALARY
```text
rl('directives',this)"><span>📣</span>Văn bản chỉ đạo</button>
  <button class="tt-left-item" data-perm="weeklyReport" onclick="showCenterPage('sheet',this)"><span>🧾</span>Báo cáo tuần</button>
  <button class="tt-left-item" data-perm="monthlyReport" onclick="showCenterPage('monthreport',this)"><span>📅</span>Báo cáo tháng</button>
  <button class="tt-left-item" data-perm="meeting" onclick="openLeftCtrl('meeting',this)"><span>📝</span>Kết luận họp</button>
  <button class="tt-left-item" data-perm="salary" onclick="openLeftCtrl('salary',this)"><span>💰</span>Nâng lương</button>

  <div class="tt-left-sep">AI & NGHIỆP VỤ</div>
  <button class="tt-left-item" data-perm="ai" data-page="ai" onclick="showCenterPage('ai',this)"><span>🤖</span>AI theo lĩnh vực</button>
  <button class="tt-left-item" data-perm="lookup" data-page="library" onclick="showCenterPage('library',this)"><span>🔎</span>Tra cứu văn bản</button>

  <div class="tt-left-lotus">❀</div>
</div>
<div class="tt-mobile-menu no-print">
  <button onclick="toggleLeftMenu()">☰ MENU</button>
  <b id="ttMobileTitle">Theo dõi công việc</b>
</div>

<div class="notice">
  <div class="notice-icon">📣</div>
  <div><strong>Bản chính thức – Kho dữ liệu trực tuyến:</strong> Mỗi công việc được đặt cùng <strong>câu lệnh AI + biểu mẫu + tài liệu tham khảo</strong>. Kho nghiệp vụ số đã được kết nối lưu trữ trực tuyến để cán bộ có thể tải lên, xem và tải xuống tài liệu dùng chung.</div>
</div>



<div id="ttaiHome" class="ttai-home">
  <div class="ttai
```
```text
/span>Văn bản chỉ đạo</button>
  <button class="tt-left-item" data-perm="weeklyReport" onclick="showCenterPage('sheet',this)"><span>🧾</span>Báo cáo tuần</button>
  <button class="tt-left-item" data-perm="monthlyReport" onclick="showCenterPage('monthreport',this)"><span>📅</span>Báo cáo tháng</button>
  <button class="tt-left-item" data-perm="meeting" onclick="openLeftCtrl('meeting',this)"><span>📝</span>Kết luận họp</button>
  <button class="tt-left-item" data-perm="salary" onclick="openLeftCtrl('salary',this)"><span>💰</span>Nâng lương</button>

  <div class="tt-left-sep">AI & NGHIỆP VỤ</div>
  <button class="tt-left-item" data-perm="ai" data-page="ai" onclick="showCenterPage('ai',this)"><span>🤖</span>AI theo lĩnh vực</button>
  <button class="tt-left-item" data-perm="lookup" data-page="library" onclick="showCenterPage('library',this)"><span>🔎</span>Tra cứu văn bản</button>

  <div class="tt-left-lotus">❀</div>
</div>
<div class="tt-mobile-menu no-print">
  <button onclick="toggleLeftMenu()">☰ MENU</button>
  <b id="ttMobileTitle">Theo dõi công việc</b>
</div>

<div class="notice">
  <div class="notice-icon">📣</div>
  <div><strong>Bản chính thức – Kho dữ liệu trực tuyến:</strong> Mỗi công việc được đặt cùng <strong>câu lệnh AI + biểu mẫu + tài liệu tham khảo</strong>. Kho nghiệp vụ số đã được kết nối lưu trữ trực tuyến để cán bộ có thể tải lên, xem và tải xuống tài liệu dùng chung.</div>
</div>



<div id="ttaiHome" class="ttai-home">
  <div class="ttai-nav">
    <button onclick="goT
```
```text
hảo</strong>. Kho nghiệp vụ số đã được kết nối lưu trữ trực tuyến để cán bộ có thể tải lên, xem và tải xuống tài liệu dùng chung.</div>
</div>



<div id="ttaiHome" class="ttai-home">
  <div class="ttai-nav">
    <button onclick="goTT('overview')">🏠 Tổng quan</button>
    <button onclick="goTT('staff')">👥 Danh sách cán bộ</button>
    <button onclick="openCtrl('work')">📊 Công việc & văn bản</button>
    <button onclick="openCtrl('meeting')">📝 Kết luận họp</button>
    <button onclick="openCtrl('salary')">💰 Nâng lương</button>
    <button onclick="openCtrl('directives')">📣 Văn bản chỉ đạo</button><button onclick="goTT('aiwork')">🤖 AI theo lĩnh vực</button>
    <button onclick="goTT('libraryTop')">🔎 Tra cứu văn bản</button>
  </div>

  <section id="overview" class="tt-section">
    <div class="tt-section-head">
      <div><div class="tt-kicker">TRUNG TÂM AI – BAN XÂY DỰNG ĐẢNG</div><h2>TỔNG QUAN CÔNG VIỆC</h2>
      <p>Theo dõi tình hình thực hiện nhiệm vụ của Ban tại thời điểm mở Trung tâm.</p></div>
      <div id="ttNow" class="tt-now"></div>
    </div>
    <div class="tt-kpis">
      <div class="tt-kpi"><span>👥</span><div><b>Cán bộ Ban</b><strong id="ttStaffCount">0</strong></div></div>
      <div class="tt-kpi"><span>📌</span><div><b>Tổng nhiệm vụ</b><strong id="ttTaskCount">0</strong></div></div>
      <div class="tt-kpi"><span>⏳</span><div><b>Đang thực hiện</b><strong id="ttDoingCount">0</strong></div></div>
      <div class="tt-kpi warning"><span>⚠</span><div><b>Sắp đến hạn</b>
```
```text
    <div class="tt-function" onclick="openCtrl('meeting')"><div class="tt-icon">📝</div><b>Kết luận họp Ban</b><p>Tạo dự thảo kết luận, gắn nhiệm vụ, người thực hiện, kết quả/sản phẩm và thời hạn.</p><span>Tạo Kết luận →</span></div>
      <div class="tt-function" onclick="openCtrl('directives')"><div class="tt-icon">📣</div><b>Văn bản chỉ đạo</b><p>Lưu, tra cứu và thống kê văn bản chỉ đạo theo tuần, tháng, năm.</p><span>Mở Văn bản chỉ đạo →</span></div><div class="tt-function" onclick="openCtrl('salary')"><div class="tt-icon">💰</div><b>Theo dõi nâng lương</b><p>Theo dõi 36 CBCC khối Đảng, ngày đến hạn, đếm ngược và cập nhật quyết định đã nâng.</p><span>Mở theo dõi →</span></div>
    </div>
  </section>
</div>


<section id="sheetPage" class="tt-section" style="display:none">
  <div class="tt-section-head compact">
    <div><div class="tt-kicker">BÁO CÁO DÙNG CHUNG</div><h2>BIỂU BÁO CÁO GOOGLE SHEET</h2>
    <p>Cán bộ nhập trực tiếp trên biểu Google Sheet ngay trong Trung tâm AI, không cần mở thêm tab riêng.</p></div>
  </div>
  <div class="sheet-toolbar">
    <div>
      <b>Biểu báo cáo tuần của Ban Xây dựng Đảng</b>
      <span>Dữ liệu vẫn lưu trên Google Sheet gốc.</span>
    </div>
    <div class="sheet-actions">
      <button class="btn light" onclick="reloadEmbeddedSheet()">↻ Tải lại</button>
      <button class="btn light" onclick="openOriginalSheet()">↗ Mở toàn màn hình</button>
    </div>
  </div>
  <div class="sheet-note">Nếu Google yêu cầu đăng nhập, cán bộ đăng nhập tài k
```
```text
Ctrl()">Đóng ✕</button></div>
 <div class="ctrl-tabs">
  <button class="ctrl-tab" data-c="meeting" onclick="switchCtrl('meeting')">📝 Kết luận họp</button>
  <button class="ctrl-tab" data-c="aiassign" onclick="switchCtrl('aiassign')">📥🤖 AI giao việc</button>
  <button class="ctrl-tab" data-c="work" onclick="switchCtrl('work')">📊 Công việc & văn bản</button>
  <button class="ctrl-tab" data-c="directives" onclick="switchCtrl('directives')">📣 Văn bản chỉ đạo</button><button class="ctrl-tab" data-c="salary" onclick="switchCtrl('salary')">💰 Nâng lương</button>
 </div>

 <div id="c-meeting" class="ctrl-pane">
  <div class="ctrl-note"><b>Nguyên tắc:</b> hệ thống chỉ sắp xếp nội dung đã nhập, không tự tạo số liệu, căn cứ, tên người hoặc mốc thời gian. Chỗ thiếu được đánh dấu [CẦN BỔ SUNG].</div>
  <div class="ctrl-form">
   <div><label>Ngày họp</label><input id="mhDate" type="date"></div><div><label>Địa điểm</label><input id="mhPlace"></div><div><label>Chủ trì</label><select id="mhChair"></select></div><div><label>Thư ký</label><select id="mhSec"></select></div>
   <div class="span2"><label>Thành phần dự họp</label><textarea id="mhAttend">Các thành viên trong Ban Xây dựng Đảng</textarea></div><div class="span2"><label>Nội dung/chương trình họp</label><textarea id="mhAgenda"></textarea></div>
   <div class="full"><label>Ý kiến thảo luận, nội dung đã thống nhất</label><textarea id="mhDiscuss"></textarea></div>
   <div class="full"><label>Kết luận chung của Trưởng Ban/chủ trì</label><textarea 
```
```text

 <div class="ctrl-tabs">
  <button class="ctrl-tab" data-c="meeting" onclick="switchCtrl('meeting')">📝 Kết luận họp</button>
  <button class="ctrl-tab" data-c="aiassign" onclick="switchCtrl('aiassign')">📥🤖 AI giao việc</button>
  <button class="ctrl-tab" data-c="work" onclick="switchCtrl('work')">📊 Công việc & văn bản</button>
  <button class="ctrl-tab" data-c="directives" onclick="switchCtrl('directives')">📣 Văn bản chỉ đạo</button><button class="ctrl-tab" data-c="salary" onclick="switchCtrl('salary')">💰 Nâng lương</button>
 </div>

 <div id="c-meeting" class="ctrl-pane">
  <div class="ctrl-note"><b>Nguyên tắc:</b> hệ thống chỉ sắp xếp nội dung đã nhập, không tự tạo số liệu, căn cứ, tên người hoặc mốc thời gian. Chỗ thiếu được đánh dấu [CẦN BỔ SUNG].</div>
  <div class="ctrl-form">
   <div><label>Ngày họp</label><input id="mhDate" type="date"></div><div><label>Địa điểm</label><input id="mhPlace"></div><div><label>Chủ trì</label><select id="mhChair"></select></div><div><label>Thư ký</label><select id="mhSec"></select></div>
   <div class="span2"><label>Thành phần dự họp</label><textarea id="mhAttend">Các thành viên trong Ban Xây dựng Đảng</textarea></div><div class="span2"><label>Nội dung/chương trình họp</label><textarea id="mhAgenda"></textarea></div>
   <div class="full"><label>Ý kiến thảo luận, nội dung đã thống nhất</label><textarea id="mhDiscuss"></textarea></div>
   <div class="full"><label>Kết luận chung của Trưởng Ban/chủ trì</label><textarea id="mhGeneral"></textarea></d
```
```text
><button class="btn light" onclick="buildDirectiveSummary()">↻ Cập nhật danh sách</button><button class="btn light" onclick="copyDirectiveSummary()">📋 Sao chép báo cáo</button><button class="btn primary" onclick="sendSummaryToAIReview()">🤖 Phân tích nhiệm vụ</button></div>
 </div>
 <div id="vdSummaryStatus" class="ctrl-note">Danh sách văn bản được tổng hợp tự động theo lĩnh vực.</div>
 <div id="vdSummaryBox"></div>
</div>
<div id="vdGrouped" style="display:none!important"></div></div><div id="c-salary" class="ctrl-pane">
  <div class="ctrl-kpis"><div class="ctrl-kpi"><b>Tổng CBCC</b><strong id="slTotal">36</strong></div><div class="ctrl-kpi"><b>Quá hạn</b><strong id="slLate">0</strong></div><div class="ctrl-kpi"><b>≤30 ngày</b><strong id="sl30">0</strong></div><div class="ctrl-kpi"><b>31–90 ngày</b><strong id="sl90">0</strong></div><div class="ctrl-kpi"><b>Đã có QĐ/Ghi chú nâng</b><strong id="slRaised">0</strong></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><o
```
```text
QĐ/Ghi chú nâng</b><strong id="slRaised">0</strong></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5
```
```text
g></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5d7cd;padding-top:16px">
    <div id="whCurrent" c
```
```text
rSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5d7cd;padding-top:16px">
    <div id="whCurrent" class="wh-current">Chọn một nhóm nghiệp vụ ở phía trên.</div>
    <div class="wh-toolbar">
      <button class="btn primary" onclick="chooseUploadFiles()">＋ Tải tài liệu lên</button>
      <button class="btn light" onclick="loadWarehouseFiles()">↻ Làm mới danh sách</button>
      <input id="whSearch" class="wh-search" placeholder="Tìm theo tên file..." oninput="renderWarehouseFiles()">
      <input id="hiddenUploader" type="file" multiple style="display:none">
    </div>
    <div id="warehouseIn
```
```text
NH", "title": "ĐUV, Phó trưởng ban Xây dựng Đảng", "area": "Phụ trách công tác Đảng, đảng viên"}, {"name": "TRƯƠNG HỮU LUYỆN", "title": "ĐUV, Phó trưởng ban Xây dựng Đảng", "area": "Phụ trách công tác Tuyên giáo"}];

const APP_PERMISSION_DEFS=[
 ['overview','Tổng quan'],['staff','Danh sách cán bộ'],['staffWork','Theo dõi công việc'],
 ['work','Công việc & văn bản'],['directives','Văn bản chỉ đạo'],['weeklyReport','Báo cáo tuần'],
 ['monthlyReport','Báo cáo tháng'],['meeting','Kết luận họp'],
 ['salary','Nâng lương'],['ai','AI theo lĩnh vực'],['lookup','Tra cứu văn bản']
];
const APP_DEFAULT_PERMS=Object.fromEntries(APP_PERMISSION_DEFS.map(x=>[x[0],true]));

const BAN_QUICK_ACCOUNTS=[
 {name:'NGUYỄN TRỌNG HẢI',username:'trolyAI_nguyentronghai'},
 {name:'TÔ VĂN NGỌC',username:'trolyAI_tovanngoc'},
 {name:'TRẦN THỊ SINH',username:'trolyAI_tranthisinh'},
 {name:'ĐÀO THỊ THANH VÂN',username:'trolyAI_daothithanhvan'},
 {name:'NGUYỄN BÁ MẠNH',username:'trolyAI_nguyenbamanh'},
 {name:'NGÔ THANH NGÀ',username:'trolyAI_ngothanhnga'},
 {name:'NGUYỄN THỊ VÂN ANH',username:'trolyAI_nguyenthivananh'},
 {name:'TRƯƠNG HỮU LUYỆN',username:'trolyAI_truonghuuluyen'}
];

function lockSetMsg(msg,type=''){
 const e=document.getElementById('lockMsg');if(e){e.className='app-lock-msg'+(type?' '+type:'');e.textContent=msg}
}
function lockVisual(){
 document.body.classList.add('app-locked');
 document.getElementById('appLockScreen')?.classList.remove('unlocked');
}
function unlockVisual(){
 document.body.cla
```
```text
tối thiểu 6 ký tự):');if(!pw)return;try{await adminUserApi({action:'password',user_id:uid,password:pw});setAdminMsg('Đã đổi mật khẩu.','ok')}catch(e){setAdminMsg(e.message,'err')}}
async function toggleAppUser(uid,state){if(!confirm(state?'Mở lại tài khoản này?':'Khóa tài khoản này?'))return;try{await adminUserApi({action:'status',user_id:uid,is_active:state});setAdminMsg(state?'Đã mở tài khoản.':'Đã khóa tài khoản.','ok');await loadAppUsersAdmin()}catch(e){setAdminMsg(e.message,'err')}}

const SALARY_SOURCE=[{"name": "Nguyễn Thị Thanh Tâm", "title": "Bí thư Đảng uỷ, Chủ tịch HĐND xã", "rank": "01.002", "grade": 5, "coef": 5.76, "lastDate": "2026-01-01", "cycle": 36, "decision": "số 385-QĐ/TU", "decisionDate": "2025-12-19", "note": "Đã nâng năm 2026"}, {"name": "Phạm Văn Đức", "title": "Phó bí thư thường trực Đảng uỷ xã", "rank": "01.002", "grade": 3, "coef": 5.08, "lastDate": "2024-09-01", "cycle": 36, "decision": "", "decisionDate": "", "note": ""}, {"name": "Nguyễn Trọng Hải", "title": "UVTV, Trưởng Ban Xây dựng Đảng", "rank": "01.003", "grade": 9, "coef": 4.98, "lastDate": "2024-08-01", "cycle": 36, "decision": "", "decisionDate": "", "note": ""}, {"name": "Tô Văn Ngọc", "title": "ĐUV, Phó Trưởng Ban Xây dựng Đảng", "rank": "01.003", "grade": 4, "coef": 3.33, "lastDate": "2026-04-06", "cycle": 36, "decision": "số 238-QĐ/ĐU", "decisionDate": "2026-04-24", "note": "Đã nâng năm 2026"}, {"name": "Trần Thị Sinh", "title": "Chuyên viên", "rank": "01.003", "grade": 4, "coef": 3.33, "l
```
## salary
```text
rl('directives',this)"><span>📣</span>Văn bản chỉ đạo</button>
  <button class="tt-left-item" data-perm="weeklyReport" onclick="showCenterPage('sheet',this)"><span>🧾</span>Báo cáo tuần</button>
  <button class="tt-left-item" data-perm="monthlyReport" onclick="showCenterPage('monthreport',this)"><span>📅</span>Báo cáo tháng</button>
  <button class="tt-left-item" data-perm="meeting" onclick="openLeftCtrl('meeting',this)"><span>📝</span>Kết luận họp</button>
  <button class="tt-left-item" data-perm="salary" onclick="openLeftCtrl('salary',this)"><span>💰</span>Nâng lương</button>

  <div class="tt-left-sep">AI & NGHIỆP VỤ</div>
  <button class="tt-left-item" data-perm="ai" data-page="ai" onclick="showCenterPage('ai',this)"><span>🤖</span>AI theo lĩnh vực</button>
  <button class="tt-left-item" data-perm="lookup" data-page="library" onclick="showCenterPage('library',this)"><span>🔎</span>Tra cứu văn bản</button>

  <div class="tt-left-lotus">❀</div>
</div>
<div class="tt-mobile-menu no-print">
  <button onclick="toggleLeftMenu()">☰ MENU</button>
  <b id="ttMobileTitle">Theo dõi công việc</b>
</div>

<div class="notice">
  <div class="notice-icon">📣</div>
  <div><strong>Bản chính thức – Kho dữ liệu trực tuyến:</strong> Mỗi công việc được đặt cùng <strong>câu lệnh AI + biểu mẫu + tài liệu tham khảo</strong>. Kho nghiệp vụ số đã được kết nối lưu trữ trực tuyến để cán bộ có thể tải lên, xem và tải xuống tài liệu dùng chung.</div>
</div>



<div id="ttaiHome" class="ttai-home">
  <div class="ttai
```
```text
/span>Văn bản chỉ đạo</button>
  <button class="tt-left-item" data-perm="weeklyReport" onclick="showCenterPage('sheet',this)"><span>🧾</span>Báo cáo tuần</button>
  <button class="tt-left-item" data-perm="monthlyReport" onclick="showCenterPage('monthreport',this)"><span>📅</span>Báo cáo tháng</button>
  <button class="tt-left-item" data-perm="meeting" onclick="openLeftCtrl('meeting',this)"><span>📝</span>Kết luận họp</button>
  <button class="tt-left-item" data-perm="salary" onclick="openLeftCtrl('salary',this)"><span>💰</span>Nâng lương</button>

  <div class="tt-left-sep">AI & NGHIỆP VỤ</div>
  <button class="tt-left-item" data-perm="ai" data-page="ai" onclick="showCenterPage('ai',this)"><span>🤖</span>AI theo lĩnh vực</button>
  <button class="tt-left-item" data-perm="lookup" data-page="library" onclick="showCenterPage('library',this)"><span>🔎</span>Tra cứu văn bản</button>

  <div class="tt-left-lotus">❀</div>
</div>
<div class="tt-mobile-menu no-print">
  <button onclick="toggleLeftMenu()">☰ MENU</button>
  <b id="ttMobileTitle">Theo dõi công việc</b>
</div>

<div class="notice">
  <div class="notice-icon">📣</div>
  <div><strong>Bản chính thức – Kho dữ liệu trực tuyến:</strong> Mỗi công việc được đặt cùng <strong>câu lệnh AI + biểu mẫu + tài liệu tham khảo</strong>. Kho nghiệp vụ số đã được kết nối lưu trữ trực tuyến để cán bộ có thể tải lên, xem và tải xuống tài liệu dùng chung.</div>
</div>



<div id="ttaiHome" class="ttai-home">
  <div class="ttai-nav">
    <button onclick="goT
```
```text
hảo</strong>. Kho nghiệp vụ số đã được kết nối lưu trữ trực tuyến để cán bộ có thể tải lên, xem và tải xuống tài liệu dùng chung.</div>
</div>



<div id="ttaiHome" class="ttai-home">
  <div class="ttai-nav">
    <button onclick="goTT('overview')">🏠 Tổng quan</button>
    <button onclick="goTT('staff')">👥 Danh sách cán bộ</button>
    <button onclick="openCtrl('work')">📊 Công việc & văn bản</button>
    <button onclick="openCtrl('meeting')">📝 Kết luận họp</button>
    <button onclick="openCtrl('salary')">💰 Nâng lương</button>
    <button onclick="openCtrl('directives')">📣 Văn bản chỉ đạo</button><button onclick="goTT('aiwork')">🤖 AI theo lĩnh vực</button>
    <button onclick="goTT('libraryTop')">🔎 Tra cứu văn bản</button>
  </div>

  <section id="overview" class="tt-section">
    <div class="tt-section-head">
      <div><div class="tt-kicker">TRUNG TÂM AI – BAN XÂY DỰNG ĐẢNG</div><h2>TỔNG QUAN CÔNG VIỆC</h2>
      <p>Theo dõi tình hình thực hiện nhiệm vụ của Ban tại thời điểm mở Trung tâm.</p></div>
      <div id="ttNow" class="tt-now"></div>
    </div>
    <div class="tt-kpis">
      <div class="tt-kpi"><span>👥</span><div><b>Cán bộ Ban</b><strong id="ttStaffCount">0</strong></div></div>
      <div class="tt-kpi"><span>📌</span><div><b>Tổng nhiệm vụ</b><strong id="ttTaskCount">0</strong></div></div>
      <div class="tt-kpi"><span>⏳</span><div><b>Đang thực hiện</b><strong id="ttDoingCount">0</strong></div></div>
      <div class="tt-kpi warning"><span>⚠</span><div><b>Sắp đến hạn</b>
```
```text
    <div class="tt-function" onclick="openCtrl('meeting')"><div class="tt-icon">📝</div><b>Kết luận họp Ban</b><p>Tạo dự thảo kết luận, gắn nhiệm vụ, người thực hiện, kết quả/sản phẩm và thời hạn.</p><span>Tạo Kết luận →</span></div>
      <div class="tt-function" onclick="openCtrl('directives')"><div class="tt-icon">📣</div><b>Văn bản chỉ đạo</b><p>Lưu, tra cứu và thống kê văn bản chỉ đạo theo tuần, tháng, năm.</p><span>Mở Văn bản chỉ đạo →</span></div><div class="tt-function" onclick="openCtrl('salary')"><div class="tt-icon">💰</div><b>Theo dõi nâng lương</b><p>Theo dõi 36 CBCC khối Đảng, ngày đến hạn, đếm ngược và cập nhật quyết định đã nâng.</p><span>Mở theo dõi →</span></div>
    </div>
  </section>
</div>


<section id="sheetPage" class="tt-section" style="display:none">
  <div class="tt-section-head compact">
    <div><div class="tt-kicker">BÁO CÁO DÙNG CHUNG</div><h2>BIỂU BÁO CÁO GOOGLE SHEET</h2>
    <p>Cán bộ nhập trực tiếp trên biểu Google Sheet ngay trong Trung tâm AI, không cần mở thêm tab riêng.</p></div>
  </div>
  <div class="sheet-toolbar">
    <div>
      <b>Biểu báo cáo tuần của Ban Xây dựng Đảng</b>
      <span>Dữ liệu vẫn lưu trên Google Sheet gốc.</span>
    </div>
    <div class="sheet-actions">
      <button class="btn light" onclick="reloadEmbeddedSheet()">↻ Tải lại</button>
      <button class="btn light" onclick="openOriginalSheet()">↗ Mở toàn màn hình</button>
    </div>
  </div>
  <div class="sheet-note">Nếu Google yêu cầu đăng nhập, cán bộ đăng nhập tài k
```
```text
Ctrl()">Đóng ✕</button></div>
 <div class="ctrl-tabs">
  <button class="ctrl-tab" data-c="meeting" onclick="switchCtrl('meeting')">📝 Kết luận họp</button>
  <button class="ctrl-tab" data-c="aiassign" onclick="switchCtrl('aiassign')">📥🤖 AI giao việc</button>
  <button class="ctrl-tab" data-c="work" onclick="switchCtrl('work')">📊 Công việc & văn bản</button>
  <button class="ctrl-tab" data-c="directives" onclick="switchCtrl('directives')">📣 Văn bản chỉ đạo</button><button class="ctrl-tab" data-c="salary" onclick="switchCtrl('salary')">💰 Nâng lương</button>
 </div>

 <div id="c-meeting" class="ctrl-pane">
  <div class="ctrl-note"><b>Nguyên tắc:</b> hệ thống chỉ sắp xếp nội dung đã nhập, không tự tạo số liệu, căn cứ, tên người hoặc mốc thời gian. Chỗ thiếu được đánh dấu [CẦN BỔ SUNG].</div>
  <div class="ctrl-form">
   <div><label>Ngày họp</label><input id="mhDate" type="date"></div><div><label>Địa điểm</label><input id="mhPlace"></div><div><label>Chủ trì</label><select id="mhChair"></select></div><div><label>Thư ký</label><select id="mhSec"></select></div>
   <div class="span2"><label>Thành phần dự họp</label><textarea id="mhAttend">Các thành viên trong Ban Xây dựng Đảng</textarea></div><div class="span2"><label>Nội dung/chương trình họp</label><textarea id="mhAgenda"></textarea></div>
   <div class="full"><label>Ý kiến thảo luận, nội dung đã thống nhất</label><textarea id="mhDiscuss"></textarea></div>
   <div class="full"><label>Kết luận chung của Trưởng Ban/chủ trì</label><textarea 
```
```text

 <div class="ctrl-tabs">
  <button class="ctrl-tab" data-c="meeting" onclick="switchCtrl('meeting')">📝 Kết luận họp</button>
  <button class="ctrl-tab" data-c="aiassign" onclick="switchCtrl('aiassign')">📥🤖 AI giao việc</button>
  <button class="ctrl-tab" data-c="work" onclick="switchCtrl('work')">📊 Công việc & văn bản</button>
  <button class="ctrl-tab" data-c="directives" onclick="switchCtrl('directives')">📣 Văn bản chỉ đạo</button><button class="ctrl-tab" data-c="salary" onclick="switchCtrl('salary')">💰 Nâng lương</button>
 </div>

 <div id="c-meeting" class="ctrl-pane">
  <div class="ctrl-note"><b>Nguyên tắc:</b> hệ thống chỉ sắp xếp nội dung đã nhập, không tự tạo số liệu, căn cứ, tên người hoặc mốc thời gian. Chỗ thiếu được đánh dấu [CẦN BỔ SUNG].</div>
  <div class="ctrl-form">
   <div><label>Ngày họp</label><input id="mhDate" type="date"></div><div><label>Địa điểm</label><input id="mhPlace"></div><div><label>Chủ trì</label><select id="mhChair"></select></div><div><label>Thư ký</label><select id="mhSec"></select></div>
   <div class="span2"><label>Thành phần dự họp</label><textarea id="mhAttend">Các thành viên trong Ban Xây dựng Đảng</textarea></div><div class="span2"><label>Nội dung/chương trình họp</label><textarea id="mhAgenda"></textarea></div>
   <div class="full"><label>Ý kiến thảo luận, nội dung đã thống nhất</label><textarea id="mhDiscuss"></textarea></div>
   <div class="full"><label>Kết luận chung của Trưởng Ban/chủ trì</label><textarea id="mhGeneral"></textarea></d
```
```text
><button class="btn light" onclick="buildDirectiveSummary()">↻ Cập nhật danh sách</button><button class="btn light" onclick="copyDirectiveSummary()">📋 Sao chép báo cáo</button><button class="btn primary" onclick="sendSummaryToAIReview()">🤖 Phân tích nhiệm vụ</button></div>
 </div>
 <div id="vdSummaryStatus" class="ctrl-note">Danh sách văn bản được tổng hợp tự động theo lĩnh vực.</div>
 <div id="vdSummaryBox"></div>
</div>
<div id="vdGrouped" style="display:none!important"></div></div><div id="c-salary" class="ctrl-pane">
  <div class="ctrl-kpis"><div class="ctrl-kpi"><b>Tổng CBCC</b><strong id="slTotal">36</strong></div><div class="ctrl-kpi"><b>Quá hạn</b><strong id="slLate">0</strong></div><div class="ctrl-kpi"><b>≤30 ngày</b><strong id="sl30">0</strong></div><div class="ctrl-kpi"><b>31–90 ngày</b><strong id="sl90">0</strong></div><div class="ctrl-kpi"><b>Đã có QĐ/Ghi chú nâng</b><strong id="slRaised">0</strong></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><o
```
```text
QĐ/Ghi chú nâng</b><strong id="slRaised">0</strong></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5
```
```text
g></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5d7cd;padding-top:16px">
    <div id="whCurrent" c
```
```text
rSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5d7cd;padding-top:16px">
    <div id="whCurrent" class="wh-current">Chọn một nhóm nghiệp vụ ở phía trên.</div>
    <div class="wh-toolbar">
      <button class="btn primary" onclick="chooseUploadFiles()">＋ Tải tài liệu lên</button>
      <button class="btn light" onclick="loadWarehouseFiles()">↻ Làm mới danh sách</button>
      <input id="whSearch" class="wh-search" placeholder="Tìm theo tên file..." oninput="renderWarehouseFiles()">
      <input id="hiddenUploader" type="file" multiple style="display:none">
    </div>
    <div id="warehouseIn
```
```text
NH", "title": "ĐUV, Phó trưởng ban Xây dựng Đảng", "area": "Phụ trách công tác Đảng, đảng viên"}, {"name": "TRƯƠNG HỮU LUYỆN", "title": "ĐUV, Phó trưởng ban Xây dựng Đảng", "area": "Phụ trách công tác Tuyên giáo"}];

const APP_PERMISSION_DEFS=[
 ['overview','Tổng quan'],['staff','Danh sách cán bộ'],['staffWork','Theo dõi công việc'],
 ['work','Công việc & văn bản'],['directives','Văn bản chỉ đạo'],['weeklyReport','Báo cáo tuần'],
 ['monthlyReport','Báo cáo tháng'],['meeting','Kết luận họp'],
 ['salary','Nâng lương'],['ai','AI theo lĩnh vực'],['lookup','Tra cứu văn bản']
];
const APP_DEFAULT_PERMS=Object.fromEntries(APP_PERMISSION_DEFS.map(x=>[x[0],true]));

const BAN_QUICK_ACCOUNTS=[
 {name:'NGUYỄN TRỌNG HẢI',username:'trolyAI_nguyentronghai'},
 {name:'TÔ VĂN NGỌC',username:'trolyAI_tovanngoc'},
 {name:'TRẦN THỊ SINH',username:'trolyAI_tranthisinh'},
 {name:'ĐÀO THỊ THANH VÂN',username:'trolyAI_daothithanhvan'},
 {name:'NGUYỄN BÁ MẠNH',username:'trolyAI_nguyenbamanh'},
 {name:'NGÔ THANH NGÀ',username:'trolyAI_ngothanhnga'},
 {name:'NGUYỄN THỊ VÂN ANH',username:'trolyAI_nguyenthivananh'},
 {name:'TRƯƠNG HỮU LUYỆN',username:'trolyAI_truonghuuluyen'}
];

function lockSetMsg(msg,type=''){
 const e=document.getElementById('lockMsg');if(e){e.className='app-lock-msg'+(type?' '+type:'');e.textContent=msg}
}
function lockVisual(){
 document.body.classList.add('app-locked');
 document.getElementById('appLockScreen')?.classList.remove('unlocked');
}
function unlockVisual(){
 document.body.cla
```
```text
tối thiểu 6 ký tự):');if(!pw)return;try{await adminUserApi({action:'password',user_id:uid,password:pw});setAdminMsg('Đã đổi mật khẩu.','ok')}catch(e){setAdminMsg(e.message,'err')}}
async function toggleAppUser(uid,state){if(!confirm(state?'Mở lại tài khoản này?':'Khóa tài khoản này?'))return;try{await adminUserApi({action:'status',user_id:uid,is_active:state});setAdminMsg(state?'Đã mở tài khoản.':'Đã khóa tài khoản.','ok');await loadAppUsersAdmin()}catch(e){setAdminMsg(e.message,'err')}}

const SALARY_SOURCE=[{"name": "Nguyễn Thị Thanh Tâm", "title": "Bí thư Đảng uỷ, Chủ tịch HĐND xã", "rank": "01.002", "grade": 5, "coef": 5.76, "lastDate": "2026-01-01", "cycle": 36, "decision": "số 385-QĐ/TU", "decisionDate": "2025-12-19", "note": "Đã nâng năm 2026"}, {"name": "Phạm Văn Đức", "title": "Phó bí thư thường trực Đảng uỷ xã", "rank": "01.002", "grade": 3, "coef": 5.08, "lastDate": "2024-09-01", "cycle": 36, "decision": "", "decisionDate": "", "note": ""}, {"name": "Nguyễn Trọng Hải", "title": "UVTV, Trưởng Ban Xây dựng Đảng", "rank": "01.003", "grade": 9, "coef": 4.98, "lastDate": "2024-08-01", "cycle": 36, "decision": "", "decisionDate": "", "note": ""}, {"name": "Tô Văn Ngọc", "title": "ĐUV, Phó Trưởng Ban Xây dựng Đảng", "rank": "01.003", "grade": 4, "coef": 3.33, "lastDate": "2026-04-06", "cycle": 36, "decision": "số 238-QĐ/ĐU", "decisionDate": "2026-04-24", "note": "Đã nâng năm 2026"}, {"name": "Trần Thị Sinh", "title": "Chuyên viên", "rank": "01.003", "grade": 4, "coef": 3.33, "l
```
## localStorage
```text
 lockVisual(){
 document.body.classList.add('app-locked');
 document.getElementById('appLockScreen')?.classList.remove('unlocked');
}
function unlockVisual(){
 document.body.classList.remove('app-locked');
 document.getElementById('appLockScreen')?.classList.add('unlocked');
}

const LOCAL_AUTH_KEY='thu_lam_local_auth_v1';
const INITIAL_PASSWORD_SHA256='8d969eef6ecad3c29a3a629280e686cff8cae7a36a7a8193aaf1c4d3e8e1d5a'; // SHA-256 of initial password
function localAuthData(){try{return JSON.parse(localStorage.getItem(LOCAL_AUTH_KEY)||'{}')}catch(_){return {}}}
function saveLocalAuthData(x){localStorage.setItem(LOCAL_AUTH_KEY,JSON.stringify(x))}
async function sha256hex(text){
 const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(text));
 return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('');
}
function localAccount(username){
 const u=String(username||'').toLowerCase();
 return BAN_QUICK_ACCOUNTS.find(x=>x.username.toLowerCase()===u)||null;
}
async function tryLocalLogin(username,password){
 const acc=localAccount(username);if(!acc)return false;
 const data=localAuthData(), saved=data[acc.username.toLowerCase()];
 const hash=await sha256hex(password);
 const expected=saved?.passwordHash||INITIAL_PASSWORD_SHA256;
 if(saved?.locked===true||hash!==expected)return false;
 const st=STAFF.find(x=>x.name===acc.name);
 currentAppUser={id:'local:'+acc.username,email:acc.username+'@thulam.local'};
 currentAppProfile={user_id:currentAppUser.id,staff_name:acc.n
```
```text
een')?.classList.remove('unlocked');
}
function unlockVisual(){
 document.body.classList.remove('app-locked');
 document.getElementById('appLockScreen')?.classList.add('unlocked');
}

const LOCAL_AUTH_KEY='thu_lam_local_auth_v1';
const INITIAL_PASSWORD_SHA256='8d969eef6ecad3c29a3a629280e686cff8cae7a36a7a8193aaf1c4d3e8e1d5a'; // SHA-256 of initial password
function localAuthData(){try{return JSON.parse(localStorage.getItem(LOCAL_AUTH_KEY)||'{}')}catch(_){return {}}}
function saveLocalAuthData(x){localStorage.setItem(LOCAL_AUTH_KEY,JSON.stringify(x))}
async function sha256hex(text){
 const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(text));
 return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('');
}
function localAccount(username){
 const u=String(username||'').toLowerCase();
 return BAN_QUICK_ACCOUNTS.find(x=>x.username.toLowerCase()===u)||null;
}
async function tryLocalLogin(username,password){
 const acc=localAccount(username);if(!acc)return false;
 const data=localAuthData(), saved=data[acc.username.toLowerCase()];
 const hash=await sha256hex(password);
 const expected=saved?.passwordHash||INITIAL_PASSWORD_SHA256;
 if(saved?.locked===true||hash!==expected)return false;
 const st=STAFF.find(x=>x.name===acc.name);
 currentAppUser={id:'local:'+acc.username,email:acc.username+'@thulam.local'};
 currentAppProfile={user_id:currentAppUser.id,staff_name:acc.name,username:acc.username,title:st?.title||'',area:st?.area||'',is_active:true};
 currentAppPer
```
```text
 cấp, phân quyền", "2.5. Công tác phối hợp với MTTQ và các đoàn thể", "3. Công tác lãnh đạo MTTQ và các tổ chức chính trị - xã hội", "IV. ĐÁNH GIÁ CHUNG", "1. Kết quả công tác lãnh đạo, chỉ đạo", "2. Kết quả nổi bật, điểm mới, mô hình mới, cách làm sáng tạo, hiệu quả", "3. Hạn chế, tồn tại, nguyên nhân", "4. Vấn đề mới phát sinh, vấn đề phức tạp", "V. NHIỆM VỤ TRỌNG TÂM KỲ TIẾP THEO", "VI. NHỮNG VƯỚNG MẮC, KHÓ KHĂN VÀ KIẾN NGHỊ, ĐỀ XUẤT"];
const CTRLKEY='thu_lam_control_v2';
let CTRL=JSON.parse(localStorage.getItem(CTRLKEY)||'null')||{work:[],reports:[],meetingTasks:[],salary:SALARY_SOURCE};
if(!CTRL.salary||CTRL.salary.length<30) CTRL.salary=SALARY_SOURCE;
function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }
function ce(x){return String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function openCtrl(p){ctrlModal.style.display='block';switchCtrl(p)} function closeCtrl(){ctrlModal.style.display='none'}
function switchCtrl(p){document.querySelectorAll('.ctrl-pane').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.ctrl-tab').forEach(x=>x.classList.toggle('active',x.dataset.c===p));document.getElementById('c-'+p)?.classList.add('active');renderCtrlAll()}
function initCtrl
```
```text
đạo", "2. Kết quả nổi bật, điểm mới, mô hình mới, cách làm sáng tạo, hiệu quả", "3. Hạn chế, tồn tại, nguyên nhân", "4. Vấn đề mới phát sinh, vấn đề phức tạp", "V. NHIỆM VỤ TRỌNG TÂM KỲ TIẾP THEO", "VI. NHỮNG VƯỚNG MẮC, KHÓ KHĂN VÀ KIẾN NGHỊ, ĐỀ XUẤT"];
const CTRLKEY='thu_lam_control_v2';
let CTRL=JSON.parse(localStorage.getItem(CTRLKEY)||'null')||{work:[],reports:[],meetingTasks:[],salary:SALARY_SOURCE};
if(!CTRL.salary||CTRL.salary.length<30) CTRL.salary=SALARY_SOURCE;
function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }
function ce(x){return String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function openCtrl(p){ctrlModal.style.display='block';switchCtrl(p)} function closeCtrl(){ctrlModal.style.display='none'}
function switchCtrl(p){document.querySelectorAll('.ctrl-pane').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.ctrl-tab').forEach(x=>x.classList.toggle('active',x.dataset.c===p));document.getElementById('c-'+p)?.classList.add('active');renderCtrlAll()}
function initCtrlSelects(){
 const opts='<option value="">-- Chọn --</option>'+STAFF.map((x,i)=>`<option value="${i}">${ce(x.name)}</option>`).join('');
 wOwner.innerHTML=opts;rpPerson.innerHTML=opts;wfPerso
```
```text
async function enableWorkNotify(){if(!('Notification'in window))return alert('Trình duyệt không hỗ trợ thông báo.');let p=await Notification.requestPermission();if(p==='granted')new Notification('Trung tâm AI - Ban Xây dựng Đảng',{body:'Đã bật nhắc việc. Khi mở Trung tâm mỗi ngày, hệ thống sẽ cảnh báo nhiệm vụ đến hạn/quá hạn.'})}
function dailyWorkNotify(){if(!('Notification'in window)||Notification.permission!=='granted')return;let key='tl_work_notify_'+new Date().toISOString().slice(0,10);if(localStorage.getItem(key))return;let a=CTRL.work.filter(x=>x.status!=='Đã hoàn thành'&&dleft(x.due)<=1);if(a.length){new Notification('Nhắc việc Ban Xây dựng Đảng',{body:`Có ${a.length} nhiệm vụ đến hạn hoặc quá hạn cần kiểm tra.`});localStorage.setItem(key,'1')}}
function exportWorkCSV(){let h=['Người thực hiện','Lĩnh vực','Loại','Văn bản/Nhiệm vụ','Kết quả/Sản phẩm','Ngày giao','Thời hạn','Trạng thái','Tiến độ','Số VB ban hành','Ngày ban hành','Kết quả thực tế'];let rows=CTRL.work.map(x=>[x.owner,x.area,x.type,x.task,x.product,x.start,x.due,x.status,x.progress,x.outNo,x.outDate,x.result]);let csv='\ufeff'+[h,...rows].map(r=>r.map(v=>'"'+String(v??'').replaceAll('"','""')+'"').join(',')).join('\n');let b=new Blob([csv],{type:'text/csv;charset=utf-8'}),a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Thong_ke_cong_viec_van_ban.csv';a.click()}
function saveReportItem(){if(!rpPeriod.value.trim()||rpPerson.value===''||!rpContent.value.trim())return alert('Nhập kỳ báo cáo, người
```
```text
dy:'Đã bật nhắc việc. Khi mở Trung tâm mỗi ngày, hệ thống sẽ cảnh báo nhiệm vụ đến hạn/quá hạn.'})}
function dailyWorkNotify(){if(!('Notification'in window)||Notification.permission!=='granted')return;let key='tl_work_notify_'+new Date().toISOString().slice(0,10);if(localStorage.getItem(key))return;let a=CTRL.work.filter(x=>x.status!=='Đã hoàn thành'&&dleft(x.due)<=1);if(a.length){new Notification('Nhắc việc Ban Xây dựng Đảng',{body:`Có ${a.length} nhiệm vụ đến hạn hoặc quá hạn cần kiểm tra.`});localStorage.setItem(key,'1')}}
function exportWorkCSV(){let h=['Người thực hiện','Lĩnh vực','Loại','Văn bản/Nhiệm vụ','Kết quả/Sản phẩm','Ngày giao','Thời hạn','Trạng thái','Tiến độ','Số VB ban hành','Ngày ban hành','Kết quả thực tế'];let rows=CTRL.work.map(x=>[x.owner,x.area,x.type,x.task,x.product,x.start,x.due,x.status,x.progress,x.outNo,x.outDate,x.result]);let csv='\ufeff'+[h,...rows].map(r=>r.map(v=>'"'+String(v??'').replaceAll('"','""')+'"').join(',')).join('\n');let b=new Blob([csv],{type:'text/csv;charset=utf-8'}),a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Thong_ke_cong_viec_van_ban.csv';a.click()}
function saveReportItem(){if(!rpPeriod.value.trim()||rpPerson.value===''||!rpContent.value.trim())return alert('Nhập kỳ báo cáo, người nhập và nội dung.');let st=STAFF[+rpPerson.value];CTRL.reports.push({id:Date.now(),type:rpType.value,period:rpPeriod.value.trim(),person:st.name,area:rpArea.value,section:rpSection.value,content:rpContent.value.trim(),issue:rpIssue.
```
```text
late+' nhiệm vụ quá hạn':'✓ Không có nhiệm vụ quá hạn'}</div>
    </div>`
  }).join('')
}
window.addEventListener('load',()=>{renderStaffWorkCards();setInterval(renderStaffWorkCards,30000)})


function isThuLamAdmin(){
 try{
  if(currentAppProfile&&String(currentAppProfile.staff_name||'').trim().toUpperCase()==='TRẦN THỊ SINH' && !currentAppProfile.auth_user_id) return true;
  const vals=[window.currentAppUsername,currentAppProfile?.username,currentAppProfile?.user_name,currentAppProfile?.login,localStorage.getItem('thu_lam_current_username'),localStorage.getItem('thu_lam_username')].filter(Boolean).map(x=>String(x).trim().toLowerCase());
  if(vals.includes('trolyai_tranthisinh')) return true;
 }catch(e){}
 return (typeof isAdmin!=='undefined'&&!!isAdmin);
}
let STAFF_REGISTRY=[];
function applyStaffRegistry(rows){
  STAFF_REGISTRY=(rows||[]).map(x=>({id:Number(x.id)||0,name:String(x.name||'').trim(),title:String(x.title||''),area:String(x.area||''),is_active:x.is_active!==false,sort_order:Number(x.sort_order)||0}));
  const active=STAFF_REGISTRY.filter(x=>x.is_active).sort((a,b)=>(a.sort_order-b.sort_order)||a.name.localeCompare(b.name,'vi'));
  const mapped=active.map(x=>({id:x.id,name:x.name,title:x.title,area:x.area}));
  STAFF.splice(0,STAFF.length,...mapped);TT_STAFF.splice(0,TT_STAFF.length,...mapped);TT_STAFF_WORK.splice(0,TT_STAFF_WORK.length,...mapped);
  try{initCtrlSelects()}catch(e){} try{renderTTStaff();renderTTOverview();renderStaffWorkCards();renderWork()}catch(e){} try{p
```
```text
 hạn'}</div>
    </div>`
  }).join('')
}
window.addEventListener('load',()=>{renderStaffWorkCards();setInterval(renderStaffWorkCards,30000)})


function isThuLamAdmin(){
 try{
  if(currentAppProfile&&String(currentAppProfile.staff_name||'').trim().toUpperCase()==='TRẦN THỊ SINH' && !currentAppProfile.auth_user_id) return true;
  const vals=[window.currentAppUsername,currentAppProfile?.username,currentAppProfile?.user_name,currentAppProfile?.login,localStorage.getItem('thu_lam_current_username'),localStorage.getItem('thu_lam_username')].filter(Boolean).map(x=>String(x).trim().toLowerCase());
  if(vals.includes('trolyai_tranthisinh')) return true;
 }catch(e){}
 return (typeof isAdmin!=='undefined'&&!!isAdmin);
}
let STAFF_REGISTRY=[];
function applyStaffRegistry(rows){
  STAFF_REGISTRY=(rows||[]).map(x=>({id:Number(x.id)||0,name:String(x.name||'').trim(),title:String(x.title||''),area:String(x.area||''),is_active:x.is_active!==false,sort_order:Number(x.sort_order)||0}));
  const active=STAFF_REGISTRY.filter(x=>x.is_active).sort((a,b)=>(a.sort_order-b.sort_order)||a.name.localeCompare(b.name,'vi'));
  const mapped=active.map(x=>({id:x.id,name:x.name,title:x.title,area:x.area}));
  STAFF.splice(0,STAFF.length,...mapped);TT_STAFF.splice(0,TT_STAFF.length,...mapped);TT_STAFF_WORK.splice(0,TT_STAFF_WORK.length,...mapped);
  try{initCtrlSelects()}catch(e){} try{renderTTStaff();renderTTOverview();renderStaffWorkCards();renderWork()}catch(e){} try{populateNewUserStaff()}catch(e){}
}
async function
```
```text
dFile?.files?.[0];
 let saveDate=vdDate.value||new Date().toISOString().slice(0,10);
 let id=Date.now();
 CTRL.directives.push({
   id,no:vdNo.value.trim(),date:saveDate,issuer:vdIssuer.value.trim(),
   area:vdArea.value,title:vdTitle.value.trim(),file:f?f.name:'',
   fileType:f?f.type:'',note:vdNote.value.trim()
 });
 if(f){
   try{ await saveDirectiveFileBlob(id,f); }
   catch(e){ console.error(e); alert('Đã lưu thông tin văn bản nhưng chưa lưu được tệp đính kèm trên trình duyệt này.'); }
 }
 localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
 vdPeriod.value='all'; vdAreaFilter.value=''; vdSearch.value='';
 renderDirectives();
 if(typeof buildDirectiveSummary==='function')buildDirectiveSummary();
 if(typeof renderTTOverview==='function')renderTTOverview();
 alert('Đã lưu văn bản chỉ đạo.');
 vdNo.value='';vdDate.value='';vdIssuer.value='';vdArea.value='';vdTitle.value='';vdNote.value='';
 if(vdFile)vdFile.value='';
}
async function delDirective(id){
 ensureDirectives();
 CTRL.directives=CTRL.directives.filter(x=>x.id!==id);
 localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
 try{await deleteDirectiveFileBlob(id)}catch(e){}
 renderDirectives();
}
function dirPeriodOK(x,m){if(m==='all')return true;if(!x.date)return false;let d=new Date(x.date+'T00:00:00'),n=new Date();if(m==='year')return d.getFullYear()===n.getFullYear();if(m==='month')return d.getFullYear()===n.getFullYear()&&d.getMonth()===n.getMonth();return dateInISOWeek(x.date,isoWeekValue(n))}
function renderDirectives(){
 if(!
```
```text
CTRL));
 vdPeriod.value='all'; vdAreaFilter.value=''; vdSearch.value='';
 renderDirectives();
 if(typeof buildDirectiveSummary==='function')buildDirectiveSummary();
 if(typeof renderTTOverview==='function')renderTTOverview();
 alert('Đã lưu văn bản chỉ đạo.');
 vdNo.value='';vdDate.value='';vdIssuer.value='';vdArea.value='';vdTitle.value='';vdNote.value='';
 if(vdFile)vdFile.value='';
}
async function delDirective(id){
 ensureDirectives();
 CTRL.directives=CTRL.directives.filter(x=>x.id!==id);
 localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
 try{await deleteDirectiveFileBlob(id)}catch(e){}
 renderDirectives();
}
function dirPeriodOK(x,m){if(m==='all')return true;if(!x.date)return false;let d=new Date(x.date+'T00:00:00'),n=new Date();if(m==='year')return d.getFullYear()===n.getFullYear();if(m==='month')return d.getFullYear()===n.getFullYear()&&d.getMonth()===n.getMonth();return dateInISOWeek(x.date,isoWeekValue(n))}
function renderDirectives(){
 if(!window.vdGrouped)return;ensureDirectives();
 let q=(vdSearch.value||'').toLowerCase(),m=vdPeriod.value,af=vdAreaFilter.value;
 let a=CTRL.directives.filter(x=>dirPeriodOK(x,m)&&(!af||x.area===af)&&(!q||[x.no,x.issuer,x.area,x.title,x.note].join(' ').toLowerCase().includes(q)));
 vdStats.textContent=`Đang hiển thị ${a.length}/${CTRL.directives.length} văn bản đã lưu.`;
 if(!a.length){vdGrouped.innerHTML='<div class="ctrl-note">Chưa có văn bản phù hợp.</div>';return}
 let groups={};
 a.forEach(x=>{let k=x.area||'Chưa phân lĩnh vực';(groups[
```
## openMonthlySheet
```text
gle Sheet gốc hoặc ngay trong Trung tâm AI đều dùng chung một nguồn dữ liệu.</p>
    </div>
  </div>

  <div class="sheet-toolbar">
    <div>
      <b>Biểu báo cáo tháng của Ban Xây dựng Đảng</b>
      <span>Đồng bộ trực tiếp với Google Sheet: mọi thay đổi trên link gốc sẽ hiển thị tại đây khi Sheet cập nhật/tải lại.</span>
    </div>
    <div class="sheet-actions">
      <button class="btn light" onclick="reloadMonthlySheet()">↻ Đồng bộ/Tải lại</button>
      <button class="btn light" onclick="openMonthlySheet()">↗ Mở Google Sheet</button>
    </div>
  </div>

  <div class="sheet-note">
    <b>Nguyên tắc:</b> Trung tâm AI không tạo bản sao dữ liệu. Khung dưới đây mở trực tiếp đúng Google Sheet gốc,
    vì vậy cán bộ nhập trên link Google Sheet hoặc nhập trong Trung tâm AI đều là cùng một dữ liệu.
  </div>

  <div class="month-live-status">
    <span class="live-dot"></span>
    <b>Dữ liệu dùng chung</b>
    <span id="monthSyncTime">Chưa tải</span>
  </div>

  <div class="sheet-frame-wrap month-sheet-frame">
    <iframe id="monthReportSheetFrame" src="https://docs.google.com/spreadsheets/d/1CgV_SPeUXB6xpxg7RpONY9gkV0Ztpuw_/edit?gid=1002803415&rm=minimal#gid=1002803415" allow="clipboard-read; clipboard-write"></iframe>
  </div>
</section>



<div id="aiwork" class="tt-section tt-ai-section"><div class="tt-ai-big" onclick="toggleAISection()"><div><div class="tt-kicker">ỨNG DỤNG AI THEO LĨNH VỰC</div><h2>🤖 TRỢ LÝ AI NGHIỆP VỤ</h2><p>Chọn lĩnh vực → chọn công việc → sử dụng câu lệnh AI chuẩn.</p
```
## reloadMonthlySheet
```text
</div>
      <h2>📅 BÁO CÁO THÁNG – ĐỒNG BỘ GOOGLE SHEET</h2>
      <p>Cán bộ nhập trên Google Sheet gốc hoặc ngay trong Trung tâm AI đều dùng chung một nguồn dữ liệu.</p>
    </div>
  </div>

  <div class="sheet-toolbar">
    <div>
      <b>Biểu báo cáo tháng của Ban Xây dựng Đảng</b>
      <span>Đồng bộ trực tiếp với Google Sheet: mọi thay đổi trên link gốc sẽ hiển thị tại đây khi Sheet cập nhật/tải lại.</span>
    </div>
    <div class="sheet-actions">
      <button class="btn light" onclick="reloadMonthlySheet()">↻ Đồng bộ/Tải lại</button>
      <button class="btn light" onclick="openMonthlySheet()">↗ Mở Google Sheet</button>
    </div>
  </div>

  <div class="sheet-note">
    <b>Nguyên tắc:</b> Trung tâm AI không tạo bản sao dữ liệu. Khung dưới đây mở trực tiếp đúng Google Sheet gốc,
    vì vậy cán bộ nhập trên link Google Sheet hoặc nhập trong Trung tâm AI đều là cùng một dữ liệu.
  </div>

  <div class="month-live-status">
    <span class="live-dot"></span>
    <b>Dữ liệu dùng chung</b>
    <span id="monthSyncTime">Chưa tải</span>
  </div>

  <div class="sheet-frame-wrap month-sheet-frame">
    <iframe id="monthReportSheetFrame" src="https://docs.google.com/spreadsheets/d/1CgV_SPeUXB6xpxg7RpONY9gkV0Ztpuw_/edit?gid=1002803415&rm=minimal#gid=1002803415" allow="clipboard-read; clipboard-write"></iframe>
  </div>
</section>



<div id="aiwork" class="tt-section tt-ai-section"><div class="tt-ai-big" onclick="toggleAISection()"><div><div class="tt-kicker">ỨNG DỤNG AI THEO LĨNH VỰC</div><h2>🤖 T
```
## vdPdfViewer
```text
application/pdf'||String(name).toLowerCase().endsWith('.pdf')){
     const url=URL.createObjectURL(rec.blob);openPdfViewer(url,name);return;
   }
   // Non-PDF cannot be reliably previewed in browser; offer download.
   if(confirm('Định dạng này không xem trực tiếp ổn định trong trình duyệt. Bạn có muốn tải tệp xuống để mở không?'))downloadDirectiveFile(id,name)
 }catch(e){console.error(e);alert('Không mở được tệp văn bản.')}
}
function openPdfViewer(url,name){
 let old=document.getElementById('vdPdfViewer');if(old)old.remove();
 const el=document.createElement('div');el.id='vdPdfViewer';el.className='vd-pdf-modal';
 el.innerHTML=`<div class="vd-pdf-box"><div class="vd-pdf-head"><b>📄 ${ce(name||'Văn bản PDF')}</b><button onclick="closePdfViewer()">Đóng ✕</button></div><iframe src="${url}#toolbar=1&navpanes=0"></iframe></div>`;
 el.dataset.url=url;document.body.appendChild(el)
}
function closePdfViewer(){
 const el=document.getElementById('vdPdfViewer');if(!el)return;
 const url=el.dataset.url;if(url)URL.revokeObjectURL(url);el.remove()
}

function ensureDirectives(){if(!Array.isArray(CTRL.directives))CTRL.directives=[]}
async function saveDirective(){
 ensureDirectives();
 if(!vdNo.value.trim()&&!vdTitle.value.trim())return alert('Nhập số/ký hiệu hoặc trích yếu văn bản.');
 let f=vdFile?.files?.[0];
 let saveDate=vdDate.value||new Date().toISOString().slice(0,10);
 let id=Date.now();
 CTRL.directives.push({
   id,no:vdNo.value.trim(),date:saveDate,issuer:vdIssuer.value.trim(),
   area:v
```
```text
.createObjectURL(rec.blob);openPdfViewer(url,name);return;
   }
   // Non-PDF cannot be reliably previewed in browser; offer download.
   if(confirm('Định dạng này không xem trực tiếp ổn định trong trình duyệt. Bạn có muốn tải tệp xuống để mở không?'))downloadDirectiveFile(id,name)
 }catch(e){console.error(e);alert('Không mở được tệp văn bản.')}
}
function openPdfViewer(url,name){
 let old=document.getElementById('vdPdfViewer');if(old)old.remove();
 const el=document.createElement('div');el.id='vdPdfViewer';el.className='vd-pdf-modal';
 el.innerHTML=`<div class="vd-pdf-box"><div class="vd-pdf-head"><b>📄 ${ce(name||'Văn bản PDF')}</b><button onclick="closePdfViewer()">Đóng ✕</button></div><iframe src="${url}#toolbar=1&navpanes=0"></iframe></div>`;
 el.dataset.url=url;document.body.appendChild(el)
}
function closePdfViewer(){
 const el=document.getElementById('vdPdfViewer');if(!el)return;
 const url=el.dataset.url;if(url)URL.revokeObjectURL(url);el.remove()
}

function ensureDirectives(){if(!Array.isArray(CTRL.directives))CTRL.directives=[]}
async function saveDirective(){
 ensureDirectives();
 if(!vdNo.value.trim()&&!vdTitle.value.trim())return alert('Nhập số/ký hiệu hoặc trích yếu văn bản.');
 let f=vdFile?.files?.[0];
 let saveDate=vdDate.value||new Date().toISOString().slice(0,10);
 let id=Date.now();
 CTRL.directives.push({
   id,no:vdNo.value.trim(),date:saveDate,issuer:vdIssuer.value.trim(),
   area:vdArea.value,title:vdTitle.value.trim(),file:f?f.name:'',
   fileType:f?f.type:'',n
```
```text
r(url,name){
 let old=document.getElementById('vdPdfViewer');if(old)old.remove();
 const el=document.createElement('div');el.id='vdPdfViewer';el.className='vd-pdf-modal';
 el.innerHTML=`<div class="vd-pdf-box"><div class="vd-pdf-head"><b>📄 ${ce(name||'Văn bản PDF')}</b><button onclick="closePdfViewer()">Đóng ✕</button></div><iframe src="${url}#toolbar=1&navpanes=0"></iframe></div>`;
 el.dataset.url=url;document.body.appendChild(el)
}
function closePdfViewer(){
 const el=document.getElementById('vdPdfViewer');if(!el)return;
 const url=el.dataset.url;if(url)URL.revokeObjectURL(url);el.remove()
}

function ensureDirectives(){if(!Array.isArray(CTRL.directives))CTRL.directives=[]}
async function saveDirective(){
 ensureDirectives();
 if(!vdNo.value.trim()&&!vdTitle.value.trim())return alert('Nhập số/ký hiệu hoặc trích yếu văn bản.');
 let f=vdFile?.files?.[0];
 let saveDate=vdDate.value||new Date().toISOString().slice(0,10);
 let id=Date.now();
 CTRL.directives.push({
   id,no:vdNo.value.trim(),date:saveDate,issuer:vdIssuer.value.trim(),
   area:vdArea.value,title:vdTitle.value.trim(),file:f?f.name:'',
   fileType:f?f.type:'',note:vdNote.value.trim()
 });
 if(f){
   try{ await saveDirectiveFileBlob(id,f); }
   catch(e){ console.error(e); alert('Đã lưu thông tin văn bản nhưng chưa lưu được tệp đính kèm trên trình duyệt này.'); }
 }
 localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
 vdPeriod.value='all'; vdAreaFilter.value=''; vdSearch.value='';
 renderDirectives();
 if(typeof buildDirectiv
```
```text
|'—'}</td><td>${dlEsc(d.date)||'—'}</td><td>${dlEsc(d.title)||'—'}</td><td>${dlEsc(d.actor)||'—'}</td><td>${dlActions(d)}</td></tr>`).join(''):'<tr><td colspan="8" class="dl-empty">Chưa có văn bản phù hợp.</td></tr>';
}

</script>
<script>

document.addEventListener('keydown',function(e){
 if(e.key!=='Escape')return;
 const ul=document.getElementById('userLoginModal');if(ul&&getComputedStyle(ul).display!=='none'){closeUserLogin();return;}
 e.preventDefault();
 const pdf=document.getElementById('vdPdfViewer');
 if(pdf && getComputedStyle(pdf).display!=='none'){ try{closePdfViewer()}catch(_){} return; }
 const admin=document.getElementById('adminModal');
 if(admin && getComputedStyle(admin).display!=='none'){ try{closeAdmin()}catch(_){} return; }
 const wh=document.getElementById('warehouseModal');
 if(wh && getComputedStyle(wh).display!=='none'){ try{closeWarehouse()}catch(_){} return; }
 const ctrl=document.getElementById('ctrlModal');
 if(ctrl && getComputedStyle(ctrl).display!=='none'){ try{closeCtrl()}catch(_){} return; }
});

</script>
<script>
document.addEventListener('DOMContentLoaded',async()=>{
 lockVisual();
 try{await sb.auth.signOut({scope:'local'})}catch(_){}
 const u=document.getElementById('lockUsername'),p=document.getElementById('lockPassword');
 if(u)u.addEventListener('keydown',e=>{if(e.key==='Enter')p?.focus()});
 if(p)p.addEventListener('keydown',e=>{if(e.key==='Enter')unlockApp()});
});
</script>
<script>
function togglePassword(inputId,btn){
 const input=document.
```
## CTRLKEY
```text
 UBND xã, phường", "2.4. Cải cách hành chính, phân cấp, phân quyền", "2.5. Công tác phối hợp với MTTQ và các đoàn thể", "3. Công tác lãnh đạo MTTQ và các tổ chức chính trị - xã hội", "IV. ĐÁNH GIÁ CHUNG", "1. Kết quả công tác lãnh đạo, chỉ đạo", "2. Kết quả nổi bật, điểm mới, mô hình mới, cách làm sáng tạo, hiệu quả", "3. Hạn chế, tồn tại, nguyên nhân", "4. Vấn đề mới phát sinh, vấn đề phức tạp", "V. NHIỆM VỤ TRỌNG TÂM KỲ TIẾP THEO", "VI. NHỮNG VƯỚNG MẮC, KHÓ KHĂN VÀ KIẾN NGHỊ, ĐỀ XUẤT"];
const CTRLKEY='thu_lam_control_v2';
let CTRL=JSON.parse(localStorage.getItem(CTRLKEY)||'null')||{work:[],reports:[],meetingTasks:[],salary:SALARY_SOURCE};
if(!CTRL.salary||CTRL.salary.length<30) CTRL.salary=SALARY_SOURCE;
function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }
function ce(x){return String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function openCtrl(p){ctrlModal.style.display='block';switchCtrl(p)} function closeCtrl(){ctrlModal.style.display='none'}
function switchCtrl(p){document.querySelectorAll('.ctrl-pane').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.ctrl-tab').forEach(x=>x.classList.toggle('active',x.dataset.c===p));document.getElementById('c-'+p)?.cla
```
```text
.5. Công tác phối hợp với MTTQ và các đoàn thể", "3. Công tác lãnh đạo MTTQ và các tổ chức chính trị - xã hội", "IV. ĐÁNH GIÁ CHUNG", "1. Kết quả công tác lãnh đạo, chỉ đạo", "2. Kết quả nổi bật, điểm mới, mô hình mới, cách làm sáng tạo, hiệu quả", "3. Hạn chế, tồn tại, nguyên nhân", "4. Vấn đề mới phát sinh, vấn đề phức tạp", "V. NHIỆM VỤ TRỌNG TÂM KỲ TIẾP THEO", "VI. NHỮNG VƯỚNG MẮC, KHÓ KHĂN VÀ KIẾN NGHỊ, ĐỀ XUẤT"];
const CTRLKEY='thu_lam_control_v2';
let CTRL=JSON.parse(localStorage.getItem(CTRLKEY)||'null')||{work:[],reports:[],meetingTasks:[],salary:SALARY_SOURCE};
if(!CTRL.salary||CTRL.salary.length<30) CTRL.salary=SALARY_SOURCE;
function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }
function ce(x){return String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function openCtrl(p){ctrlModal.style.display='block';switchCtrl(p)} function closeCtrl(){ctrlModal.style.display='none'}
function switchCtrl(p){document.querySelectorAll('.ctrl-pane').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.ctrl-tab').forEach(x=>x.classList.toggle('active',x.dataset.c===p));document.getElementById('c-'+p)?.classList.add('active');renderCtrlAll()}
function initCtrlSelects(){
 cons
```
```text
 bật, điểm mới, mô hình mới, cách làm sáng tạo, hiệu quả", "3. Hạn chế, tồn tại, nguyên nhân", "4. Vấn đề mới phát sinh, vấn đề phức tạp", "V. NHIỆM VỤ TRỌNG TÂM KỲ TIẾP THEO", "VI. NHỮNG VƯỚNG MẮC, KHÓ KHĂN VÀ KIẾN NGHỊ, ĐỀ XUẤT"];
const CTRLKEY='thu_lam_control_v2';
let CTRL=JSON.parse(localStorage.getItem(CTRLKEY)||'null')||{work:[],reports:[],meetingTasks:[],salary:SALARY_SOURCE};
if(!CTRL.salary||CTRL.salary.length<30) CTRL.salary=SALARY_SOURCE;
function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }
function ce(x){return String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function openCtrl(p){ctrlModal.style.display='block';switchCtrl(p)} function closeCtrl(){ctrlModal.style.display='none'}
function switchCtrl(p){document.querySelectorAll('.ctrl-pane').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.ctrl-tab').forEach(x=>x.classList.toggle('active',x.dataset.c===p));document.getElementById('c-'+p)?.classList.add('active');renderCtrlAll()}
function initCtrlSelects(){
 const opts='<option value="">-- Chọn --</option>'+STAFF.map((x,i)=>`<option value="${i}">${ce(x.name)}</option>`).join('');
 wOwner.innerHTML=opts;rpPerson.innerHTML=opts;wfPerson.innerHTML='<op
```
```text
et saveDate=vdDate.value||new Date().toISOString().slice(0,10);
 let id=Date.now();
 CTRL.directives.push({
   id,no:vdNo.value.trim(),date:saveDate,issuer:vdIssuer.value.trim(),
   area:vdArea.value,title:vdTitle.value.trim(),file:f?f.name:'',
   fileType:f?f.type:'',note:vdNote.value.trim()
 });
 if(f){
   try{ await saveDirectiveFileBlob(id,f); }
   catch(e){ console.error(e); alert('Đã lưu thông tin văn bản nhưng chưa lưu được tệp đính kèm trên trình duyệt này.'); }
 }
 localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
 vdPeriod.value='all'; vdAreaFilter.value=''; vdSearch.value='';
 renderDirectives();
 if(typeof buildDirectiveSummary==='function')buildDirectiveSummary();
 if(typeof renderTTOverview==='function')renderTTOverview();
 alert('Đã lưu văn bản chỉ đạo.');
 vdNo.value='';vdDate.value='';vdIssuer.value='';vdArea.value='';vdTitle.value='';vdNote.value='';
 if(vdFile)vdFile.value='';
}
async function delDirective(id){
 ensureDirectives();
 CTRL.directives=CTRL.directives.filter(x=>x.id!==id);
 localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
 try{await deleteDirectiveFileBlob(id)}catch(e){}
 renderDirectives();
}
function dirPeriodOK(x,m){if(m==='all')return true;if(!x.date)return false;let d=new Date(x.date+'T00:00:00'),n=new Date();if(m==='year')return d.getFullYear()===n.getFullYear();if(m==='month')return d.getFullYear()===n.getFullYear()&&d.getMonth()===n.getMonth();return dateInISOWeek(x.date,isoWeekValue(n))}
function renderDirectives(){
 if(!window.vdGrouped
```
```text
ue='all'; vdAreaFilter.value=''; vdSearch.value='';
 renderDirectives();
 if(typeof buildDirectiveSummary==='function')buildDirectiveSummary();
 if(typeof renderTTOverview==='function')renderTTOverview();
 alert('Đã lưu văn bản chỉ đạo.');
 vdNo.value='';vdDate.value='';vdIssuer.value='';vdArea.value='';vdTitle.value='';vdNote.value='';
 if(vdFile)vdFile.value='';
}
async function delDirective(id){
 ensureDirectives();
 CTRL.directives=CTRL.directives.filter(x=>x.id!==id);
 localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
 try{await deleteDirectiveFileBlob(id)}catch(e){}
 renderDirectives();
}
function dirPeriodOK(x,m){if(m==='all')return true;if(!x.date)return false;let d=new Date(x.date+'T00:00:00'),n=new Date();if(m==='year')return d.getFullYear()===n.getFullYear();if(m==='month')return d.getFullYear()===n.getFullYear()&&d.getMonth()===n.getMonth();return dateInISOWeek(x.date,isoWeekValue(n))}
function renderDirectives(){
 if(!window.vdGrouped)return;ensureDirectives();
 let q=(vdSearch.value||'').toLowerCase(),m=vdPeriod.value,af=vdAreaFilter.value;
 let a=CTRL.directives.filter(x=>dirPeriodOK(x,m)&&(!af||x.area===af)&&(!q||[x.no,x.issuer,x.area,x.title,x.note].join(' ').toLowerCase().includes(q)));
 vdStats.textContent=`Đang hiển thị ${a.length}/${CTRL.directives.length} văn bản đã lưu.`;
 if(!a.length){vdGrouped.innerHTML='<div class="ctrl-note">Chưa có văn bản phù hợp.</div>';return}
 let groups={};
 a.forEach(x=>{let k=x.area||'Chưa phân lĩnh vực';(groups[k]??=[]).push(x)
```
## function csave
```text
 công tác lãnh đạo, chỉ đạo", "2. Kết quả nổi bật, điểm mới, mô hình mới, cách làm sáng tạo, hiệu quả", "3. Hạn chế, tồn tại, nguyên nhân", "4. Vấn đề mới phát sinh, vấn đề phức tạp", "V. NHIỆM VỤ TRỌNG TÂM KỲ TIẾP THEO", "VI. NHỮNG VƯỚNG MẮC, KHÓ KHĂN VÀ KIẾN NGHỊ, ĐỀ XUẤT"];
const CTRLKEY='thu_lam_control_v2';
let CTRL=JSON.parse(localStorage.getItem(CTRLKEY)||'null')||{work:[],reports:[],meetingTasks:[],salary:SALARY_SOURCE};
if(!CTRL.salary||CTRL.salary.length<30) CTRL.salary=SALARY_SOURCE;
function csave(){
      localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));
      renderCtrlAll();
      if(typeof renderTTOverview==='function') renderTTOverview();
      if(typeof renderTTStaff==='function') renderTTStaff();
      if(typeof renderStaffWorkCards==='function') renderStaffWorkCards();
    }
function ce(x){return String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function openCtrl(p){ctrlModal.style.display='block';switchCtrl(p)} function closeCtrl(){ctrlModal.style.display='none'}
function switchCtrl(p){document.querySelectorAll('.ctrl-pane').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.ctrl-tab').forEach(x=>x.classList.toggle('active',x.dataset.c===p));document.getElementById('c-'+p)?.classList.add('active');renderCtrlAll()}
function initCtrlSelects(){
 const opts='<option value="">-- Chọn --</option>'+STAFF.map((x,i)=>`<option value="${i}">${ce(x.name)}</option>`).join('');
 wOwner.innerHTML=opts;rpPerson.
```
## saveSalary
## renderSalary
```text
Đã có QĐ/Ghi chú nâng</b><strong id="slRaised">0</strong></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5
```
```text
/strong></div><div class="ctrl-kpi"><b>Thiếu dữ liệu</b><strong id="slMissing">0</strong></div></div>
  <div class="ctrl-note">Dữ liệu ban đầu được nạp từ <b>Biểu theo dõi nâng lương</b> bạn gửi: họ tên, chức vụ, ngạch, bậc/hệ số, ngày hưởng gần nhất, chu kỳ, số quyết định/ngày ký và ghi chú. Ngày đến hạn được tính lại từ ngày hưởng gần nhất + chu kỳ tháng.</div>
  <div class="ctrl-filter"><input id="slSearch" placeholder="Tìm họ tên..." oninput="renderSalary2()"><select id="slFilter" onchange="renderSalary2()"><option value="">Tất cả</option><option value="late">Quá hạn</option><option value="30">≤30 ngày</option><option value="90">31–90 ngày</option><option value="missing">Thiếu dữ liệu</option></select></div>
  <div style="overflow:auto;max-height:520px"><table class="ctrl-table"><thead><tr><th>Họ tên</th><th>Chức vụ</th><th>Ngạch</th><th>Bậc/HS</th><th>Ngày hưởng gần nhất</th><th>Ngày đến hạn</th><th>Còn</th><th>Số QĐ</th><th>Ngày ký</th><th>Ghi chú</th><th></th></tr></thead><tbody id="salaryRows2"></tbody></table></div>
 </div>
</div></div>
<div id="warehouseModal">
 <div class="modalbox">
  <button class="close" onclick="closeWarehouse()">Đóng ✕</button>
  <h2>KHO NGHIỆP VỤ SỐ – XÃ THƯ LÂM</h2>
  <p>Kho dùng chung trực tuyến. Cán bộ chọn lĩnh vực, tải tài liệu lên và tài liệu sẽ được lưu online để mọi người cùng xem/tải xuống.</p>
  <div class="whgrid" id="warehouseGroups"></div>
  <div style="margin-top:18px;border-top:1px solid #e5d7cd;padding-top:16px">
    <div id="whCurrent" c
```
```text
te()<day)d.setDate(0);return d.toISOString().slice(0,10)}
function salaryBaseDue(x){return addMonthsISO(x.lastDate,x.cycle)}
function salaryNextDue(x){let due=salaryBaseDue(x);return (x.decision&&due&&x.cycle)?addMonthsISO(due,x.cycle):due}
function salaryClass(x){let due=salaryNextDue(x),n=dleft(due);if(!x.lastDate||!x.cycle)return 'missing';if(n<0)return 'late';if(n<=30)return '30';if(n<=90)return '90';return 'ok'}
function updateSalary(i,field,val){CTRL.salary[i][field]=val;csave()}
function renderSalary2(){
 let q=(slSearch.value||'').toLowerCase(),f=slFilter.value;let late=0,d30=0,d90=0,raised=0,miss=0;
 CTRL.salary.forEach(x=>{let c=salaryClass(x);if(c==='late')late++;if(c==='30')d30++;if(c==='90')d90++;if(c==='missing')miss++;if(x.decision)raised++});
 slTotal.textContent=CTRL.salary.length;slLate.textContent=late;sl30.textContent=d30;sl90.textContent=d90;slRaised.textContent=raised;slMissing.textContent=miss;
 salaryRows2.innerHTML=CTRL.salary.map((x,i)=>[x,i]).filter(([x])=>(!q||x.name.toLowerCase().includes(q))&&(!f||salaryClass(x)===f)).map(([x,i])=>{let baseDue=salaryBaseDue(x),due=salaryNextDue(x),n=dleft(due),rem=!due?'Thiếu dữ liệu':n<0?`<span class="st-late">Quá ${Math.abs(n)} ngày</span>`:n<=30?`<span class="st-warn">Còn ${n} ngày</span>`:`Còn ${n} ngày`;let dueText=x.decision&&baseDue?`${ce(due)}<br><small style="color:#2f855a;font-weight:700">Kỳ tiếp theo</small>`:ce(due);return `<tr><td><b>${ce(x.name)}</b></td><td>${ce(x.title)}</td><td>${ce(x.rank)}</td><td>${ce(x.g
```
```text
><td>${ce(x.lastDate)}</td><td>${dueText}</td><td>${rem}</td><td><input style="width:120px" value="${ce(x.decision)}" onchange="updateSalary(${i},'decision',this.value)"></td><td><input type="date" value="${ce(x.decisionDate)}" onchange="updateSalary(${i},'decisionDate',this.value)"></td><td><input style="width:180px" value="${ce(x.note)}" onchange="updateSalary(${i},'note',this.value)"></td><td></td></tr>`}).join('')
}
function renderCtrlAll(){renderMeetingTasks();renderWork();renderReports2();renderSalary2()}
window.addEventListener('load',()=>{initCtrlSelects();renderCtrlAll();setTimeout(dailyWorkNotify,1000)})
</script>


<script>
const TT_STAFF=[{"name": "NGUYỄN TRỌNG HẢI", "title": "UVBTV, Trưởng ban Xây dựng Đảng", "area": "Phụ trách chung"}, {"name": "TÔ VĂN NGỌC", "title": "ĐUV, Phó trưởng ban Xây dựng Đảng", "area": "Phụ trách công tác tổ chức, cán bộ"}, {"name": "TRẦN THỊ SINH", "title": "Chuyên viên", "area": "Phụ trách công tác tổ chức, cán bộ"}, {"name": "ĐÀO THỊ THANH VÂN", "title": "Chuyên viên", "area": "Phụ trách công tác Đảng, đảng viên"}, {"name": "NGUYỄN BÁ MẠNH", "title": "Chuyên viên", "area": "Phụ trách công tác Tuyên giáo"}, {"name": "NGÔ THANH NGÀ", "title": "Chuyên viên", "area": "[CHƯA CÓ THÔNG TIN]"}, {"name": "NGUYỄN THỊ VÂN ANH", "title": "ĐUV, Phó trưởng ban Xây dựng Đảng", "area": "Phụ trách công tác Đảng, đảng viên"}, {"name": "TRƯƠNG HỮU LUYỆN", "title": "ĐUV, Phó trưởng ban Xây dựng Đảng", "area": "Phụ trách công tác Tuyên giáo"}];
function goTT(id){do
```