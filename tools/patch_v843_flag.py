from pathlib import Path
import base64,gzip,math,re

# Rebuild the exact Party flag PNG from the preserved base64 chunks.
b64=''.join(Path(f'assets/co-dang-chuan.b64.part{i}').read_text().strip() for i in range(1,8))
b64 += '=' * (-len(b64) % 4)
img=base64.b64decode(b64)
Path('assets/co-dang-chuan.png').write_bytes(img)

P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
asset='https://sinhtranthi28286-lang.github.io/trung-tam-ai-thu-lam/assets/co-dang-chuan.png?v=847'

for v in ('v843','v844','v845','v846','v847'):
    s=re.sub(rf'<style id="{v}-party-flag-fix">.*?</style>','',s,flags=re.S)
    s=re.sub(rf'<script id="{v}-party-flag-runtime">.*?</script>','',s,flags=re.S)

s=re.sub(r'assets/co-dang-chuan(?:\.png|\.svg)(?:\?v=\d+)?',asset,s)
s=re.sub(r'(<img\b[^>]*\bsrc=["\'])([^"\']*(?:bua|liem|party|co-dang|logo-dang)[^"\']*)(["\'][^>]*>)',lambda m:m.group(1)+asset+m.group(3),s,flags=re.I)
s=s.replace('☭',f'<img src="{asset}" alt="Cờ Đảng" class="v847-party-flag-img">')

css=f'''<style id="v847-party-flag-fix">
.v847-party-flag-img,img[src*="co-dang-chuan.png"]{{display:block!important;width:100%!important;height:100%!important;object-fit:contain!important;object-position:center center!important;margin:0!important;padding:0!important;background:#df291f!important}}
.party-emblem,.party-logo,.dang-emblem,.dang-logo{{background-image:url('{asset}')!important;background-size:contain!important;background-position:center center!important;background-repeat:no-repeat!important;background-color:#df291f!important;color:transparent!important;overflow:hidden!important}}
.party-emblem>*,.party-logo>*,.dang-emblem>*,.dang-logo>*{{visibility:hidden!important}}
</style>'''
s=s.replace('</head>',css+'\n</head>',1)

js=f'''<script id="v847-party-flag-runtime">
(()=>{{
 const SRC='{asset}';
 function apply(root=document){{
   const imgs=[];
   if(root.matches?.('img')) imgs.push(root);
   root.querySelectorAll?.('img').forEach(i=>imgs.push(i));
   imgs.forEach(img=>{{
     const alt=(img.getAttribute('alt')||'').toLowerCase();
     const src=(img.getAttribute('src')||'').toLowerCase();
     const cls=(img.className||'').toString().toLowerCase();
     if(!(alt.includes('cờ đảng')||alt.includes('co dang')||src.includes('co-dang-chuan')||cls.includes('party-flag'))) return;
     img.src=SRC;
     img.style.setProperty('display','block','important');
     img.style.setProperty('width','100%','important');
     img.style.setProperty('height','100%','important');
     img.style.setProperty('object-fit','contain','important');
     img.style.setProperty('object-position','center center','important');
   }});
   root.querySelectorAll?.('.party-emblem,.party-logo,.dang-emblem,.dang-logo').forEach(el=>{{
     el.style.setProperty('background-image',`url(${{SRC}})`,'important');
     el.style.setProperty('background-size','contain','important');
     el.style.setProperty('background-position','center center','important');
     el.style.setProperty('background-repeat','no-repeat','important');
     el.style.setProperty('background-color','#df291f','important');
   }});
 }}
 const go=()=>{{apply(document);setTimeout(()=>apply(document),300);setTimeout(()=>apply(document),1200)}};
 if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',go); else go();
 new MutationObserver(ms=>ms.forEach(m=>m.addedNodes.forEach(n=>{{if(n.nodeType===1)apply(n)}}))).observe(document.documentElement,{{childList:true,subtree:true}});
}})();
</script>'''
s=s.replace('</body>',js+'\n</body>',1)

s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.47">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode(); chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts): p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html'); x=idx.read_text(); x=re.sub(r"f\+'\?v=\d+'","f+'?v=847'",x); idx.write_text(x)
print('V8.47 exact Party flag restored; bytes=',len(img))
