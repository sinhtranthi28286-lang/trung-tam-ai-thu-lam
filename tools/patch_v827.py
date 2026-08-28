from pathlib import Path
import base64, gzip, math, re

PART_DIR = Path('v825')
parts = [PART_DIR / f'part{i:02d}.txt' for i in range(1, 10)]
b64 = ''.join(p.read_text(encoding='utf-8').strip() for p in parts)
s = gzip.decompress(base64.b64decode(b64)).decode('utf-8')

# V8.27 - Quan ly danh sach can bo: them / sua / xoa (ngung hien thi), dung chung Supabase.

style = '''
<style>
.tt-staff-toolbar{display:flex;gap:8px;align-items:center}.tt-staff-toolbar input{flex:1}.tt-staff-admin-note{margin:8px 0;padding:9px 11px;border-radius:9px;background:#fff7ed;border:1px solid #fed7aa;color:#7c2d12;font-size:12px}.tt-staff-editor{margin:8px 0 12px;padding:12px;border:1px solid #e7d6c8;border-radius:10px;background:#fffaf6;display:grid;grid-template-columns:1.2fr 1.1fr 1.7fr auto;gap:9px;align-items:end}.tt-staff-editor label{display:block;font-size:11px;font-weight:700;color:#6b4f42;margin-bottom:4px}.tt-staff-editor input{width:100%;box-sizing:border-box}.tt-staff-editor-actions{display:flex;gap:6px;white-space:nowrap}.tt-staff-action{display:flex;gap:5px;flex-wrap:wrap}.tt-staff-action button{padding:5px 7px;font-size:11px}
@media(max-width:900px){.tt-staff-editor{grid-template-columns:1fr 1fr}.tt-staff-editor-actions{grid-column:1/-1}}@media(max-width:600px){.tt-staff-editor{grid-template-columns:1fr}.tt-staff-editor-actions{grid-column:auto}.tt-staff-toolbar{align-items:stretch;flex-direction:column}}
</style>
'''
if '.tt-staff-toolbar{' not in s:
    s = s.replace('</head>', style + '</head>', 1)

old_panel = '''    <div class="tt-panel">
      <div class="tt-filter-row"><input id="ttStaffSearch" placeholder="🔎 Tìm theo họ tên, chức vụ hoặc lĩnh vực..." oninput="renderTTStaff()"></div>
      <div style="overflow:auto"><table class="tt-table"><thead><tr><th>STT</th><th>Họ và tên</th><th>Chức vụ</th><th>Lĩnh vực phụ trách</th></tr></thead><tbody id="ttStaffRows"></tbody></table></div>
    </div>'''
new_panel = '''    <div class="tt-panel">
      <div class="tt-filter-row tt-staff-toolbar"><input id="ttStaffSearch" placeholder="🔎 Tìm theo họ tên, chức vụ hoặc lĩnh vực..." oninput="renderTTStaff()"><button id="ttAddStaffBtn" class="btn primary" type="button" onclick="openStaffEditor()" style="display:none">➕ Thêm cán bộ</button></div>
      <div id="ttStaffAdminNote" class="tt-staff-admin-note" style="display:none">Quản trị viên có thể thêm cán bộ mới, sửa chức vụ/lĩnh vực phụ trách hoặc xóa cán bộ đã chuyển đi. Dữ liệu được lưu dùng chung trên hệ thống.</div>
      <div id="ttStaffEditor" class="tt-staff-editor" style="display:none">
        <input type="hidden" id="ttStaffEditId">
        <div><label>Họ và tên</label><input id="ttStaffName" placeholder="Nhập họ và tên"></div>
        <div><label>Chức vụ</label><input id="ttStaffTitle" placeholder="Nhập chức vụ"></div>
        <div><label>Lĩnh vực/phân công phụ trách</label><input id="ttStaffArea" placeholder="Nhập lĩnh vực hoặc nhiệm vụ phụ trách"></div>
        <div class="tt-staff-editor-actions"><button class="btn primary" type="button" onclick="saveStaffMember()">💾 Lưu</button><button class="btn light" type="button" onclick="closeStaffEditor()">Hủy</button></div>
      </div>
      <div style="overflow:auto"><table class="tt-table"><thead><tr><th>STT</th><th>Họ và tên</th><th>Chức vụ</th><th>Lĩnh vực phụ trách</th><th id="ttStaffActionHead" style="display:none">Thao tác</th></tr></thead><tbody id="ttStaffRows"></tbody></table></div>
    </div>'''
if old_panel in s:
    s = s.replace(old_panel, new_panel, 1)

