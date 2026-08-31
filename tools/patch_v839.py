from pathlib import Path
import base64,gzip,math,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode()
# Admin: make Sinh account recognition robust to case/email alias/session profile.
admin_js=r'''
function isSinhAdminAccount(){
 const vals=[];
 try{vals.push(localStorage.getItem('thu_lam_username'),localStorage.getItem('app_username'),localStorage.getItem('username'));}catch(e){}
 try{if(window.CURRENT_APP_USER)vals.push(CURRENT_APP_USER.username,CURRENT_APP_USER.email,CURRENT_APP_USER.full_name);if(window.currentAppUser)vals.push(currentAppUser.username,currentAppUser.email,currentAppUser.full_name);}catch(e){}
 const t=vals.filter(Boolean).join('|').toLowerCase().replace(/[^a-z0-9@._|-]/g,'');
 return t.includes('trolyai_tranthisinh')||t.includes('tranthisinh@thulam.local')||t.includes('sinhtranthi28286@gmail.com')
}
const _oldEnsureAdminExport=window.ensureAdminExport;
window.ensureAdminExport=function(){if(isSinhAdminAccount())return true;return _oldEnsureAdminExport?_oldEnsureAdminExport():false}
'''
# OCR V8.38 wrapper depended on guessed function/file IDs. V8.39 attaches directly to visible button and resolves directive from CTRL + cloud/local file helpers.
ocr_js=r'''
async function v839GetSelectedDirective(){
 const selects=[...document.querySelectorAll('select')];const sel=selects.find(x=>/Chọn văn bản đã lưu/i.test(x.previousElementSibling?.textContent||'')||[...x.options].some(o=>/Số .*TU|Văn bản/i.test(o.textContent||'')));
 const val=sel?.value;let d=(window.CTRL?.directives||[]).find(x=>String(x.id)===String(val)||String(x.fileKey||'')===String(val));
 if(!d&&sel?.selectedIndex>=0){const tx=sel.options[sel.selectedIndex]?.textContent||'';d=(window.CTRL?.directives||[]).find(x=>tx.includes(x.number||x.document_no||'__NO__'))}
 return {d,sel}
}
async function v839GetDirectiveBlob(d){
 if(!d)return null;const keys=[d.fileKey,d.file_key,d.id,'directive-'+d.id].filter(Boolean);
 for(const k of keys){try{if(typeof getAppFile==='function'){let z=await getAppFile(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}try{if(typeof getDirectiveFile==='function'){let z=await getDirectiveFile(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}try{if(typeof idbGetDirectiveFile==='function'){let z=await idbGetDirectiveFile(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}}
 const url=d.fileUrl||d.file_url||d.url;if(url){try{const r=await fetch(url);if(r.ok)return await r.blob()}catch(e){}}
 return null
}
async function v839OCRVisibleSavedDoc(){
 const box=[...document.querySelectorAll('textarea')].find(x=>/Chọn văn bản đã lưu/i.test(x.placeholder||''))||document.querySelector('#aiDocText,#directiveExtractedText,#savedDocText');
 if(!box||!extractedTextTooShort(box.value))return;
 const {d}=await v839GetSelectedDirective();const blob=await v839GetDirectiveBlob(d);if(!blob)return;
 const status=[...document.querySelectorAll('div,span,p')].find(e=>/^Đã đọc:/.test((e.textContent||'').trim()));
 if(status)status.textContent='PDF scan: đang nhận dạng chữ tiếng Việt...';
 const text=await ocrScannedPdfBlob(blob,status);if(text&&text.trim().length>=50){box.value=text.trim();box.dispatchEvent(new Event('input',{bubbles:true}));if(status)status.textContent=`Đã OCR PDF scan • ${text.trim().length.toLocaleString('vi-VN')} ký tự.`;return true}
 if(status)status.textContent='PDF scan chưa nhận dạng đủ nội dung.';return false
}
document.addEventListener('click',async e=>{
 const b=e.target.closest('button');if(!b||!/Đọc văn bản đã lưu/i.test(b.textContent||''))return;
 setTimeout(async()=>{try{await v839OCRVisibleSavedDoc()}catch(err){console.error('V839 OCR',err);alert('Chưa đọc được PDF scan: '+err.message)}},900)
},true);
'''
# Correct multi-language syntax for Tesseract v5: array is documented and more reliable than plus string.
s=s.replace("T.createWorker('vie+eng',1,", "T.createWorker(['vie','eng'],1,")
s=s.replace('</body>','<script>\n'+admin_js+'\n'+ocr_js+'\n</script>\n</body>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.39">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode();chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html');x=idx.read_text();x=re.sub(r"f\+'\?v=\d+'","f+'?v=839'",x);idx.write_text(x)
print('V8.39 admin + OCR fix applied')