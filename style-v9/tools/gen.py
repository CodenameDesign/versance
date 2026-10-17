import os,re
OUT='/Users/grahamdobson/Documents/GitHub/versance-edgar/browser-extension/style-v9/screens/'
FA_ICONS={'gavel','out'}
def ic(paths,cls='ico',vb='0 0 24 24'): return f'<svg class="{cls}" viewBox="{vb}" aria-hidden="true">{paths}</svg>'
I=dict(
 backpack='<path d="M4 10a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M8 21v-5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v5"/><path d="M8 10h8"/>',
 folder='<path d="M20 17a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3.9a2 2 0 0 1-1.69-.9l-.81-1.2a2 2 0 0 0-1.67-.9H8a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2Z"/><path d="M2 8v11a2 2 0 0 0 2 2h14"/>',
 bank='<path d="M3 22h18M6 18v-7M10 18v-7M14 18v-7M18 18v-7M12 2l8 5H4z"/>',
 gavel='<path d="M256.4 204.1L228.3 176L320.4 83.9L348.5 112L256.4 204.1zM188.7 204.3L228.1 243.7C239.3 254.9 255.5 258.1 269.6 253.2L311.4 295L79.4 527C70 536.4 70 551.6 79.4 560.9C88.8 570.2 104 570.3 113.3 560.9L345.3 328.9L387.1 370.7C382.2 384.7 385.4 401 396.6 412.2L436 451.6C451.6 467.2 476.9 467.2 492.6 451.6L596.1 348.3C611.7 332.7 611.7 307.4 596.1 291.7L556.7 252.3C545.5 241.1 529.3 237.9 515.2 242.8L397.6 125.2C402.5 111.2 399.3 94.9 388.1 83.7L348.7 44.3C333.1 28.7 307.8 28.7 292.1 44.3L188.7 147.7C173.1 163.3 173.1 188.6 188.7 204.3zM478.5 274L418.4 334.1L306.4 222.1L366.5 162L478.5 274zM556.6 320L464.5 412.1L436.4 384L528.5 291.9L556.6 320z"/>',
 out='<path d="M240.5 112L128.5 112C119.7 112 112.5 119.2 112.5 128L112.5 512C112.5 520.8 119.7 528 128.5 528L384.5 528C393.3 528 400.5 520.8 400.5 512L400.5 464L448.5 464L448.5 512C448.5 547.3 419.8 576 384.5 576L128.5 576C93.2 576 64.5 547.3 64.5 512L64.5 128C64.5 92.7 93.2 64 128.5 64L262 64C279 64 295.3 70.7 307.3 82.7L429.8 205.3C441.8 217.3 448.5 233.6 448.5 250.6L448.5 320.1L400.5 320.1L400.5 272.1L312.5 272.1C272.7 272.1 240.5 239.9 240.5 200.1L240.5 112.1zM312.5 368L526.6 368L495.6 337C486.2 327.6 486.2 312.4 495.6 303.1C505 293.8 520.2 293.7 529.5 303.1L601.5 375.1C610.9 384.5 610.9 399.7 601.5 409L529.5 481C520.1 490.4 504.9 490.4 495.6 481C486.3 471.6 486.2 456.4 495.6 447.1L526.6 416.1L312.5 416.1C299.2 416.1 288.5 405.4 288.5 392.1C288.5 378.8 299.2 368.1 312.5 368.1zM380.6 224L288.5 131.9L288.5 200C288.5 213.3 299.2 224 312.5 224L380.6 224z"/>',
 hist='<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/>',
 home='<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
 arr='<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>', arl='<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
 min='<path d="m3 3 7 7"/><path d="M4 10h6V4"/><path d="m21 21-7-7"/><path d="M20 14h-6v6"/>',
 info='<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
 page='<path d="M16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V8z"/><path d="M15 3v5h6"/><path d="M8 13h8M8 17h5"/>',
 plus='<path d="M12 5v14M5 12h14"/>', send='<path d="M12 19V5"/><path d="m5 12 7-7 7 7"/>',
 chev='<path d="m6 9 6 6 6-6"/>', x='<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
 sliders='<path d="M21 4h-7M10 4H3M21 12h-9M8 12H3M21 20h-5M12 20H3M14 2v4M8 10v4M16 18v4"/>',
 pen='<path d="M12 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.375 2.625a1 1 0 0 1 3 3l-9.013 9.014a2 2 0 0 1-.853.505l-2.873.84a.5.5 0 0 1-.62-.62l.84-2.873a2 2 0 0 1 .506-.852z"/>',
 ext='<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
 dl='<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
 cmp='<rect width="14" height="14" x="8" y="8" rx="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>',
 globe='<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
 bpadd='<path d="M4 10a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M12 12v6M9 15h6"/>',
 user='<circle cx="12" cy="9" r="3.5"/><path d="M5 20c1-4 4-5.5 7-5.5s6 1.5 7 5.5"/>',
 puzzle='<path d="M15.39 4.39a1 1 0 0 0 1.68-.474 2.5 2.5 0 1 1 3.014 3.015 1 1 0 0 0-.474 1.68l1.683 1.682a2.414 2.414 0 0 1 0 3.414L19.61 15.39a1 1 0 0 1-1.68-.474 2.5 2.5 0 1 0-3.014 3.015 1 1 0 0 1 .474 1.68l-1.683 1.682a2.414 2.414 0 0 1-3.414 0L8.61 19.61a1 1 0 0 0-1.68.474 2.5 2.5 0 1 1-3.014-3.015 1 1 0 0 0 .474-1.68l-1.683-1.682a2.414 2.414 0 0 1 0-3.414L4.39 8.61a1 1 0 0 1 1.68.474 2.5 2.5 0 1 0 3.014-3.015 1 1 0 0 1-.474-1.68l1.683-1.682a2.414 2.414 0 0 1 3.414 0z"/>',
 back='<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>', dots='<circle cx="12" cy="5" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="12" cy="19" r="1.2"/>',
 reload='<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
 download2='<path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/>',
)
LOGO='<svg class="{c}" viewBox="0 0 84 84"><path fill="{f}" fill-rule="evenodd" d="M84,42c0,23.196-18.804,42-42,42S0,65.196,0,42,18.804,0,42,0s42,18.804,42,42ZM21.856,32.513c0-.981-.8-1.777-1.788-1.777s-1.788.796-1.788,1.777v17.956c0,.981.8,1.777,1.788,1.777s1.788-.796,1.788-1.777v-17.956ZM30.89,27.93c0-.981-.8-1.777-1.788-1.777s-1.788.796-1.788,1.777v27.122c0,.981.8,1.777,1.788,1.777s1.788-.796,1.788-1.777v-27.122ZM39.924,31.765c0-.981-.8-1.777-1.788-1.777s-1.788.796-1.788,1.777v19.453c0,.981.8,1.777,1.788,1.777s1.788-.796,1.788-1.777v-19.453ZM47.403,33.355h-.467c-.859,0-1.555.692-1.555,1.545v13.183c0,.853.696,1.545,1.555,1.545h.467c.859,0,1.555-.692,1.555-1.545v-13.183c0-.853-.696-1.545-1.555-1.545ZM57.992,26.714c0-.981-.8-1.777-1.788-1.777s-1.788.796-1.788,1.777v29.74c0,.981.8,1.777,1.788,1.777s1.788-.796,1.788-1.777v-29.74ZM67.025,30.642c0-.981-.8-1.777-1.788-1.777s-1.788.796-1.788,1.777v21.697c0,.981.8,1.777,1.788,1.777s1.788-.796,1.788-1.777v-21.697Z"/></svg>'
def logo(c,f): return LOGO.format(c=c,f=f)
def i(n,c='ico'): return ic(I[n],c+' fa','0 0 640 640') if n in FA_ICONS else ic(I[n],c)

