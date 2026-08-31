from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
asset='assets/co-dang-chuan.png?v=845'
# Remove prior flag CSS/runtime if present.
s=re.sub(r'<style id="v843-party-flag-fix">.*?</style>','',s,flags=re.S)
s=re.sub(r'<style id="v844-party-flag-fix">.*?</style>','',s,flags=re.S)
s=re.sub(r'<script id="v844-party-flag-runtime">.*?</script>','',s,flags=re.S)
# Point previous Party flag references to the exact PNG uploaded by the user.
s=s.replace('assets/co-dang-chuan.svg?v=843',asset).replace('assets/co-dang-chuan.svg',asset)
s=s.replace('assets/co-dang-chuan.png?v=844',asset)
# Replace only Party emblem image sources; keep all app content/functions intact.
s=re.sub(r'(<img\b[^>]*\bsrc=["\'])([^"\']*(?:bua|liem|party|co-dang|logo-dang)[^"\']*)(["\'][^>]*>)',lambda m:m.group(1)+asset+m.group(3),s,flags=re.I)
# If a hammer-and-sickle glyph remains, use the exact uploaded image instead.
s=s.replace('☭',f'<img src="{asset}" alt="Cờ Đảng" class="v845-party-flag-img">')
css=f'''<style id="v845-party-flag-fix">
.v845-party-flag-img,img[src*="co-dang-chuan.png"]{{display:block!important;width:100%!important;height:100%!important;object-fit:fill!important;object-position:center!important;margin:0!important;padding:0!important;background:transparent!important}}
.party-emblem,.party-logo,.dang-emblem,.dang-logo{{background-image:url('{asset}')!important;background-size:100% 100%!important;background-position:center!important;background-repeat:no-repeat!important;color:transparent!important;overflow:hidden!important}}
.party-emblem>*,.party-logo>*,.dang-emblem>*,.dang-logo>*{{visibility:hidden!important}}
</style>'''
s=s.replace('</head>',css+'\n</head>',1)
# Preserve the original image ratio (275x183) for the direct image container at login and banner.
js=f'''<script id="v845-party-flag-runtime">
(()=>{{
 const SRC='{asset}', R=275/183;
 function fit(root=document){{
  const imgs=[];
  if(root.matches?.('img')) imgs.push(root);
  root.querySelectorAll?.('img').forEach(x=>imgs.push(x));
  imgs.forEach(img=>{{
   const a=(img.getAttribute('alt')||'').toLowerCase();
   const src=(img.getAttribute('src')||'').toLowerCase();
   if(!(a.includes('cờ đảng')||a.includes('co dang')||src.includes('co-dang-chuan'))) return;
   img.src=SRC;
   const p=img.parentElement;
   if(p){{
    const r=p.getBoundingClientRect();
    const h=Math.max(40,Math.min(100,Math.round(r.height||62)));
    p.style.setProperty('width',Math.round(h*R)+'px','important');
    p.style.setProperty('height',h+'px','important');
    p.style.setProperty('min-width','0','important');
    p.style.setProperty('max-width','none','important');
    p.style.setProperty('padding','0','important');
    p.style.setProperty('overflow','hidden','important');
   }}
   img.style.setProperty('width','100%','important');
   img.style.setProperty('height','100%','important');
   img.style.setProperty('object-fit','fill','important');
   img.style.setProperty('object-position','center','important');
  }});
 }}
 const go=()=>{{fit(document);setTimeout(()=>fit(document),300);setTimeout(()=>fit(document),1200)}};
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go();
 new MutationObserver(ms=>ms.forEach(m=>m.addedNodes.forEach(n=>{{if(n.nodeType===1)fit(n)}}))).observe(document.documentElement,{{childList:true,subtree:true}});
}})();
</script>'''
s=s.replace('</body>',js+'\n</body>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.45">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode(); chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts): p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html'); x=idx.read_text(); x=re.sub(r"f\+'\?v=\d+'","f+'?v=845'",x); idx.write_text(x)
print('V8.45 exact Party flag ratio/alignment fixed')
