from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')

js=r'''<script id="v850-ai-assignment-refine">
(()=>{
 const clean=t=>String(t||'').replace(/\s+/g,' ').trim();
 const low=t=>clean(t).toLowerCase();
 function area(text){const t=low(text);if(/cán bộ|biên chế|đánh giá|xếp loại|bổ nhiệm|quy hoạch|điều động|đào tạo|bồi dưỡng|chính sách cán bộ/.test(t))return 'Tổ chức, cán bộ';if(/đảng viên|chi bộ|tổ chức đảng|kết nạp|chuyển chính thức|sinh hoạt đảng|huy hiệu đảng/.test(t))return 'Đảng, đảng viên';if(/tuyên giáo|tuyên truyền|dư luận|báo chí|văn hóa|tư tưởng|chỉ thị 24/.test(t))return 'Tuyên giáo';return 'Công tác tổng hợp';}
 function task(text){const t=clean(text);let m=t.match(/(?:giao|yêu cầu|đề nghị)[^.;:]{0,100}(?:ban xây dựng đảng|đảng ủy|cấp ủy)?[^.;]{8,220}/i);if(m)return 'Tham mưu triển khai thực hiện '+clean(m[0]).replace(/^(giao|yêu cầu|đề nghị)\s*/i,'').replace(/[.;,]+$/,'');let title=t.match(/(?:kế hoạch|chỉ thị|quy định|hướng dẫn|công văn|thông báo)\s+(?:số\s*)?[^.;\n]{3,90}/i);return title?'Tham mưu triển khai thực hiện '+clean(title[0]):'Tham mưu triển khai thực hiện nội dung văn bản chỉ đạo';}
 function product(text){const t=low(text);if(/báo cáo|tổng hợp kết quả/.test(t))return 'Tham mưu văn bản triển khai thực hiện và báo cáo kết quả theo yêu cầu của văn bản';if(/kế hoạch/.test(t))return 'Tham mưu văn bản triển khai, tổ chức thực hiện Kế hoạch';if(/chỉ thị/.test(t))return 'Tham mưu văn bản triển khai, tổ chức thực hiện Chỉ thị';return 'Tham mưu văn bản triển khai, tổ chức thực hiện theo yêu cầu của văn bản';}
 function table(){return [...document.querySelectorAll('table')].find(x=>{const h=low(x.tHead?.innerText||x.querySelector('thead')?.innerText||'');return h.includes('nhiệm vụ/văn bản')&&h.includes('người thực hiện')&&h.includes('kết quả/sản phẩm')});}
 function source(){const ta=[...document.querySelectorAll('textarea')].find(x=>/nội dung trích xuất|trích xuất/i.test((x.placeholder||'')+' '+(x.previousElementSibling?.innerText||'')));return clean(ta?.value||window.__thuLamDirectiveExtract||'');}
 function setControl(cell,val,blank=false){const e=cell?.querySelector('textarea,input,select');if(!e)return false;if(e.tagName==='SELECT'){if(blank){e.value='';e.selectedIndex=0;}else{const o=[...e.options].find(o=>low(o.textContent)===low(val)||low(o.textContent).includes(low(val)));if(o)e.value=o.value;else return false}}else e.value=blank?'':val;e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));return true;}
 function refine(){const tb=table();if(!tb)return false;const rows=[...tb.querySelectorAll('tbody tr')];if(!rows.length)return false;const text=source()||clean(rows.map(r=>r.cells?.[1]?.innerText||'').join(' '));const first=rows[0];rows.slice(1).forEach(r=>r.remove());const c=first.cells;if(!c||c.length<7)return false;setControl(c[1],task(text));if(!c[1].querySelector('textarea,input')){c[1].contentEditable='true';c[1].innerText=task(text)}setControl(c[2],area(text));setControl(c[3],'',true);setControl(c[4],'',true);setControl(c[5],product(text));const headers=[...tb.querySelectorAll('thead th')];headers.forEach(h=>{if(/nhiệm vụ\/văn bản/i.test(h.innerText))h.innerText='Nhiệm vụ cụ thể cần thực hiện';if(/kết quả\/sản phẩm/i.test(h.innerText))h.innerText='Sản phẩm cần hoàn thành'});return true;}
 let timer=null;const obs=new MutationObserver(()=>{clearTimeout(timer);timer=setTimeout(refine,120)});const start=()=>{obs.observe(document.body,{childList:true,subtree:true});refine()};if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();
 document.addEventListener('click',e=>{const b=e.target.closest('button');if(b&&/phân tích.*đề xuất giao việc/i.test(b.innerText||''))setTimeout(refine,250)},true);
})();
</script>'''
if 'id="v850-ai-assignment-refine"' not in s:s=s.replace('</body>',js+'\n</body>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.50">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode();chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts):p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html');x=idx.read_text();x=re.sub(r"f\+'\?v=\d+'","f+'?v=850'",x);idx.write_text(x)
print('V8.50 assignment refinement installed')
