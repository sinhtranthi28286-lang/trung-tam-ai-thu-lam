from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')

# Add docx browser library once.
if 'docx@8.5.0' not in s:
    s=s.replace('</head>','<script src="https://unpkg.com/docx@8.5.0/build/index.umd.js"></script>\n</head>',1)

# Add Save + Export buttons next to existing draft button.
old='''<button class="btn light" onclick="buildMeetingDraft()">Tạo dự thảo Kết luận</button>'''
new='''<button class="btn light" onclick="buildMeetingDraft()">Tạo dự thảo Kết luận</button><button class="btn primary" type="button" onclick="saveMeetingNotice()">💾 Lưu Thông báo kết luận</button><button class="btn light" type="button" onclick="exportCurrentMeetingNoticeWord()">📄 Xuất Word Thông báo</button>'''
if old in s:
    s=s.replace(old,new,1)
else:
    s=s.replace('>Tạo dự thảo Kết luận</button>', '>Tạo dự thảo Kết luận</button><button class="btn primary" type="button" onclick="saveMeetingNotice()">💾 Lưu Thông báo kết luận</button><button class="btn light" type="button" onclick="exportCurrentMeetingNoticeWord()">📄 Xuất Word Thông báo</button>',1)

# Add saved notices panel before next control pane.
panel='''
<div id="meetingNoticePanel" style="margin-top:16px;border-top:1px solid #ead8c7;padding-top:12px">
 <div style="display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap"><h3 style="margin:0;color:#a82619">📚 THÔNG BÁO KẾT LUẬN ĐÃ LƯU</h3><span style="font-size:12px;color:#73584a">Lưu dùng chung để theo dõi, mở lại và xuất Word.</span></div>
 <div style="overflow:auto;margin-top:8px"><table class="ctrl-table"><thead><tr><th>STT</th><th>Số/Ký hiệu</th><th>Ngày họp</th><th>Nội dung</th><th>Chủ trì</th><th>Số nhiệm vụ</th><th>Thao tác</th></tr></thead><tbody id="meetingNoticeRows"></tbody></table></div>
</div>
'''
if 'id="meetingNoticePanel"' not in s:
    pos=s.find('<div id="c-aiassign"')
    if pos<0: pos=s.find('<div id="c-work"')
    if pos>=0:s=s[:pos]+panel+s[pos:]

# Make meeting notices part of shared merge so updates are not lost.
s=s.replace("['work','reports','meetingTasks','directives'].forEach", "['work','reports','meetingTasks','directives','meetingNotices'].forEach",1)

