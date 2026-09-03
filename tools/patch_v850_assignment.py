from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
# Remove prior experimental DOM refinement; V8.51 overrides the actual analyzer data model.
s=re.sub(r'<script id="v850-ai-assignment-refine">.*?</script>','',s,flags=re.S)
s=re.sub(r'<script id="v851-ai-assignment-refine">.*?</script>','',s,flags=re.S)
js=r'''<script id="v851-ai-assignment-refine">
(()=>{
 const clean=t=>String(t||'').replace(/\s+/g,' ').trim();
 const esc=t=>typeof ce==='function'?ce(t):clean(t).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 function getArea(text){const t=clean(text).toLowerCase();if(/biên chế|tổ chức bộ máy|phân cấp quản lý|cán bộ|công chức|viên chức|đánh giá|xếp loại|bổ nhiệm|quy hoạch|điều động|luân chuyển|đào tạo|bồi dưỡng|chính sách cán bộ/.test(t))return 'Tổ chức, cán bộ';if(/đảng viên|chi bộ|tổ chức đảng|kết nạp|chuyển chính thức|sinh hoạt đảng|huy hiệu đảng/.test(t))return 'Đảng, đảng viên';if(/tuyên giáo|tuyên truyền|dư luận|báo chí|không gian mạng|lý luận chính trị|văn hóa|tư tưởng/.test(t))return 'Tuyên giáo';return 'Công tác tổng hợp';}
 function docLabel(text){const t=clean(text);let m=t.match(/(?:QUY ĐỊNH|KẾ HOẠCH|CHỈ THỊ|HƯỚNG DẪN|THÔNG BÁO|CÔNG VĂN|QUYẾT ĐỊNH)\s+(?:SỐ\s*)?[^.;\n]{0,120}/i);if(m)return clean(m[0]).replace(/\s+[-–—]+\s*$/,'');const no=clean(window.aiDocNo?.value||'');return no||'văn bản chỉ đạo';}
 function makeTask(text){return 'Tham mưu triển khai thực hiện '+docLabel(text);}
 function makeProduct(text){const t=clean(text).toLowerCase();const label=docLabel(text);if(/quy định/.test(label.toLowerCase()))return 'Tham mưu văn bản triển khai, tổ chức thực hiện '+label;if(/kế hoạch/.test(label.toLowerCase()))return 'Tham mưu văn bản triển khai, tổ chức thực hiện Kế hoạch';if(/chỉ thị/.test(label.toLowerCase()))return 'Tham mưu văn bản triển khai, tổ chức thực hiện Chỉ thị';if(/báo cáo|tổng hợp kết quả/.test(t))return 'Tham mưu văn bản triển khai thực hiện và báo cáo kết quả theo yêu cầu';return 'Tham mưu văn bản triển khai, tổ chức thực hiện theo yêu cầu của văn bản';}
 window.analyzeAIDocument=function(){
   const text=clean(aiDocText?.value);if(!text)return alert('Chưa có nội dung văn bản để phân tích.');
   const task=makeTask(text),area=getArea(text);
   AI_PROPOSALS=[{id:Date.now(),selected:true,task,area,lead:'',coord:'',product:makeProduct(text),due:typeof inferAIDeadline==='function'?inferAIDeadline(task,text):'',source:text.slice(0,1200),review:true}];
   renderAIProposals();
   aiReadStatus.innerHTML='Đã phân tích văn bản. AI đề xuất <b>01 nhiệm vụ chính</b> để lãnh đạo xem, chỉnh sửa và giao việc.';
 };
 window.renderAIProposals=function(){
   aiTaskCount.textContent=AI_PROPOSALS.length;
   aiNeedReview.textContent=AI_PROPOSALS.filter(x=>!x.lead).length;
   aiHasDeadline.textContent=AI_PROPOSALS.filter(x=>x.due).length;
   aiAssignRows.innerHTML=AI_PROPOSALS.map((x,i)=>`<tr>
    <td><input type="checkbox" ${x.selected?'checked':''} onchange="AI_PROPOSALS[${i}].selected=this.checked"></td>
    <td><textarea class="ai-inline-input" style="min-width:300px;min-height:76px;resize:vertical" oninput="AI_PROPOSALS[${i}].task=this.value">${esc(x.task)}</textarea></td>
    <td><input class="ai-inline-input" value="${esc(x.area)}" oninput="AI_PROPOSALS[${i}].area=this.value"></td>
    <td><select class="ai-inline-select ai-person-select" onchange="AI_PROPOSALS[${i}].lead=this.value;AI_PROPOSALS[${i}].review=!this.value;renderAIProposals()"><option value="" ${!x.lead?'selected':''}>-- Lãnh đạo chọn người thực hiện --</option>${TT_STAFF_WORK.map(p=>`<option ${p.name===x.lead?'selected':''}>${esc(p.name)}</option>`).join('')}</select>${x.lead?`<div class="ai-ok">Đang chọn: ${esc(x.lead)}</div>`:'<div class="ai-review">Chưa chọn người thực hiện</div>'}</td>
    <td><input class="ai-inline-input" value="${esc(x.coord||'')}" placeholder="Để trống nếu không có" oninput="AI_PROPOSALS[${i}].coord=this.value"></td>
    <td><textarea class="ai-inline-input" style="min-width:220px;min-height:76px;resize:vertical" oninput="AI_PROPOSALS[${i}].product=this.value">${esc(x.product)}</textarea></td>
    <td><input type="date" class="ai-inline-input" value="${esc(x.due||'')}" onchange="AI_PROPOSALS[${i}].due=this.value"></td>
    <td><button class="ai-source-btn" onclick="showAISource(${i})">Xem căn cứ</button></td></tr>`).join('');
   const tb=aiAssignRows.closest('table');if(tb){const hs=[...tb.querySelectorAll('th')];hs.forEach(h=>{if(/Nhiệm vụ\/Văn bản/i.test(h.innerText))h.innerText='Nhiệm vụ cụ thể cần thực hiện';if(/Kết quả\/Sản phẩm/i.test(h.innerText))h.innerText='Sản phẩm cần hoàn thành';});}
 };
})();
</script>'''
s=s.replace('</body>',js+'\n</body>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.51">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode();chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html');x=idx.read_text();x=re.sub(r"f\+'\?v=\d+'","f+'?v=851'",x);idx.write_text(x)
print('V8.51 one directive = one editable assignment installed')