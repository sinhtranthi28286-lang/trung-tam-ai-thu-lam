from pathlib import Path
import base64,gzip,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
terms=['Đọc văn bản đã lưu','Đã đọc:','Chưa có nội dung văn bản để phân tích','Nội dung trích xuất từ văn bản','getDirectiveFileBlob','ocrScannedPdfBlob','Tesseract.createWorker','pdfjsLib']
out=[]
for term in terms:
 out.append('\n===== '+term+' =====\n')
 for m in list(re.finditer(re.escape(term),s,re.I))[:8]:
  a=max(0,m.start()-2500); b=min(len(s),m.end()+3500); out.append(s[a:b])
Path('DIAG_OCR_V841.txt').write_text('\n'.join(out),encoding='utf-8')
print('wrote diagnostic',len(s))