old_render = '''function renderTTStaff(){
 let q=(ttStaffSearch?.value||'').toLowerCase();
 let arr=TT_STAFF.filter(x=>!q||[x.name,x.title,x.area].join(' ').toLowerCase().includes(q));
 ttStaffRows.innerHTML=arr.map((x,i)=>{
   let t=ttStaffTasks(x.name),doing=t.filter(y=>y.status!=='Đã hoàn thành').length,done=t.filter(y=>y.status==='Đã hoàn thành').length,late=t.filter(y=>y.status!=='Đã hoàn thành'&&ttDayLeft(y.due)<0).length;
   return `<tr><td>${i+1}</td><td><b>${ce(x.name)}</b></td><td>${ce(x.title)}</td><td>${ce(x.area)}</td></tr>`
 }).join('')
}'''
new_render = '''function renderTTStaff(){
 let q=(ttStaffSearch?.value||'').toLowerCase();
 let arr=TT_STAFF.filter(x=>!q||[x.name,x.title,x.area].join(' ').toLowerCase().includes(q));
 const admin=typeof isAdmin!=='undefined'&&isAdmin;
 const addBtn=document.getElementById('ttAddStaffBtn'),note=document.getElementById('ttStaffAdminNote'),head=document.getElementById('ttStaffActionHead');
 if(addBtn)addBtn.style.display=admin?'':'none';if(note)note.style.display=admin?'':'none';if(head)head.style.display=admin?'':'none';
 ttStaffRows.innerHTML=arr.map((x,i)=>{
   const action=admin?`<td><div class="tt-staff-action"><button class="btn light" type="button" onclick="openStaffEditor(${Number(x.id)||0})">✏️ Sửa</button><button class="btn light" type="button" onclick="deleteStaffMember(${Number(x.id)||0},'${String(x.name).replaceAll("'","\\\\'")}')">🗑 Xóa</button></div></td>`:'';
   return `<tr><td>${i+1}</td><td><b>${ce(x.name)}</b></td><td>${ce(x.title)}</td><td>${ce(x.area||'')}</td>${action}</tr>`
 }).join('')
}'''
if old_render in s:
    s = s.replace(old_render, new_render, 1)