def chrome():
    return f'''<div class="tabbar"><span class="tl" style="left:20px;background:#FF5F57"></span><span class="tl" style="left:50px;background:#FEBC2E"></span><span class="tl" style="left:80px;background:#28C840"></span>
<div class="tab-cur"><span class="x" style="right:16px;top:12px">{i('x','ico sm')}</span></div><span class="plus" style="position:absolute;left:402px;top:15px;color:#1f1f1f">{i('plus','ico')}</span></div>
<div class="toolbar"><span class="tb-ic" style="left:20px">{i('arl')}</span><span class="tb-ic" style="left:62px;color:#9aa">{i('arr')}</span><span class="tb-ic" style="left:104px">{i('reload')}</span>
<div class="omni"></div><span class="ext-btn">{logo('','#324EFE').replace('<svg class=""','<svg style="width:28px;height:28px"')}</span>
<span class="tb-ic" style="right:222px">{i('puzzle')}</span><span class="tb-ic" style="right:96px">{i('dl')}</span><span class="avatar-chrome"></span><span class="tb-ic" style="right:14px">{i('dots')}</span></div>'''

def rail(active,badge=3):
    items=[('home','home',None),('backpack','research',None),('folder','filings',None),('bank','cad','CAD'),('bank','us','US'),('gavel','compliance',None),('out','output',None),('hist','history',None)]
    h=''
    for icn,key,cc in items:
        a=' active' if key==active else ''
        b=''
        if key=='research' and badge: b=f'<span class="badge">{badge}</span>'
        if cc: h+=f'<button class="rail-btn has-cc{a}">{i(icn)}<span class="cc">{cc}</span></button>'
        else: h+=f'<button class="rail-btn{a}">{i(icn)}{b}</button>'
    return f'<div class="rail">{h}</div>'

def cbar(name='INTEGRA RESOURCES CORP'): return f'<div class="cbar"><span>{name}</span><span class="edit">edit</span></div>'
def navs(): return ''   # Home now lives in the icon rail
def collapse(): return f'<span class="sq collapse">{i("min")}</span>'
def strip(second=None,btn='new chat'):
    if second: t=f'<span class="t">Coworker</span><span class="t on">{second}</span>'
    else: t='<span class="t">Coworker</span>'
    return f'<div class="strip"><div class="seg">{t}</div><span class="newc">{btn}</span></div>'
