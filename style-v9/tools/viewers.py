"""Builds the three design-system viewer pages (view-*.html) from tokens.css, components.css and
design-system.md in this style's design-system folder. Each page has a Back arrow and links to the
other design-system pages. Run automatically by gen.py."""
import os,re,html
BAR_CSS = """<style id="dsbar-css">
html body .dsbar{position:sticky;top:0;z-index:2147483000;display:flex;align-items:center;gap:6px;padding:8px 14px;background:#fff;border-bottom:1px solid #D4D4D4;font:13px/1.2 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;color:#111;text-transform:none;letter-spacing:0;box-shadow:0 1px 6px rgba(0,0,0,.06)}
html body .dsbar a,html body .dsbar button{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 10px;border:0;border-radius:7px;background:transparent;color:#111;text-decoration:none;font:inherit;cursor:pointer}
html body .dsbar a:hover,html body .dsbar button:hover{background:#F0F0F0}
html body .dsbar .back{font-weight:600;margin:0 6px 0 0;border:1px solid #D4D4D4}
html body .dsbar .sep{width:1px;height:18px;background:#D4D4D4;margin:0 6px}
html body .dsbar a.cur{background:#111;color:#fff}
html body .dsbar .ttl{margin-left:auto;color:#777;font-size:12px}
</style>"""
BAR_JS = """<script id="dsbar-js">(function(){var b=document.getElementById('dsback');if(!b)return;
var came=false;try{came=sessionStorage.getItem('dsReturn')==='1'}catch(e){came=history.length>1}
b.addEventListener('click',function(e){e.preventDefault();if(came&&history.length>1){history.back()}else{location.href=b.getAttribute('data-fallback')}});
[].forEach.call(document.querySelectorAll('.dsbar a:not(.back)'),function(a){a.addEventListener('click',function(e){e.preventDefault();location.replace(a.href)})})})()</script>"""
def bar(current,style_n,fallback="../screens/VBE-101-Coworker.html"):
    items=[('specimen.html','specimen.html','Specimen'),('view-design-system.html','design-system.md','design-system.md'),('view-tokens.html','tokens.css','tokens.css'),('view-components.html','components.css','components.css')]
    cur=' class="cur"'
    links=''.join('<a href="'+h+'"'+(cur if k==current else '')+'>'+t+'</a>' for h,k,t in items)
    arrow='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"/><path d="m12 19-7-7 7-7"/></svg>'
    return f'<div class="dsbar" role="navigation" aria-label="Design system pages"><a class="back" id="dsback" href="{fallback}" data-fallback="{fallback}" aria-label="Back">{arrow}Back</a><span class="sep"></span>{links}<span class="ttl">style v{style_n} · design system</span></div>'
def inline(s):
    s=html.escape(s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    return s
def md_to_html(md):
    lines=md.split('\n'); out=[]; i=0; para=[]; ul=False
    def flush():
        nonlocal para
        if para: out.append('<p>'+inline(' '.join(para))+'</p>'); para=[]
    def endul():
        nonlocal ul
        if ul: out.append('</ul>'); ul=False
    while i<len(lines):
        ln=lines[i]
        if ln.startswith('|') and i+1<len(lines) and re.match(r'^\|[\s:|-]+\|?\s*$',lines[i+1]):
            flush(); endul()
            head=[c.strip() for c in ln.strip().strip('|').split('|')]
            i+=2; rows=[]
            while i<len(lines) and lines[i].startswith('|'): rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i+=1
            out.append('<table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table>')
            continue
        m=re.match(r'^(#{1,4})\s+(.*)$',ln)
        if m: flush(); endul(); n=len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>')
        elif re.match(r'^\s*[-*]\s+',ln):
            flush()
            if not ul: out.append('<ul>'); ul=True
            out.append('<li>'+inline(re.sub(r'^\s*[-*]\s+','',ln))+'</li>')
        elif not ln.strip(): flush(); endul()
        else:
            endul(); para.append(ln.strip())
        i+=1
    flush(); endul()
    return '\n'.join(out)
PAGE="""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
{barcss}<style>
html,body{{margin:0;background:#fff;color:#111}}
.vw{{max-width:{maxw}px;margin:0 auto;padding:26px 20px 60px;font:15px/1.6 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif}}
.vw h1{{font-size:24px;margin:0 0 14px}} .vw h2{{font-size:18px;margin:30px 0 10px;padding-top:12px;border-top:1px solid #E4E4E4}} .vw h3{{font-size:15px;margin:22px 0 8px}}
.vw p{{margin:0 0 12px}} .vw ul{{margin:0 0 12px;padding-left:22px}} .vw li{{margin:3px 0}}
.vw code{{font:12.5px/1.4 ui-monospace,Menlo,Consolas,monospace;background:#F3F3F3;padding:1px 5px;border-radius:4px}}
.vw table{{border-collapse:collapse;width:100%;margin:6px 0 18px;font-size:13.5px}} .vw th,.vw td{{border-bottom:1px solid #E4E4E4;padding:6px 10px;text-align:left;vertical-align:top}} .vw th{{background:#FAFAFA;font-weight:600}}
.vw pre{{margin:0;font:12.5px/1.55 ui-monospace,Menlo,Consolas,monospace;white-space:pre;overflow:auto;tab-size:2}}
</style></head><body>{bar}<main class="vw">{body}</main>{barjs}</body></html>"""
def build(style_dir):
    n=int(re.search(r'style-v(\d+)',style_dir).group(1)); ds=os.path.join(style_dir,'design-system')
    md=open(os.path.join(ds,'design-system.md')).read()
    for fname,key,title,body,maxw in (
      ('view-design-system.html','design-system.md','design-system.md',md_to_html(md),900),
      ('view-tokens.html','tokens.css','tokens.css','<pre>'+html.escape(open(os.path.join(ds,'tokens.css')).read())+'</pre>',1100),
      ('view-components.html','components.css','components.css','<pre>'+html.escape(open(os.path.join(ds,'components.css')).read())+'</pre>',1100)):
        open(os.path.join(ds,fname),'w').write(PAGE.format(title=f'style v{n} · {title}',barcss=BAR_CSS,bar=bar(key,n),barjs=BAR_JS,body=body,maxw=maxw))
if __name__=='__main__':
    import sys
    for d in sys.argv[1:]: build(d)
