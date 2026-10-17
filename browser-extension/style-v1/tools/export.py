import glob,os,sys
from playwright.sync_api import sync_playwright
D='/Users/grahamdobson/Documents/GitHub/versance-edgar/browser-extension/style-v1/screens/'
only=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(channel='chrome',headless=True)
    pg=b.new_page(viewport={'width':1630,'height':960},device_scale_factor=2)
    msgs=[]
    pg.on('console',lambda m: msgs.append(m.text) if m.type=='error' else None)
    import re
    for f in sorted(glob.glob(D+'VBE-*.html')):
        states=re.findall(r'data-state="([^"]+)"',open(f).read())
        for n in states:
            if only and not any(o in n for o in only): continue
            pg.goto('file://'+f+'?export#'+n); pg.reload(); pg.wait_for_timeout(500); pg.evaluate('document.fonts.ready')
            pg.locator('.stage.on').screenshot(path=D+'png/'+n+'.png')
            print('ok',n)
    print('console errors:',msgs[:3]); b.close()