def closex(cls='close'): return f'<button class="{cls}" aria-label="Close">{i("x","ico xs")}</button>'
def composer(ph='Ask me anything…',ws='off',send_on=False,export_on=False,actrow=True):
    s='' if send_on else ' disabled'
    wsb=f'<span class="ws on">{i("globe","ico sm")}Web Search On</span>' if ws=='on' else f'<span class="ws off">{i("globe","ico sm")}Web Search Off</span>'
    e=f'<button class="btn o exp"{"" if export_on else " disabled"}>Export Conversation {i("ext","ico xs")}</button>'
    row=f'<div class="actrow">{wsb}{e}</div>' if actrow else ''
    at='<svg class="ico sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 8"/></svg>'
    sl='<svg class="ico sm" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><path d="m15 9-6 6"/></svg>'
    return f'<div class="composer"><div class="inrow"><input class="chat-in" type="text" placeholder="{ph}" aria-label="Message"><div class="tools"><span class="plus">{i("plus","ico sm")}</span><span class="tool">{at}</span><span class="tool">{sl}</span><button class="send-btn"{s} aria-label="Send">{i("send","ico sm")}</button></div></div>{row}</div>'
def foot(): return f'<div class="pane-foot">{logo("logo-dark","#0A1922")}<span>Open Versance.ai</span>{i("ext","ico xs")}</div>'
def ptitle(t,q=True): return f'<div class="ptitle">{t}{"<span class=q>?</span>" if q else ""}</div>'
def pane(inner,title=None,sub=None,q=True):
    h=''
    if title: h+=ptitle(title,q)
    if sub: h+=f'<div class="psub">{sub}</div>'
    return f'<div class="pane"><div class="pane-main">{h}{inner}</div>{foot()}</div>'
def panel(kind,body,active,badge=3):
    nv=navs() if kind=='wide' else ''
    return f'<div class="panel {kind}">{cbar()}{nv}{collapse()}{body}{rail(active,badge)}<button class="themebtn" type="button" aria-label="Switch dark / light mode" title="Switch dark / light mode"><svg class="ico sm sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="ico sm moon" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button><span class="userav">{i("user","ico sm")}</span></div>'
def page(name,inner):
    return f'''<div class="stage vc-ext {'c' if 'panel compact' in inner else 'w'}" data-state="@@STATE@@" aria-label="{name}">{inner}</div>'''

SRC=[('Company A'),('Company B'),('Company C')]
TITLE='52-109F2 - Certification of interim filings - CFO (E)'
def srccards():
    return ''.join(f'<div class="srccard"><button class="x" aria-label="Remove">{i("x","ico xs")}</button>{c}<br>{TITLE}<div class="d">07/29/2024</div></div>' for c in SRC)
def list_rows(n,hov=None,inline=False):
    r=''
    for k in range(n):
        if inline:
            h=' hov' if k==hov else ''
            add=f'<span class="addi">{i("bpadd","ico")}</span>'
            r+=f'<div class="li{h}">{TITLE} <span class="d">07/29/2024</span>{add}</div>'
        else: r+=f'<div class="li">{TITLE}<div class="d">07/29/2024</div></div>'
    return f'<div class="list{" stack" if inline else ""}">{r}</div>'
def toggles(cur_on=True):
    c='on' if cur_on else ''
    return f'<div class="toggle-row"><span>All INTEGRA RESOURCES C… Filings</span><span class="tog on"></span></div><div class="toggle-row"><span>Current URL</span><span class="tog {c}"></span></div>'
def searchbar(ph,filt=True):
    f=f'<span class="filter">{i("sliders")}</span>' if filt else ''
    return f'<div class="searchrow"><input class="field" placeholder="{ph}" style="flex:1">{f}</div>'

S={}
# ── 101a / ab / ac / b: compact ────────────────────────────────────────
WELCOME=f'''<div class="tile w">{closex("close")}{logo("logo28","#23221F")}<p class="hi">Hi,</p><p class="lead">Welcome to the Versance Coworker</p><p style="margin:0">I can help you research any Canadian or US public company's filings and news, and see how they compare with peers and with the page you're working on. Every answer comes with its sources. When you're drafting, I can also check your work against securities regulations before it goes out.</p></div>'''
CHIPS=f'<div class="chips"><span class="chip">{i("info","ico sm")}How it works</span><span class="chip">{i("page","ico sm")}Summarise the current web page</span><span class="chip">{i("gavel","ico sm")}Run a compliance review</span></div>'
def compact_chat(extra=''):
    return f'<div class="chatcol"><div class="chatbody full">{WELCOME}</div>{CHIPS}{composer(ws="on")}</div>{extra}'
S['VBE-101a-Coworker-Small']=page('Coworker — Small',panel('compact',compact_chat(),'home',badge=0))
dd1=f'<div class="dd"><div class="caps grp">Recent companies</div><div class="it">Company One</div><div class="it">Company Two</div><div class="it">Company Three</div></div>'
def sw(value,dd,exit_=False):
    ex='<span class="exit">EXIT</span>' if exit_ else ''
    inner=f'<div class="cbar search"><span>{value}<span class="caret"></span></span>{ex}</div>'
    return inner
def switcher_panel(value,dd,exit_):
    body=compact_chat(dd)
    p=panel('compact',body,'home',badge=0)
    return p.replace(cbar(),sw(value,dd,exit_))
