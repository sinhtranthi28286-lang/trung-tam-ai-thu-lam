from pathlib import Path
import base64,gzip,math,re
P=Path('v825');parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text(encoding='utf-8').strip() for p in parts))).decode('utf-8')
# Load Tesseract.js only when OCR is actually needed, to keep normal startup fast.
js=r'''
async function ensureTesseractOCR(){
 if(window.Tesseract)return window.Tesseract;
 await new Promise((resolve,reject)=>{const sc=document.createElement('script');sc.src='https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js';sc.onload=resolve;sc.onerror=()=>reject(new Error('Không tải được bộ nhận dạng PDF scan. Kiểm tra Internet.'));document.head.appendChild(sc)});
 return window.Tesseract
}
async function ocrScannedPdfBlob(blob,statusEl){
 if(!window.pdfjsLib)throw new Error('Chưa tải được thư viện PDF.');
 const T=await ensureTesseractOCR();const data=new Uint8Array(await blob.arrayBuffer());const pdf=await pdfjsLib.getDocument({data}).promise;let out=[];
 const worker=await T.createWorker('vie+eng',1,{logger:m=>{if(statusEl&&m.status==='recognizing text')statusEl.textContent=`Đang nhận dạng PDF scan: ${Math.round((m.progress||0)*100)}%...`}});
 try{
  for(let i=1;i<=pdf.numPages;i++){if(statusEl)statusEl.textContent=`Đang nhận dạng trang ${i}/${pdf.numPages}...`;const page=await pdf.getPage(i);const vp=page.getViewport({scale:1.7});const cv=document.createElement('canvas');cv.width=Math.ceil(vp.width);cv.height=Math.ceil(vp.height);const ctx=cv.getContext('2d',{willReadFrequently:true});await page.render({canvasContext:ctx,viewport:vp}).promise;const r=await worker.recognize(cv);if(r?.data?.text)out.push(r.data.text.trim());}
 }finally{await worker.terminate()}
 return out.join('\n\n').replace(/\n{3,}/g,'\n\n').trim()
}
function extractedTextTooShort(t){const x=String(t||'').replace(/\s+/g,' ').trim();return x.length<80}
'''
if 'async function ocrScannedPdfBlob' not in s:s=s.replace('</body>','<script>\n'+js+'\n</script>\n</body>',1)
# Wrap existing saved-document reader: if its normal PDF extraction yields too little text, OCR the stored blob and populate extraction box.
wrap=r'''
window.addEventListener('load',()=>setTimeout(()=>{
 const candidates=['readSavedDirective','readSavedDocument','readDirectiveFile','loadSavedDirectiveText'];let fname=candidates.find(n=>typeof window[n]==='function');if(!fname)return;const original=window[fname];
 window[fname]=async function(){
  const r=await original.apply(this,arguments);try{
   const box=document.querySelector('#aiDocText,#directiveExtractedText,#savedDocText,textarea[placeholder*="Chọn văn bản đã lưu"]');const txt=box?.value||'';if(!extractedTextTooShort(txt))return r;
   const sel=document.querySelector('#aiDirectiveSelect,#savedDirectiveSelect,select option:checked')?.closest?.('select')||document.querySelector('select');const id=sel?.value;if(!id)return r;
   let blob=null;if(typeof getDirectiveFile==='function')blob=await getDirectiveFile(id);if(!blob&&typeof idbGetDirectiveFile==='function')blob=await idbGetDirectiveFile(id);if(blob?.blob)blob=blob.blob;if(!(blob instanceof Blob)||!(/pdf/i.test(blob.type)||/\.pdf$/i.test(blob.name||'')))return r;
   const status=[...document.querySelectorAll('div,span,p')].find(e=>/Đã đọc:/.test(e.textContent||''));if(status)status.textContent='PDF không có lớp chữ; đang nhận dạng bản scan...';const ocr=await ocrScannedPdfBlob(blob,status);if(extractedTextTooShort(ocr)){if(status)status.textContent='Không nhận dạng đủ nội dung từ PDF scan.';alert('PDF này là bản scan nhưng hệ thống chưa nhận dạng đủ nội dung. Vui lòng thử bản scan rõ hơn.');return r}if(box){box.value=ocr;box.dispatchEvent(new Event('input',{bubbles:true}))}if(status)status.textContent=`Đã OCR PDF scan • ${ocr.length.toLocaleString('vi-VN')} ký tự.`;
  }catch(e){console.warn('OCR fallback:',e);alert('Không đọc được PDF scan: '+e.message)}return r
 }
},1200));
'''
if 'OCR fallback:' not in s:s=s.replace('</body>','<script>\n'+wrap+'\n</script>\n</body>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.38">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode();chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk],encoding='utf-8')
idx=Path('index.html');x=idx.read_text();x=re.sub(r"f\+'\?v=\d+'","f+'?v=838'",x);idx.write_text(x)
print('V8.38 OCR fallback added')