registry_js = r'''
let STAFF_REGISTRY=[];
function applyStaffRegistry(rows){
  STAFF_REGISTRY=(rows||[]).map(x=>({id:Number(x.id)||0,name:String(x.name||'').trim(),title:String(x.title||''),area:String(x.area||''),is_active:x.is_active!==false,sort_order:Number(x.sort_order)||0}));
  const active=STAFF_REGISTRY.filter(x=>x.is_active).sort((a,b)=>(a.sort_order-b.sort_order)||a.name.localeCompare(b.name,'vi'));
  const mapped=active.map(x=>({id:x.id,name:x.name,title:x.title,area:x.area}));
  STAFF.splice(0,STAFF.length,...mapped);TT_STAFF.splice(0,TT_STAFF.length,...mapped);TT_STAFF_WORK.splice(0,TT_STAFF_WORK.length,...mapped);
  try{initCtrlSelects()}catch(e){} try{renderTTStaff();renderTTOverview();renderStaffWorkCards();renderWork()}catch(e){} try{populateNewUserStaff()}catch(e){}
}
async function loadStaffRegistry(){
  try{const {data,error}=await sb.from('staff_members').select('*').eq('is_active',true).order('sort_order',{ascending:true}).order('id',{ascending:true});if(error)throw error;if(data&&data.length)applyStaffRegistry(data);else renderTTStaff()}catch(e){console.warn('Không tải được danh sách cán bộ dùng chung:',e);renderTTStaff()}
}
function openStaffEditor(id=0){
  if(!(typeof isAdmin!=='undefined'&&isAdmin))return alert('Chỉ quản trị viên được thay đổi danh sách cán bộ.');
  const x=STAFF_REGISTRY.find(y=>y.id===Number(id));ttStaffEditId.value=x?.id||'';ttStaffName.value=x?.name||'';ttStaffTitle.value=x?.title||'';ttStaffArea.value=x?.area||'';ttStaffEditor.style.display='grid';ttStaffName.focus()
}
function closeStaffEditor(){ttStaffEditor.style.display='none';ttStaffEditId.value='';ttStaffName.value='';ttStaffTitle.value='';ttStaffArea.value=''}
async function saveStaffMember(){
  if(!(typeof isAdmin!=='undefined'&&isAdmin))return alert('Chỉ quản trị viên được thay đổi danh sách cán bộ.');
  const id=Number(ttStaffEditId.value)||0,name=ttStaffName.value.trim().toUpperCase(),title=ttStaffTitle.value.trim(),area=ttStaffArea.value.trim();if(!name)return alert('Nhập họ và tên cán bộ.');
  const old=STAFF_REGISTRY.find(x=>x.id===id),payload={name,title,area,is_active:true,updated_at:new Date().toISOString()};let error;
  if(id){({error}=await sb.from('staff_members').update(payload).eq('id',id))}else{payload.sort_order=Math.max(0,...STAFF_REGISTRY.map(x=>Number(x.sort_order)||0))+1;({error}=await sb.from('staff_members').insert(payload))}
  if(error)return alert('Không lưu được danh sách cán bộ: '+error.message);
  if(old&&old.name!==name&&typeof CTRL!=='undefined'){CTRL.work?.forEach(x=>{if(x.owner===old.name)x.owner=name});CTRL.reports?.forEach(x=>{if(x.person===old.name)x.person=name});try{csave()}catch(e){}}
  closeStaffEditor();await loadStaffRegistry();alert(id?'Đã cập nhật thông tin cán bộ.':'Đã thêm cán bộ mới.')
}
async function deleteStaffMember(id,name){
  if(!(typeof isAdmin!=='undefined'&&isAdmin))return alert('Chỉ quản trị viên được thay đổi danh sách cán bộ.');if(!id)return alert('Không xác định được cán bộ cần xóa.');
  if(!confirm(`Xóa ${name} khỏi danh sách cán bộ hiện tại?\n\nCác nhiệm vụ và văn bản cũ mang tên đồng chí này vẫn được giữ lại để tra cứu.`))return;
  const {error}=await sb.from('staff_members').update({is_active:false,updated_at:new Date().toISOString()}).eq('id',id);if(error)return alert('Không xóa được cán bộ: '+error.message);await loadStaffRegistry();alert('Đã xóa cán bộ khỏi danh sách hiện tại.')
}
function populateNewUserStaff(){const el=document.getElementById('newUserStaff');if(!el)return;const cur=el.value;el.innerHTML='<option value="">-- Chọn cán bộ --</option>'+STAFF.map((x,i)=>`<option value="${i}">${ce(x.name)}</option>`).join('');if([...el.options].some(o=>o.value===cur))el.value=cur}
window.addEventListener('load',()=>{loadStaffRegistry();setTimeout(()=>{try{renderTTStaff()}catch(e){}},700)});
'''
needle = "window.addEventListener('load',()=>{renderStaffWorkCards();setInterval(renderStaffWorkCards,30000)})\n</script>\n\n<script>\nfunction toggleAISection()"
if 'let STAFF_REGISTRY=[];' not in s and needle in s:
    s = s.replace(needle, "window.addEventListener('load',()=>{renderStaffWorkCards();setInterval(renderStaffWorkCards,30000)})\n" + registry_js + "\n</script>\n\n<script>\nfunction toggleAISection()", 1)

# Khi trạng thái quản trị thay đổi, cập nhật ngay nút Thêm/Sửa/Xóa.
needle_perm = "if(userBtn)userBtn.innerHTML=currentAppProfile?`👤 ${ce(currentAppProfile.staff_name.split(' ').slice(-2).join(' '))}`:'👤 Đăng nhập';\n}"
if needle_perm in s and "try{renderTTStaff()}catch(e){}\n}" not in s:
    s = s.replace(needle_perm, "if(userBtn)userBtn.innerHTML=currentAppProfile?`👤 ${ce(currentAppProfile.staff_name.split(' ').slice(-2).join(' '))}`:'👤 Đăng nhập';\n try{renderTTStaff()}catch(e){}\n}", 1)

if 'thu-lam-version" content="8.27' not in s:
    s = re.sub(r'<meta name="thu-lam-version" content="[^"]+">', '<meta name="thu-lam-version" content="8.27">', s, count=1)
    if 'thu-lam-version' not in s:
        s = s.replace('</head>', '<meta name="thu-lam-version" content="8.27">\n</head>', 1)

packed = base64.b64encode(gzip.compress(s.encode('utf-8'), 9)).decode('ascii')
chunk = math.ceil(len(packed) / 9)
for i, p in enumerate(parts):
    p.write_text(packed[i*chunk:(i+1)*chunk], encoding='utf-8')

idx = Path('index.html')
ix = idx.read_text(encoding='utf-8')
ix = re.sub(r"f\+'\?v=\d+'", "f+'?v=827'", ix)
idx.write_text(ix, encoding='utf-8')
print('Patched Trung tam AI to V8.27 - staff management')
