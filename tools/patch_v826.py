from pathlib import Path
import base64, gzip, math

PART_DIR = Path('v825')
parts = [PART_DIR / f'part{i:02d}.txt' for i in range(1, 10)]
b64 = ''.join(p.read_text(encoding='utf-8').strip() for p in parts)
s = gzip.decompress(base64.b64decode(b64)).decode('utf-8')

# 1) Bỏ chức năng Báo cáo chung, giữ Báo cáo tuần và Báo cáo tháng.
s = s.replace('  <button class="tt-left-item" data-perm="report" onclick="openLeftCtrl(\'report\',this)"><span>📑</span>Báo cáo</button>\n','')
s = s.replace('    <button onclick="openCtrl(\'report\')">📑 Báo cáo</button>\n','')
s = s.replace('      <div class="tt-function" onclick="openCtrl(\'report\')"><div class="tt-icon">📑</div><b>Báo cáo</b><p>Các lĩnh vực nhập kết quả theo đúng mục của mẫu tuần/tháng/quý/năm, sau đó tổng hợp chung.</p><span>Mở Báo cáo →</span></div>\n','')
s = s.replace('  <button class="ctrl-tab" data-c="report" onclick="switchCtrl(\'report\')">📑 Báo cáo</button>\n','')
s = s.replace("['monthlyReport','Báo cáo tháng'],['report','Báo cáo'],['meeting','Kết luận họp'],", "['monthlyReport','Báo cáo tháng'],['meeting','Kết luận họp'],")
s = s.replace('<span><i>🧾</i><b>Báo cáo dùng chung</b><small>Nhập và tổng hợp báo cáo tuần, báo cáo tháng</small></span>', '<span><i>🧾</i><b>Báo cáo tuần & tháng</b><small>Theo dõi và tổng hợp trên các biểu báo cáo đã thiết lập</small></span>')

# 2) Thêm trường tải file ở phần cập nhật kết quả.
old = '<div><label>Ngày ban hành</label><input id="wUpdateOutDate" type="date"></div><div class="span2"><label>Kết quả thực tế/Sản phẩm đã hoàn thành</label><textarea id="wUpdateResult"></textarea></div><div><label>Ghi chú</label><textarea id="wUpdateNote"></textarea></div>'
new = '<div><label>Ngày ban hành</label><input id="wUpdateOutDate" type="date"></div><div><label>File văn bản/sản phẩm đã thực hiện</label><input id="wUpdateFile" type="file" accept=".pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx"><small style="display:block;color:#9f1d16;margin-top:4px">Nhiệm vụ ban hành văn bản: bắt buộc tải file khi cập nhật.</small></div><div class="span2"><label>Kết quả thực tế/Sản phẩm đã hoàn thành</label><textarea id="wUpdateResult"></textarea></div><div><label>Ghi chú</label><textarea id="wUpdateNote"></textarea></div>'
s = s.replace(old, new)
s = s.replace('<th>Tiến độ</th><th>Cảnh báo</th><th>Văn bản ban hành</th><th></th>', '<th>Tiến độ</th><th>Cảnh báo</th><th>Văn bản ban hành</th><th>File đã thực hiện</th><th></th>')

old = "function updateWorkResult(){let id=Number(wUpdateTask.value),x=CTRL.work.find(y=>y.id===id);if(!x)return alert('Chọn nhiệm vụ cần cập nhật.');x.status=wUpdateStatus.value;x.progress=Number(wUpdateProgress.value)||0;x.outNo=wUpdateOutNo.value.trim();x.outDate=wUpdateOutDate.value;x.result=wUpdateResult.value.trim();x.resultNote=wUpdateNote.value.trim();csave();wUpdateResult.value='';wUpdateNote.value='';refreshWorkUpdateSelect()}"
new = "async function updateWorkResult(){let id=Number(wUpdateTask.value),x=CTRL.work.find(y=>y.id===id);if(!x)return alert('Chọn nhiệm vụ cần cập nhật.');const f=wUpdateFile?.files?.[0];const isDocTask=String(x.type||'').includes('Văn bản tham mưu ban hành')||/ban hành.{0,20}văn bản|văn bản.{0,20}ban hành/i.test([x.task,x.product].join(' '));if(isDocTask&&!f&&!x.outputFile)return alert('Nhiệm vụ này là ban hành văn bản. Bạn phải tải file văn bản/sản phẩm đã thực hiện trước khi lưu tiến độ.');if(f){try{await saveWorkOutputFile(id,f);x.outputFile=f.name;x.outputFileType=f.type||'';x.outputFileUpdated=new Date().toISOString()}catch(e){console.error(e);return alert('Không lưu được file văn bản. Vui lòng thử lại.')}}x.status=wUpdateStatus.value;x.progress=Number(wUpdateProgress.value)||0;x.outNo=wUpdateOutNo.value.trim();x.outDate=wUpdateOutDate.value;x.result=wUpdateResult.value.trim();x.resultNote=wUpdateNote.value.trim();csave();wUpdateResult.value='';wUpdateNote.value='';if(wUpdateFile)wUpdateFile.value='';refreshWorkUpdateSelect();renderWork();if(typeof renderDocumentLookup==='function')renderDocumentLookup()}"
s = s.replace(old, new)

