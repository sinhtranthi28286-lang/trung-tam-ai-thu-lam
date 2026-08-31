from pathlib import Path
import base64,gzip,math,re
P=Path('v825'); parts=[P/f'part{i:02d}.txt' for i in range(1,10)]
s=gzip.decompress(base64.b64decode(''.join(p.read_text().strip() for p in parts))).decode('utf-8')
# Only replace hammer-and-sickle visual marks; do not alter application content/data/functions.
asset='assets/co-dang-chuan.svg?v=843'
# Replace image sources whose filenames/alt clearly refer to Party emblem/flag.
s=re.sub(r'(<img\b[^>]*\bsrc=["\'])([^"\']*(?:bua|liem|dang|party|logo)[^"\']*)(["\'][^>]*>)',lambda m:m.group(1)+asset+m.group(3),s,flags=re.I)
# Replace common hammer-sickle Unicode glyph with the standard image while preserving surrounding text.
s=s.replace('☭',f'<img src="{asset}" alt="Cờ Đảng" style="width:100%;height:100%;object-fit:cover;display:block">')
# Add a narrowly scoped CSS fallback for emblem containers that use text/icon markup.
css=f'''<style id="v843-party-flag-fix">\n.party-emblem,.party-logo,.dang-emblem,.dang-logo{{background-image:url('{asset}')!important;background-size:cover!important;background-position:center!important;background-repeat:no-repeat!important;color:transparent!important;overflow:hidden!important}}\n.party-emblem *, .party-logo *, .dang-emblem *, .dang-logo *{{visibility:hidden!important}}\n</style>'''
s=s.replace('</head>',css+'\n</head>',1)
s=re.sub(r'<meta name="thu-lam-version" content="[^"]+">','<meta name="thu-lam-version" content="8.43">',s,count=1)
packed=base64.b64encode(gzip.compress(s.encode(),9)).decode(); chunk=math.ceil(len(packed)/9)
for i,p in enumerate(parts): p.write_text(packed[i*chunk:(i+1)*chunk])
idx=Path('index.html'); x=idx.read_text(); x=re.sub(r"f\+'\?v=\d+'","f+'?v=843'",x); idx.write_text(x)
print('V8.43 Party flag visual updated only')
