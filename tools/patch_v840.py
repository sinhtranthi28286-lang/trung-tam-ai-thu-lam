from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
s=s.replace("for(const k of keys){try{if(typeof getAppFile==='function'){let z=await getAppFile(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}try{if(typeof getDirectiveFile==='function'){let z=await getDirectiveFile(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}try{if(typeof idbGetDirectiveFile==='function'){let z=await idbGetDirectiveFile(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}}", "for(const k of keys){try{if(typeof getDirectiveFileBlob==='function'){let z=await getDirectiveFileBlob(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}try{if(typeof getAppFile==='function'){let z=await getAppFile(String(k));if(z?.blob)z=z.blob;if(z instanceof Blob)return z}}catch(e){}}")
s=re.sub(r'<meta name=\"thu-lam-version\" content=\"[^\"]+\">','<meta name=\"thu-lam-version\" content=\"8.40\">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode(); chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts): p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html'); x=idx.read_text(); x=re.sub(r"f\+'\\?v=\\d+'","f+'?v=840'",x); idx.write_text(x)
print('V8.40 cloud PDF reader fixed')