js=r'''
function mtv(id){const e=document.getElementById(id);return e?String(e.value||'').trim():''}
function meetingFieldSnapshot(){
 const tasks=JSON.parse(JSON.stringify((CTRL&&Array.isArray(CTRL.meetingTasks))?CTRL.meetingTasks:[]));
 return {date:mtv('mhDate'),place:mtv('mhPlace'),chair:document.getElementById('mhChair')?.selectedOptions?.[0]?.textContent?.replace(/^-- Chọn --$/,'').trim()||'',secretary:document.getElementById('mhSec')?.selectedOptions?.[0]?.textContent?.replace(/^-- Chọn --$/,'').trim()||'',attend:mtv('mhAttend'),agenda:mtv('mhAgenda'),discuss:mtv('mhDiscuss'),general:mtv('mhGeneral'),tasks};
}
function fmtVNDate(iso){if(!iso)return '[CẦN BỔ SUNG]';const a=String(iso).split('-');return a.length===3?`${a[2]}/${a[1]}/${a[0]}`:iso}
function meetingNoticeNumberPrompt(def=''){return prompt('Nhập số/ký hiệu Thông báo kết luận (ví dụ: 12-TB/BXDĐ):',def||'')?.trim()||''}
function meetingNoticeIssueDatePrompt(def=''){return prompt('Nhập ngày ban hành Thông báo theo định dạng YYYY-MM-DD:',def||new Date().toISOString().slice(0,10))?.trim()||''}
async function saveMeetingNotice(){
 try{
  if(!CTRL.meetingNotices)CTRL.meetingNotices=[];
  const snap=meetingFieldSnapshot();if(!snap.date&&!snap.agenda&&!snap.general)return alert('Bạn chưa nhập nội dung cuộc họp để lưu.');
  const no=meetingNoticeNumberPrompt('');if(no===null)return;const issueDate=meetingNoticeIssueDatePrompt(snap.date||'');
  const rec={id:'mn-'+Date.now(),no,issueDate,...snap,createdAt:new Date().toISOString(),createdBy:currentAppProfile?.staff_name||''};
  CTRL.meetingNotices.unshift(rec);csave();renderMeetingNotices();alert('Đã lưu Thông báo kết luận để theo dõi.')
 }catch(e){alert('Không lưu được Thông báo kết luận: '+e.message)}
}
function renderMeetingNotices(){
 const body=document.getElementById('meetingNoticeRows');if(!body)return;const arr=CTRL?.meetingNotices||[];
 body.innerHTML=arr.length?arr.map((x,i)=>`<tr><td>${i+1}</td><td><b>${ce(x.no||'[Chưa có số]')}</b></td><td>${ce(fmtVNDate(x.date))}</td><td>${ce((x.agenda||x.general||'').slice(0,120))}</td><td>${ce(x.chair||'')}</td><td>${(x.tasks||[]).length}</td><td style="white-space:nowrap"><button class="btn light" onclick="openMeetingNotice('${x.id}')">👁 Xem/Sửa</button> <button class="btn light" onclick="exportSavedMeetingNoticeWord('${x.id}')">📄 Word</button> <button class="btn light" onclick="deleteMeetingNotice('${x.id}')">🗑 Xóa</button></td></tr>`).join(''):'<tr><td colspan="7" style="text-align:center;padding:18px;color:#777">Chưa có Thông báo kết luận nào được lưu.</td></tr>'
}
function openMeetingNotice(id){
 const x=(CTRL.meetingNotices||[]).find(y=>y.id===id);if(!x)return;
 const set=(id,v)=>{const e=document.getElementById(id);if(e)e.value=v||''};set('mhDate',x.date);set('mhPlace',x.place);set('mhAttend',x.attend);set('mhAgenda',x.agenda);set('mhDiscuss',x.discuss);set('mhGeneral',x.general);
 const sel=(id,text)=>{const e=document.getElementById(id);if(!e)return;const o=[...e.options].find(o=>o.textContent.trim()===String(text||'').trim());if(o)e.value=o.value};sel('mhChair',x.chair);sel('mhSec',x.secretary);
 CTRL.meetingTasks=JSON.parse(JSON.stringify(x.tasks||[]));localStorage.setItem(CTRLKEY,JSON.stringify(CTRL));renderCtrlAll();alert('Đã mở lại Thông báo kết luận. Bạn có thể chỉnh nội dung rồi lưu thành bản mới hoặc xuất Word.')
}
function deleteMeetingNotice(id){if(!confirm('Xóa Thông báo kết luận đã lưu này?'))return;CTRL.meetingNotices=(CTRL.meetingNotices||[]).filter(x=>x.id!==id);csave();renderMeetingNotices()}
function taskText(t,klist){for(const k of klist){if(t&&t[k]!=null&&String(t[k]).trim())return String(t[k]).trim()}return ''}
async function exportCurrentMeetingNoticeWord(){const snap=meetingFieldSnapshot();const no=meetingNoticeNumberPrompt('');const issueDate=meetingNoticeIssueDatePrompt(snap.date||'');await exportMeetingNoticeWord({...snap,no,issueDate})}
async function exportSavedMeetingNoticeWord(id){const x=(CTRL.meetingNotices||[]).find(y=>y.id===id);if(x)await exportMeetingNoticeWord(x)}
async function exportMeetingNoticeWord(x){
 try{
  if(!window.docx)throw new Error('Thư viện tạo Word chưa tải được. Hãy kiểm tra Internet rồi thử lại.');
  const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,AlignmentType,BorderStyle,VerticalAlign,PageOrientation}=window.docx;
  const none={top:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},bottom:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},left:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},right:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},insideHorizontal:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},insideVertical:{style:BorderStyle.NONE,size:0,color:'FFFFFF'}};
  const tr=(text,opt={})=>new TextRun({text:String(text??''),font:'Times New Roman',size:opt.size||26,bold:!!opt.bold,italics:!!opt.italics});
  const p=(text,opt={})=>new Paragraph({alignment:opt.align||AlignmentType.JUSTIFIED,spacing:{after:opt.after??100,line:360},indent:opt.indent===false?undefined:{firstLine:567},children:[tr(text,opt)]});
  const head=new Table({width:{size:100,type:WidthType.PERCENTAGE},borders:none,rows:[new TableRow({children:[new TableCell({width:{size:45,type:WidthType.PERCENTAGE},borders:none,children:[new Paragraph({alignment:AlignmentType.CENTER,children:[tr('ĐẢNG BỘ XÃ THƯ LÂM',{bold:true})]}),new Paragraph({alignment:AlignmentType.CENTER,children:[tr('BAN XÂY DỰNG ĐẢNG',{bold:true})]}),new Paragraph({alignment:AlignmentType.CENTER,children:[tr('*',{bold:true})]}),new Paragraph({alignment:AlignmentType.CENTER,children:[tr('Số: '+(x.no||'[CẦN BỔ SUNG]'))]})]}),new TableCell({width:{size:55,type:WidthType.PERCENTAGE},borders:none,children:[new Paragraph({alignment:AlignmentType.CENTER,children:[tr('ĐẢNG CỘNG SẢN VIỆT NAM',{bold:true})]}),new Paragraph({alignment:AlignmentType.CENTER,children:[tr('_________________________')]}),new Paragraph({alignment:AlignmentType.CENTER,children:[tr(`Thư Lâm, ngày ${x.issueDate?fmtVNDate(x.issueDate):'[CẦN BỔ SUNG]'}`,{italics:true})]})]})]})]});
  const children=[head,new Paragraph({spacing:{before:180,after:40},alignment:AlignmentType.CENTER,children:[tr('THÔNG BÁO',{bold:true,size:30})]}),new Paragraph({spacing:{after:220},alignment:AlignmentType.CENTER,children:[tr('Kết luận của Trưởng Ban Xây dựng Đảng tại cuộc họp ngày '+fmtVNDate(x.date),{bold:true,size:28})]})];
  const intro=`Ngày ${fmtVNDate(x.date)}, tại ${x.place||'[CẦN BỔ SUNG]'}, Ban Xây dựng Đảng xã Thư Lâm tổ chức cuộc họp do ${x.chair||'[CẦN BỔ SUNG]'} chủ trì. Thành phần: ${x.attend||'[CẦN BỔ SUNG]'}. Sau khi nghe nội dung, ý kiến thảo luận, chủ trì kết luận như sau:`;children.push(p(intro));
  children.push(p('1. Nội dung cuộc họp',{bold:true,indent:false}));children.push(p(x.agenda||'[CẦN BỔ SUNG]'));
  if(x.discuss){children.push(p('2. Ý kiến thảo luận, nội dung đã thống nhất',{bold:true,indent:false}));children.push(p(x.discuss));}
  children.push(p((x.discuss?'3':'2')+'. Kết luận của Trưởng Ban/chủ trì',{bold:true,indent:false}));children.push(p(x.general||'[CẦN BỔ SUNG]'));
  const tasks=x.tasks||[];const n=x.discuss?'4':'3';children.push(p(n+'. Nhiệm vụ tổ chức thực hiện',{bold:true,indent:false}));
  if(tasks.length){tasks.forEach((t,i)=>{const task=taskText(t,['task','name','content','work']);const owner=taskText(t,['owner','person','assignee']);const prod=taskText(t,['product','result']);const due=taskText(t,['due','deadline']);children.push(p(`${i+1}. ${task||'[CẦN BỔ SUNG]'}; thực hiện: ${owner||'[CẦN BỔ SUNG]'}; sản phẩm: ${prod||'[CẦN BỔ SUNG]'}; thời hạn: ${due?fmtVNDate(due):'[CẦN BỔ SUNG]'}.`))})}else children.push(p('[CẦN BỔ SUNG nhiệm vụ, người thực hiện, sản phẩm và thời hạn]'));
  children.push(p('Thông báo này là căn cứ để các đồng chí, bộ phận được giao nhiệm vụ tổ chức thực hiện và báo cáo kết quả theo thời hạn.',{indent:false}));
  const sign=new Table({width:{size:100,type:WidthType.PERCENTAGE},borders:none,rows:[new TableRow({children:[new TableCell({width:{size:55,type:WidthType.PERCENTAGE},borders:none,children:[new Paragraph({children:[tr('Nơi nhận:',{bold:true,italics:true})]}),new Paragraph({children:[tr('- Các đồng chí trong Ban;')]}),new Paragraph({children:[tr('- Lưu Ban Xây dựng Đảng.') ]})]}),new TableCell({width:{size:45,type:WidthType.PERCENTAGE},borders:none,verticalAlign:VerticalAlign.TOP,children:[new Paragraph({alignment:AlignmentType.CENTER,children:[tr('TRƯỞNG BAN',{bold:true})]}),new Paragraph({spacing:{before:900},alignment:AlignmentType.CENTER,children:[tr(x.chair||'') ]})]})]})]});children.push(sign);
  const doc=new Document({styles:{default:{document:{run:{font:'Times New Roman',size:26},paragraph:{spacing:{line:360}}}}},sections:[{properties:{page:{size:{width:11906,height:16838,orientation:PageOrientation.PORTRAIT},margin:{top:1134,right:1134,bottom:1134,left:1701}}},children}]});
  const blob=await Packer.toBlob(doc);const a=document.createElement('a');a.href=URL.createObjectURL(blob);const fn=('Thong_bao_ket_luan_'+(x.no||x.date||'cuoc_hop')).replace(/[\\/:*?"<>|\s]+/g,'_')+'.docx';a.download=fn;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},1500)
 }catch(e){alert('Không xuất được file Word: '+e.message)}
}
const oldRenderCtrlAll=window.renderCtrlAll;
if(typeof oldRenderCtrlAll==='function'){window.renderCtrlAll=function(){const r=oldRenderCtrlAll.apply(this,arguments);try{renderMeetingNotices()}catch(e){}return r}}
window.addEventListener('load',()=>setTimeout(renderMeetingNotices,1500));
'''
if 'function saveMeetingNotice()' not in s:
    s=s.replace('</body>','<script>\n'+js+'\n</script>\n</body>',1)

# Bump version, preserving all existing data.
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.34">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode('utf-8'),9)).decode('ascii');chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text(encoding='utf-8');x=re.sub(r"f\+'\?v=\d+'","f+'?v=834'",x);idx.write_text(x,encoding='utf-8')
print('V8.34 meeting notice save + Word export applied')