helpers = """
function workFileKey(id){return 'work-'+String(id)}
async function saveWorkOutputFile(id,file){return saveDirectiveFileBlob(workFileKey(id),file)}
async function getWorkOutputFile(id){return getDirectiveFileBlob(workFileKey(id))}
async function deleteWorkOutputFile(id){return deleteDirectiveFileBlob(workFileKey(id))}
async function viewWorkOutputFile(id){try{const rec=await getWorkOutputFile(id);if(!rec?.blob)return alert('Không tìm thấy file văn bản đã thực hiện trên trình duyệt này.');const url=URL.createObjectURL(rec.blob);window.open(url,'_blank');setTimeout(()=>URL.revokeObjectURL(url),60000)}catch(e){console.error(e);alert('Không xem được file.')}}
async function downloadWorkOutputFile(id){try{const rec=await getWorkOutputFile(id);if(!rec?.blob)return alert('Không tìm thấy file văn bản đã thực hiện trên trình duyệt này.');const url=URL.createObjectURL(rec.blob),a=document.createElement('a');a.href=url;a.download=rec.name||'van-ban-da-thuc-hien';a.click();setTimeout(()=>URL.revokeObjectURL(url),2000)}catch(e){console.error(e);alert('Không tải được file.')}}
function editOutgoingDoc(id){const x=CTRL.work.find(y=>String(y.id)===String(id));if(!x)return;openCtrl('work');refreshWorkUpdateSelect();wUpdateTask.value=x.id;wUpdateStatus.value=x.status||'Đang thực hiện';wUpdateProgress.value=x.progress||0;wUpdateOutNo.value=x.outNo||'';wUpdateOutDate.value=x.outDate||'';wUpdateResult.value=x.result||'';wUpdateNote.value=x.resultNote||'';setTimeout(()=>wUpdateOutNo?.focus(),120)}
async function deleteOutgoingDoc(id){const x=CTRL.work.find(y=>String(y.id)===String(id));if(!x)return;if(!confirm('Xóa văn bản đi này khỏi mục Tra cứu văn bản? Nhiệm vụ gốc vẫn được giữ lại.'))return;try{await deleteWorkOutputFile(id)}catch(_){}x.outNo='';x.outDate='';x.result='';x.resultNote='';x.outputFile='';x.outputFileType='';x.outputFileUpdated='';csave();renderWork();renderDocumentLookup()}
"""
s = s.replace("const VD_DB_NAME='ThuLamDirectiveFiles';", helpers + "\nconst VD_DB_NAME='ThuLamDirectiveFiles';")

# Cột file trong bảng Công việc.
old = "workRows.innerHTML=arr.map(x=>`<tr><td><b>${ce(x.owner)}</b></td><td>${ce(x.area)}</td><td><small>${ce(x.type)}</small><br>${ce(x.task)}${x.inNo?'<br><b>VB vào:</b> '+ce(x.inNo):''}</td><td>${ce(x.product)}</td><td>${ce(x.due)}</td><td>${x.progress}%<br>${ce(x.status)}</td><td>${remain(x.due,x.status)}</td><td>${x.outNo?ce(x.outNo)+'<br>'+ce(x.outDate):''}</td><td><button class=\"wh-smallbtn\" onclick=\"delWork2(${x.id})\">Xóa</button></td></tr>`).join('');"
new = "workRows.innerHTML=arr.map(x=>`<tr><td><b>${ce(x.owner)}</b></td><td>${ce(x.area)}</td><td><small>${ce(x.type)}</small><br>${ce(x.task)}${x.inNo?'<br><b>VB vào:</b> '+ce(x.inNo):''}</td><td>${ce(x.product)}</td><td>${ce(x.due)}</td><td>${x.progress}%<br>${ce(x.status)}</td><td>${remain(x.due,x.status)}</td><td>${x.outNo?ce(x.outNo)+'<br>'+ce(x.outDate):''}</td><td>${x.outputFile?`<button class=\"wh-smallbtn\" onclick=\"viewWorkOutputFile('${x.id}')\">👁 Xem</button><br><small>${ce(x.outputFile)}</small>`:'—'}</td><td><button class=\"wh-smallbtn\" onclick=\"delWork2(${x.id})\">Xóa</button></td></tr>`).join('');"
s = s.replace(old, new)