S['VBE-101ab-Coworker-Switch']=page('Coworker — Switch',switcher_panel('',dd1,False))
dd2=f'<div class="dd"><div class="caps grp">Recent companies</div><div class="it">Aardvark Mines</div><hr><div class="caps grp">All companies</div><div class="it">Aarial Company</div><div class="it">Aarke Capital</div>'+'<div class="it">Aarke Mines</div>'*5+'</div>'
S['VBE-101ac-Coworker-Switch']=page('Coworker — Switch (search)',switcher_panel('Aar',dd2,True))
HELP=f'''<div class="helpfill">{closex("close")}<div class="info-title">How the Versance Coworker Works</div>
<h3 class="info-sub" style="margin-top:20px">1. Choose a primary company</h3><p class="info">Select a company at the top. All of its filings and news are added to context, so you can ask me anything about it. Switch to another company at any time.</p>
<h3 class="info-sub">2. Add documents to research context</h3><p class="info">Open the CAD or US library, find any company, and add the filings or news releases you want to compare to your research context. You can also upload your own documents or add a web page.</p>
<h3 class="info-sub">3. Ask and compare</h3><p class="info">Ask me questions across your primary company's record, the documents in your research context and the page you're working on. Every answer shows its sources.</p>
<h3 class="info-sub">4. Run a compliance review</h3><p class="info">Open Compliance review to check the page you have open, whether it's your own draft or a document you're reviewing, against Canadian or US securities regulations.</p></div>'''
S['VBE-101b-Coworker-About']=page('Coworker — About',panel('compact',f'<div class="chatcol">{HELP}{composer(ws="on")}</div>','home',badge=0))

