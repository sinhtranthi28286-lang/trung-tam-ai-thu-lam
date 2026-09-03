from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
asset='assets/co-dang-chuan.png?v=846'
# Remove all prior flag-only overrides so they cannot distort the original image.
for v in ('v843','v844','v845','v846'):
 s=re.sub(rf'<style id="{v}-party-flag-fix">.*?</style>','',s,flags=re.S)
 s=re.sub(rf'<script id="{v}-party-flag-runtime">.*?</script>','',s,flags=re.S)
s=s.replace('assets/co-dang-chuan.png?v=845',asset).replace('assets/co-dang-chuan.png?v=844',asset).replace('assets/co-dang-chuan.svg?v=843',asset).replace('assets/co-dang-chuan.svg',asset)
s=re.sub(r'(<img\b[^>]*\bsrc=["\'])([^"\']*(?:bua|liem|party|co-dang|logo-dang)[^"\']*)(["\'][^>]*>)',lambda m:m.group(1)+asset+m.group(3),s,flags=re.I)
s=s.replace('☭',f'<img src="{asset}" alt="Cờ Đảng" class="v846-party-flag-img">')
css=f'''<style id="v846-party-flag-fix">
.v846-party-flag-img,img[src*="co-dang-chuan.png"]{{display:block!important;width:100%!important;height:100%!important;object-fit:contain!important;object-position:center center!important;margin:0!important;padding:0!important;background:#df291f!important}}
.party-emblem,.party-logo,.dang-emblem,.dang-logo{{background-image:url('{asset}')!important;background-size:contain!important;background-position:center center!important;background-repeat:no-repeat!important;background-color:#df291f!important;color:transparent!important;overflow:hidden!important}}
.party-emblem>*,.party-logo>*,.dang-emblem>*,.dang-logo>*{{visibility:hidden!important}}
</style>'''
s=s.replace('</head>',css+'\n</head>',1)
# The source PNG is 275x183. Keep that exact aspect ratio at both login and banner; never stretch/crop it.
js=f'''<script id="v846-party-flag-runtime">
(()=>{{
 const SRC='{asset}', R=275/183;
 function fit(root=document){{
  const imgs=[];
  if(root.matches?.('img')) imgs.push(root);
  root.querySelectorAll?.('img').forEach(x=>imgs.push(x));
  imgs.forEach(img=>{{
   const a=(img.getAttribute('alt')||'').toLowerCase(), src=(img.getAttribute('src')||'').toLowerCase();
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
    p.style.setProperty('background','#df291f','important');
   }}
   img.style.setProperty('width','100%','important');
   img.style.setProperty('height','100%','important');
   img.style.setProperty('object-fit','contain','important');
   img.style.setProperty('object-position','center center','important');
  }});
 }}
 const go=()=>{{fit(document);setTimeout(()=>fit(document),250);setTimeout(()=>fit(document),1000)}};
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go();
 new MutationObserver(ms=>ms.forEach(m=>m.addedNodes.forEach(n=>{{if(n.nodeType===1)fit(n)}}))).observe(document.documentElement,{{childList:true,subtree:true}});
}})();
</script>'''
s=s.replace('</body>',js+'\n</body>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.46">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode(); chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts): p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html'); x=idx.read_text(); x=re.sub(r"f\+'\?v=\d+'","f+'?v=846'",x); idx.write_text(x)
print('V8.46 exact uploaded Party flag preserved without stretching/cropping')