# 3) Đồng bộ xuống Tra cứu văn bản -> Văn bản đi, có Xem/Sửa/Xóa.
old = "return works.filter(w=>dlNorm(w.outNo)||dlNorm(w.outDate)||dlNorm(w.result)||dlNorm(w.resultNote)||String(w.status||'').toLowerCase().includes('hoàn')).map(w=>({id:w.id,type:'out',area:dlNorm(w.area)||'Chưa phân lĩnh vực',no:dlNorm(w.outNo),date:dlNorm(w.outDate||w.due),title:dlNorm(w.result||w.resultNote||w.product||w.task),actor:dlNorm(w.owner)}));"
new = "return works.filter(w=>dlNorm(w.outNo)||dlNorm(w.outDate)||dlNorm(w.result)||dlNorm(w.resultNote)||dlNorm(w.outputFile)||String(w.status||'').toLowerCase().includes('hoàn')).map(w=>({id:w.id,type:'out',area:dlNorm(w.area)||'Chưa phân lĩnh vực',no:dlNorm(w.outNo),date:dlNorm(w.outDate||w.due),title:dlNorm(w.result||w.resultNote||w.product||w.task),actor:dlNorm(w.owner),file:dlNorm(w.outputFile)}));"
s = s.replace(old, new)

old = "function dlActions(d){return d.type==='in'?`<div class=\"dl-file-actions\"><button class=\"dl-mini\" onclick=\"viewDirectiveFile('${d.id}')\">👁 Xem</button><button class=\"dl-mini\" onclick=\"downloadDirectiveFile('${d.id}')\">⬇ Tải</button><button class=\"dl-mini\" onclick=\"openDirectiveInAI('${d.id}')\">🤖 AI</button></div>`:`<div class=\"dl-file-actions\"><button class=\"dl-mini\" onclick=\"dlOpenWork()\">↗ Công việc</button></div>`}"
new = "function dlActions(d){return d.type==='in'?`<div class=\"dl-file-actions\"><button class=\"dl-mini\" onclick=\"viewDirectiveFile('${d.id}')\">👁 Xem</button><button class=\"dl-mini\" onclick=\"downloadDirectiveFile('${d.id}')\">⬇ Tải</button><button class=\"dl-mini\" onclick=\"openDirectiveInAI('${d.id}')\">🤖 AI</button></div>`:`<div class=\"dl-file-actions\">${d.file?`<button class=\"dl-mini\" onclick=\"viewWorkOutputFile('${d.id}')\">👁 Xem</button><button class=\"dl-mini\" onclick=\"downloadWorkOutputFile('${d.id}')\">⬇ Tải</button>`:'<span style=\"font-size:12px;color:#999\">Chưa có file</span>'}<button class=\"dl-mini\" onclick=\"editOutgoingDoc('${d.id}')\">✏️ Sửa</button><button class=\"dl-mini\" onclick=\"deleteOutgoingDoc('${d.id}')\">🗑 Xóa</button></div>`}"
s = s.replace(old, new)
s = s.replace('<b>Không tải file lại tại đây.</b> Hệ thống tự tổng hợp <b>📥 Văn bản đến</b> từ Văn bản chỉ đạo và <b>📤 Văn bản đi</b> từ Công việc &amp; văn bản, đồng thời phân loại theo từng lĩnh vực để dễ tra cứu.', 'Hệ thống tự tổng hợp <b>📥 Văn bản đến</b> từ Văn bản chỉ đạo và <b>📤 Văn bản đi</b> từ Công việc &amp; văn bản. Văn bản đi đã thực hiện có thể <b>xem, tải, sửa, xóa</b> trực tiếp tại đây.')

if 'thu-lam-version' not in s:
    s = s.replace('</head>', '<meta name="thu-lam-version" content="8.26">\n</head>', 1)

# Đóng gói lại thành 9 phần như cấu trúc hiện tại.
packed = base64.b64encode(gzip.compress(s.encode('utf-8'), 9)).decode('ascii')
chunk = math.ceil(len(packed) / 9)
for i, p in enumerate(parts):
    p.write_text(packed[i*chunk:(i+1)*chunk], encoding='utf-8')

# Đổi tham số cache để mọi người nhận bản mới trên cùng link.
idx = Path('index.html')
ix = idx.read_text(encoding='utf-8')
ix = ix.replace("f+'?v=825'", "f+'?v=826'")
idx.write_text(ix, encoding='utf-8')

print('Patched Trung tam AI to V8.26')