# ── expanded screens ───────────────────────────────────────────────────
def wide(chat,right,active,badge=3): return panel('wide',chat+right,active,badge)
def chat_empty(second=None,**kw): return f'<div class="chatcol">{strip(second)}{kw.get("body","")}{composer(**{k:v for k,v in kw.items() if k!="body"})}</div>'
S['VBE-102a-Coworker-Backpack']=page('Backpack',wide(chat_empty(),pane(f'{toggles()}<div class="links"><span class="lnk">Add a URL</span><span class="lnk">Upload a Document</span></div><hr class="hair"><div class="sh"><span>Sources in this conversation</span><span class="clr">Clear all</span></div>{srccards()}<span class="lnk">Ask Coworker to compare these documents</span>','Research context','Coworker answers using everything listed here'),'research'))
S['VBE-102aa-Coworker-Backpack-Add-URL']=page('Backpack — Add URL',wide(chat_empty(),pane(f'{toggles()}<div class="links" style="margin-bottom:10px"><span>Add a URL</span><span class="lnk">Cancel</span></div><div class="srcrow"><input class="field" placeholder="Paste a link"><button class="btn p" disabled>ADD</button></div><hr class="hair"><div class="sh"><span>Sources in this conversation</span><span class="clr">Clear</span></div>{srccards()}','Research context','Coworker answers using everything listed here'),'research'))
empty_card='<div class="infoblock"><div class="info"><p style="margin:0 0 10px"><b>No documents added yet.</b></p><p style="margin:0 0 10px">To benchmark companies, open the CAD or US library, choose a company and add its filings or news releases here.</p><p style="margin:0">Add as many as you need, from as many companies as you need.</p></div></div>'
S['VBE-102s-Coworker-Backpack-Start']=page('Backpack — Empty',wide(chat_empty(),pane(f'{toggles(False)}<div class="sh"><span>Sources in this conversation</span><span class="clr dim">Clear</span></div>{empty_card}','Research context','Coworker answers using everything listed here'),'research',0))
S['VBE-201a-My-Filings']=page('My Filings',wide(chat_empty(),pane(f'{searchbar("Search filings")}{list_rows(10)}','Primary Company Filings',"Showing your selected company's filings"),'filings'))
hc='<div class="helpcard info"><button class="close" aria-label="Close">'+i('x','ico xs')+'</button><p>Select a document to view it or hover and click on the icon add it to your research context to compare specific documents.</p><p style="margin:0">Switch top level company to change the documents you see here.</p></div>'
S['VBE-201b-My-Filings-Help']=page('My Filings — Help',wide(chat_empty(export_on=True),pane(f'{hc}{searchbar("Search filings")}{list_rows(9)}','Primary Company Filings',"Showing your selected company's filings",q=False),'filings'))
intro_cad=f'<div class="chatbody"><div class="tile" style="position:relative">{closex("close")}<span class="chip-ic teal">{i("bank")}</span><div class="info-sub">Welcome to Canadian Documents Search</div><div class="info" style="margin-top:6px"><p style="margin:0 0 8px">I can review a document against Canadian securities regulations, identify potential issues and recommend changes.</p><p style="margin:0">{{TAIL}}</p></div></div></div>'
def cad_chat(tail): return f'<div class="chatcol">{strip("Filings")}{intro_cad.replace("{TAIL}",tail)}{composer()}</div>'
letters=''.join(f'<b class="{"a" if c=="A" else ""}">{c}</b>' for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
cos=['A-LABS CAPITAL II CORP','A-LABS CAPITAL IV CORP','A.I.S. RESOURCES LTD','AIS.V','A2ZCRYPTOCAP INC','AZC.P.V','AAJ CAPITAL 3 CORP','AAAJ.P.V','AAPKI VENTURES INC','APKI.CN','AARDVARK 2 CAPITAL CORP','ABACUS MINING & EXPLORATION']
S['VBE-401aa-Filings-Search']=page('Search Canadian Filings',wide(cad_chat("To begin select a company then you'll be able to choose documents to analyse and compare."),pane(f'<div class="card2"><input class="field" placeholder="Find a Company" style="border-radius:6px"><div class="alpha">{letters}</div><div class="cos">{"".join(f"<div class=li>{c}</div>" for c in cos)}</div></div>','Search Canadian Filings',None),'cad',3))
S['VBE-401ab-Filings-Search']=page('Search Company Filings',wide(cad_chat('Select a document on the right to continue.'),pane(f'<div class="back">{i("arl","ico sm")}<span class="lnk" style="text-decoration:none">Switch companies</span></div>{searchbar("Search filings")}{list_rows(9,hov=2,inline=True)}','Search Australis Capital Inc Filings',None),'cad'))
doc=f'''<div class="back">{i("arl","ico sm")}<span>Exit document</span></div><div class="doc-card"><div class="tt">Form of Proxy - Annual General and Special Meeting <span class="d">17/12/2021</span></div><div class="ac">{i("plus","ico sm")}<span style="flex:1">Add Document to Context</span>{i("dl","ico sm")}{i("cmp","ico sm")}</div></div>
<div class="page"><div class="hd">AUSTRALIS CAPITAL INC.</div>{"".join('<div class="ln"></div>'*3+'<div class="ln s"></div>' for _ in range(8))}</div><div class="page">{"".join('<div class="ln"></div>'*4+'<div class="ln s"></div>' for _ in range(7))}</div>'''
chat411=f'<div class="chatcol">{strip("Filings")}<div class="chips" style="left:auto;right:12px;bottom:176px;align-items:flex-end"><span class="chip right">Summarize this filing</span><span class="chip right">Highlight key points from this filing</span></div><div style="position:absolute;left:12px;right:12px;bottom:132px" class="hint">Ask questions about the selected filing</div>{composer("Ask me anything about the selected filing…",actrow=False).replace("bottom:11px","")}</div>'
S['VBE-411a-Filing']=page('Filing',wide(chat411.replace('class="composer"','class="composer" style="bottom:12px"'),pane(doc,'Search Australis Capital Inc Filings',None),'cad'))
def comp_tile(body): return f'<div class="chatbody"><div class="tile" style="position:relative">{closex("close")}{body}</div></div>'
INTRO_C='<span class="chip-ic violet">'+i('gavel')+'</span><div class="info-sub">Welcome to Compliance review</div><div class="info" style="margin-top:6px"><p style="margin:0 0 8px">I can review a document against Canadian or US securities regulations, identify potential issues and recommend changes.</p><p style="margin:0">Review the page you have open or upload a document to get started.</p></div>'
chat501aa=f'<div class="chatcol">{strip("Compliance Review")}<div class="chatbody"><div class="tile" style="position:relative">{closex("close")}{INTRO_C}</div><div style="margin-top:22px"><button class="btn tile-btn" style="height:48px;margin-bottom:14px;justify-content:center">Check current URL for compliance</button><button class="btn tile-btn" style="height:48px;justify-content:center">Upload a document</button></div></div></div>'
how=f'<div class="helpcard info" style="padding:14px 40px 16px 16px"><button class="close" aria-label="Close">{i("x","ico xs")}</button><div class="info-sub" style="margin-bottom:12px">How it works</div><div class="info-sub" style="margin-bottom:6px">1. Choose what to review</div><p style="margin:0 0 18px">Review the page you have open, such as a draft in Google Docs, a news release or a filing, or upload a document.</p><div class="info-sub" style="margin-bottom:6px">2. Set the review options</div><p style="margin:0 0 18px">Choose Canada or the US, the regulation to check against, and the type of document.</p><div class="info-sub" style="margin-bottom:6px">3. Run the report</div><p style="margin:0">I\'ll identify potential issues and recommend changes. Your report appears on the right.</p></div><p class="muted" style="color:var(--muted);margin:22px 0 0 0">Review the page you have open or upload a document. Your report will appear here.</p>'
S['VBE-501aa-Compliance-In-Coworker']=page('Compliance — start',wide(chat501aa,pane(how,'Compliance Review',None,q=False),'compliance'))
srcchip=f'<div class="srcchip"><span class="g">{i("globe","ico")}</span><span><span class="t1">XXX Gold Receives Positive Record of De…</span><span class="t2">Reviewed source • NI 43-101 • Standards of disc…</span></span><button class="x" aria-label="Close" title="Remove reviewed source">{i("x","ico xs")}</button></div>'
def sel(t): return f'<div class="sel"><span>{t}</span>{i("chev")}</div>'
chat501ab=f'<div class="chatcol">{strip("Compliance Review")}<div class="chatbody">{srcchip}{sel("Country")}{sel("Regulation")}{sel("Document Type")}<button class="btn p" disabled>Run Report</button></div></div>'
S['VBE-501ab-Compliance-In-Coworker']=page('Compliance — options',wide(chat501ab,pane('<p style="color:var(--muted);margin:0 0 12px">Set the jurisdiction, regulation and document type, then run the review.</p><p style="color:var(--muted);margin:0">Your report will appear here.</p>','Compliance Review',None),'compliance'))
chat501bb=f'<div class="chatcol">{strip("Compliance Review","new report")}<div class="chatbody">{srcchip}{sel("Canada")}{sel("NP 51-201 - Disclosure Standards")}{sel("News Release")}<button class="btn p" disabled>Re-Run Report</button><div class="gen">Compliance Report Generated<br><button class="btn p">Export Report</button></div></div></div>'
rep=f'''<div class="report-h">Compliance Review Report</div>
<div class="find"><h4>Overly Promotional Language and Unbalanced Disclosure</h4><span class="risk high">High risk</span><div class="cite-l">NP 51-201, Section 2.1(2); CSA Staff Notice 51-356</div><p>The news release uses promotional and potentially unbalanced language, particularly in describing the South Railroad project as a <mark>'significant permitting milestone'</mark> that <mark>'unlocks next North American growth project,'</mark> and in statements such as 'Equinox Gold is… positioned as the new North American senior gold producer.' This may create an impression of certainty and success that is not fully supported by the underlying facts.</p><div class="refine"><b>Suggested refinement</b>: Replace promotional phrases with factual, neutral language. Avoid statements that imply certainty about future production or status as a <mark>'senior gold producer'</mark> unless supported by objective metrics. Ensure forward-looking statements are clearly identified and balanced with risks.</div></div>
<div class="find"><h4>Forward-Looking Information (FLI) – Cautionary Language and Assumptions</h4><span class="risk medium">Medium risk</span><div class="cite-l">NP 51-201, Section 2.1(2); NI 51-102, Part 4A.3</div><p>The news release contains extensive forward-looking information, but the cautionary language does not clearly identify the material factors and assumptions used to develop it.</p></div>'''
S['VBE-501bb-Compliance-In-Coworker']=page('Compliance — report',wide(chat501bb,pane(rep,'Compliance Review',None),'compliance'))
S['VBE-601a-Output-Centre']=page('Output Centre — empty',wide(chat_empty(),pane('<div class="helpcard info"><button class="close" aria-label="Close">'+i('x','ico xs')+'</button><p style="margin:0">Access, manage, and export all documents generated from your research and filing analysis.</p></div><p style="color:var(--muted);margin:16px 6px">You haven\'t created any reports yet.</p>','Output Centre',None,q=False),'output'))
def oc(t,d,tag=None):
    m=f'<div class="meta">{tag}<span>{d}</span></div>' if tag else f'<div class="meta"><span>{d}</span></div>'
    return f'<div class="li"><div>{t}</div>{m}</div>'
ocl=''.join([oc('Technical Report','09/03/2024',f'<span class="chtag violet">{i("gavel","ico xs")}Compliance</span>'),oc('Material Change Report','08/22/2024',f'<span class="chtag teal">{i("bank","ico xs")}SEDAR</span>'),oc('Certification of Interim Filings - CEO (E)','08/12/2024'),oc('Certification of Interim Filings - CFO (E)','08/12/2024'),oc('Management Discussion &amp; Analytics','08/12/2024'),oc('Statement of Executive Compensation','04/15/2024'),oc('Annual Report Analysis','03/31/2024')])
S['VBE-601b-Output-Centre']=page('Output Centre',wide(chat_empty(),pane(f'{searchbar("Search reports")}<div class="list oc">{ocl}</div>','Output Centre',None),'output'))
S['VBE-701a-History']=page('History — empty',wide(chat_empty(),pane('<div class="helpcard info"><button class="close" aria-label="Close">'+i('x','ico xs')+'</button><p style="margin:0">Access, manage, and export all your recent conversations with the Versance coworker.</p></div><p style="color:var(--muted);margin:16px 6px">You haven\'t had any conversations yet.</p>','Conversation History',None,q=False),'history'))
ans='''<div class="bubble-u"><span>Summarize</span></div><div class="ans"><p>Integra Resources announced additional results from its 2026 growth and expansion drilling program at the producing Florida Canyon Gold Mine in Nevada. The results identify several near-mine opportunities that could expand mineral resources, improve future mine planning and potentially extend the operation’s mine life. The targets are located within or immediately adjacent to existing pits, waste dumps and mine infrastructure, which may offer logistical and cost advantages compared with more distant exploration areas.</p><p>The company has completed 30,140 metres of reverse-circulation drilling at Florida Canyon in 2026. The program is focused primarily on near-surface, oxide gold mineralization that could potentially be incorporated into future resource, reserve and life-of-mine updates.</p><hr><p style="font-style:italic;margin:0">If you need a summary of the contents or specific details from this filing, please let me know.</p></div>'''
hist_rows=''.join(f'<div class="li"><div style="font-weight:500">Auto-generated chat title</div><div class="d">{d}</div></div>' for d in ['08/22/2024','08/12/2024','08/12/2024','08/12/2024','04/15/2024','03/31/2024'])
hist_first=f'<div class="li hov" style="background:#fff;border-radius:10px;position:relative;padding-right:40px"><div style="font-weight:500">Chat title auto-generated that you can edit by clicking on the edit icon on hover</div><div class="d">09/03/2024</div><span style="position:absolute;right:12px;top:12px;color:var(--muted)">{i("pen","ico sm")}</span></div>'
chat701b=f'<div class="chatcol">{strip()}<div class="chatbody">{ans}</div>{composer(send_on=False,export_on=True)}</div>'
S['VBE-701b-History']=page('History',wide(chat701b,pane(f'<input class="field" placeholder="Search conversations" style="height:44px;margin-bottom:12px"><div class="list stack">{hist_first}{hist_rows}</div>','Conversation History',None),'history'))


G={'VBE-101-Coworker':('Coworker (compact) — home, company switcher, how it works',['VBE-101a-Coworker-Small','VBE-101ab-Coworker-Switch','VBE-101ac-Coworker-Switch','VBE-101b-Coworker-About']),
 'VBE-102-Coworker-Backpack':('Research context — sources, add URL, empty',['VBE-102a-Coworker-Backpack','VBE-102aa-Coworker-Backpack-Add-URL','VBE-102s-Coworker-Backpack-Start']),
 'VBE-201-My-Filings':('Primary company filings — list, with help card',['VBE-201a-My-Filings','VBE-201b-My-Filings-Help']),
 'VBE-401-Filings-Search':('Filings search — pick a company, then its filings',['VBE-401aa-Filings-Search','VBE-401ab-Filings-Search']),
 'VBE-411-Filing':('Filing viewer',['VBE-411a-Filing']),
 'VBE-501-Compliance-In-Coworker':('Compliance review — start, options, report',['VBE-501aa-Compliance-In-Coworker','VBE-501ab-Compliance-In-Coworker','VBE-501bb-Compliance-In-Coworker']),
 'VBE-601-Output-Centre':('Output Centre — empty, list',['VBE-601a-Output-Centre','VBE-601b-Output-Centre']),
 'VBE-701-History':('Conversation History — empty, list with chat',['VBE-701a-History','VBE-701b-History'])}
import glob
for f in glob.glob(OUT+'VBE-*.html'): os.remove(f)
def label(k):
    num=k.split('-')[1]; rest=k.split('-',2)[2].replace('-',' ')
    return f"{num} {rest}"
CHATJS="<script>(function(){document.querySelectorAll('.inrow').forEach(function(r){var i=r.querySelector('.chat-in'),b=r.querySelector('.send-btn');if(!i||!b)return;function u(){b.disabled=!i.value.trim()}i.addEventListener('input',u);i.addEventListener('keydown',function(e){if(e.key==='Enter'&&!b.disabled)b.click()});b.addEventListener('click',function(){if(!b.disabled){i.value='';u()}});u()})})()</script>"

def add_vnav(html, g):
    """Neutral, style-independent navigation: screen list (top-left) + style switcher (bottom-left)."""
    html = re.sub(r'<nav class="nav-all"[^>]*>.*?</nav>', '<nav class="nav-all" style="display:none" aria-hidden="true"></nav>', html, flags=re.S)
    items = ''.join(f'<a href="{gg}.html#{k}" data-f="{gg}.html" data-s="{k}"><b>{label(k).split(" ",1)[0]}</b> {label(k).split(" ",1)[1]}</a>' for gg,(t,sts) in G.items() for k in sts)
    css = """<style id="vnav-css">
.vnav, .vnav * { box-sizing: border-box; }
html body .vnav { position: fixed; z-index: 2147483000; font: 12.5px/1.35 -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif; color: #111; background: #fff; border: 1px solid #D4D4D4; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,.12); text-transform: none; letter-spacing: 0; }
html body .vnav-col { position: fixed; z-index: 2147483000; top: 12px; left: 12px; bottom: 64px; width: 236px; display: flex; flex-direction: column; gap: 8px; pointer-events: none; }
html body .vnav-col .vnav { position: static; pointer-events: auto; }
html body .vnav-list { flex: 0 1 auto; min-height: 0; overflow: auto; padding: 8px 6px; }
html body .vnav-ds { flex: none; padding: 8px 6px; }
html body .vnav-ds a.ds { display: flex; justify-content: space-between; align-items: center; padding: 4px 8px; border-radius: 6px; color: #111; text-decoration: none; background: transparent; font-weight: 400; }
html body .vnav-ds a.ds span { color: #999; font-size: 11px; }
html body .vnav-ds a.ds:hover { background: #F0F0F0; }
html body .vnav h2 { margin: 2px 8px 6px; font: 600 11px/1.2 -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif; text-transform: uppercase; letter-spacing: .06em; color: #777; }
html body .vnav-list a { display: block; padding: 4px 8px; border-radius: 6px; color: #111; text-decoration: none; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; background: transparent; font-weight: 400; }
html body .vnav-list a b { display: inline-block; min-width: 34px; font-weight: 600; color: #777; font-variant-numeric: tabular-nums; }
html body .vnav-list a:hover { background: #F0F0F0; }
html body .vnav-list a.cur { background: #111; color: #fff; }
html body .vnav-list a.cur b { color: #BBB; }
html body .vnav-styles { left: 12px; bottom: 12px; display: flex; align-items: center; gap: 2px; padding: 4px; font-size: 14px; font-weight: 600; }
html body .vnav-styles a, html body .vnav-styles span { display: inline-flex; align-items: center; justify-content: center; min-width: 28px; height: 28px; border-radius: 7px; color: #111; text-decoration: none; background: transparent; }
html body .vnav-styles a:hover { background: #F0F0F0; }
html body .vnav-styles .off { color: #C4C4C4; cursor: default; }
html body .vnav-styles .num { min-width: 30px; font-variant-numeric: tabular-nums; }
</style>"""
    box = f'<div class="vnav-col"><nav class="vnav vnav-list" aria-label="All screens"><h2>All screens ({len(S)})</h2>{items}</nav><nav class="vnav vnav-ds" aria-label="Design system"><h2>Design system</h2><a class="ds" href="../design-system/specimen.html">specimen.html<span>page</span></a><a class="ds" href="../design-system/view-design-system.html">design-system.md<span>doc</span></a><a class="ds" href="../design-system/view-tokens.html">tokens.css<span>css</span></a><a class="ds" href="../design-system/view-components.html">components.css<span>css</span></a></nav></div><div class="vnav vnav-styles" role="navigation" aria-label="Switch style"><a data-dir="-1" href="#" aria-label="Previous style">&lsaquo;</a><span class="num" title="Current style">1</span><a data-dir="1" href="#" aria-label="Next style">&rsaquo;</a></div>'
    js = """<script id="vnav-js">(function(){try{sessionStorage.removeItem('dsReturn')}catch(e){}document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.vnav-ds a');if(a){try{sessionStorage.setItem('dsReturn','1')}catch(x){}}});var N=13,m=location.pathname.match(/style-v(\\d+)/),cur=m?+m[1]:1,file=location.pathname.split('/').pop();
if(/[?&]export/.test(location.search)){[].forEach.call(document.querySelectorAll('.vnav,.vnav-col'),function(e){e.style.display='none'});}
document.querySelector('.vnav-styles .num').textContent=cur;
function st(){var hash=location.hash||'';[].forEach.call(document.querySelectorAll('.vnav-styles a'),function(a){var n=cur+ +a.dataset.dir;if(n<1||n>N){a.className='off';a.removeAttribute('href');a.setAttribute('aria-disabled','true')}else{a.className='';a.href='../../style-v'+n+'/screens/'+file+hash;a.removeAttribute('aria-disabled')}});
var c=document.querySelector('.stage.on'),s=c&&c.dataset.state;[].forEach.call(document.querySelectorAll('.vnav-list a'),function(a){a.classList.toggle('cur',a.dataset.f===file&&a.dataset.s===s)})}
addEventListener('hashchange',function(){setTimeout(st,0)});st();setTimeout(st,0)})()</script>"""
    return html.replace('</body>', css + box + js + '</body>')
ALLNAV=''.join(f'<a href="{g}.html#{k}" data-f="{g}.html" data-s="{k}">{label(k)}</a>' for g,(t,sts) in G.items() for k in sts)
for g,(title,states) in G.items():
    stages=''.join(S[k].replace('@@STATE@@',k) for k in states)
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<link rel="stylesheet" href="screens.css"><script>(function(){{var t=new URLSearchParams(location.search).get('theme');try{{t=t||localStorage.getItem('vc-theme')}}catch(e){{}}if(t==='dark')document.documentElement.setAttribute('data-theme','dark')}})()</script><style>
.stage{{display:none}}.stage.on{{display:block}}
.nav-all{{position:fixed;top:12px;left:12px;z-index:50;width:268px;max-height:calc(100vh - 24px);overflow:auto;background:#fff;border:1px solid #D9DDE5;border-radius:12px;padding:8px 6px;font:13px/1.35 Figtree,sans-serif;box-shadow:0 2px 10px rgba(10,25,34,.08)}}
.nav-all h2{{margin:2px 8px 6px;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#8D96AA;font-weight:600}}
.nav-all a{{display:block;padding:4px 8px;border-radius:6px;color:#000;text-decoration:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.nav-all a:hover{{background:#EFF1FF}}.nav-all a.cur{{background:#E0E4FF;color:#324EFE;font-weight:600}}
</style></head>
<body>{stages}<nav class="nav-all" aria-label="All screens"><h2>All screens ({len(S)})</h2>{ALLNAV}</nav>
<script>(function(){{var s=[].slice.call(document.querySelectorAll('.stage')),f=location.pathname.split('/').pop();
function sh(){{var h=location.hash.slice(1),c=s[0];s.forEach(function(e){{if(e.dataset.state===h)c=e}});s.forEach(function(e){{e.classList.toggle('on',e===c)}});
[].forEach.call(document.querySelectorAll('.nav-all a'),function(a){{a.classList.toggle('cur',a.dataset.f===f&&a.dataset.s===c.dataset.state)}})}}
addEventListener('hashchange',sh);sh();document.addEventListener('click',function(e){{var b=e.target.closest('.themebtn');if(!b)return;var d=document.documentElement,n=d.getAttribute('data-theme')==='dark'?'light':'dark';d.setAttribute('data-theme',n);try{{localStorage.setItem('vc-theme',n)}}catch(x){{}}}});if(/export/.test(location.search)){{document.querySelector('.nav-all').style.display='none';document.documentElement.classList.add('export')}}}})()</script></body></html>'''
    html=html.replace('</body>',CHATJS+'</body>')
    html=add_vnav(html,g)
    open(OUT+g+'.html','w').write(html)
print(len(S),'states in',len(G),'files')
import runpy as _rp, os as _os
_vt=_os.path.join(OUT,'..','tools','viewers.py')
if _os.path.exists(_vt): _rp.run_path(_vt)['build'](_os.path.normpath(_os.path.join(OUT,'..')))
