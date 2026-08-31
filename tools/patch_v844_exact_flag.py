from pathlib import Path
import base64,gzip,math,re

# Rebuild the EXACT PNG uploaded by the user from text chunks.
parts_b64=[Path(f'assets/co-dang-chuan.b64.part{i}').read_text().strip() for i in range(1,8)]
img=base64.b64decode(''.join(parts_b64))
Path('assets/co-dang-chuan.png').write_bytes(img)

P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
asset='assets/co-dang-chuan.png?v=844'

# Replace the temporary V8.43 SVG reference with the user's exact PNG.
s=s.replace('assets/co-dang-chuan.svg?v=843',asset)
s=s.replace('assets/co-dang-chuan.svg',asset)

# Replace Party-logo-like image sources only; leave all other content/functions untouched.
s=re.sub(r'(<img\b[^>]*\bsrc=["\'])([^"\']*(?:bua|liem|dang|party|co-dang|logo-dang)[^"\']*)(["\'][^>]*>)',lambda m:m.group(1)+asset+m.group(3),s,flags=re.I)

# Replace hammer-and-sickle glyph where used as the visual emblem.
s=s.replace('☭',f'<img src="{asset}" alt="Cờ Đảng" class="v844-party-flag-img">')

# Remove previous flag-only CSS and install exact-image CSS.
s=re.sub(r'<style id="v843-party-flag-fix">.*?</style>','',s,flags=re.S)
css=f'''<style id="v844-party-flag-fix">\n.v844-party-flag-img{{width:100%;height:100%;object-fit:cover;display:block}}\n.party-emblem,.party-logo,.dang-emblem,.dang-logo{{background-image:url('{asset}')!important;background-size:cover!important;background-position:center!important;background-repeat:no-repeat!important;color:transparent!important;overflow:hidden!important}}\n.party-emblem>*,.party-logo>*,.dang-emblem>*,.dang-logo>*{{visibility:hidden!important}}\n</style>'''
s=s.replace('</head>',css+'\n</head>',1)

# Runtime guard: covers login screen + banner even when those blocks are rendered dynamically.
js=f'''<script id="v844-party-flag-runtime">\n(()=>{{\n const SRC='{asset}';\n function applyExactPartyFlag(root=document){{\n  try{{\n   root.querySelectorAll('img').forEach(img=>{{\n    const a=(img.getAttribute('alt')||'').toLowerCase();\n    const c=(img.className||'').toString().toLowerCase();\n    const src=(img.getAttribute('src')||'').toLowerCase();\n    if(a.includes('cờ đảng')||a.includes('co dang')||c.includes('party-logo')||c.includes('dang-logo')||c.includes('party-emblem')||c.includes('dang-emblem')||src.includes('co-dang-chuan')||src.includes('logo-dang')||src.includes('bua-liem')){{img.src=SRC;img.style.objectFit='cover';}}\n   }});\n   root.querySelectorAll('.party-emblem,.party-logo,.dang-emblem,.dang-logo').forEach(el=>{{el.style.setProperty('background-image',`url(${{SRC}})`,'important');el.style.setProperty('background-size','cover','important');el.style.setProperty('background-position','center','important');}});\n  }}catch(e){{}}\n }}\n if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>applyExactPartyFlag());else applyExactPartyFlag();\n new MutationObserver(m=>{{for(const x of m)for(const n of x.addedNodes)if(n.nodeType===1)applyExactPartyFlag(n)}}).observe(document.documentElement,{{childList:true,subtree:true}});\n}})();\n</script>'''
s=s.replace('</body>',js+'\n</body>',1)

s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.44">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode(); chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts): p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html'); x=idx.read_text(); x=re.sub(r"f\+'\?v=\d+'","f+'?v=844'",x); idx.write_text(x)
print('V8.44 exact uploaded Party flag applied; PNG bytes:',len(img))
