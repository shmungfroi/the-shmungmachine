import re,sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read()
def rep(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:60],c); s=s.replace(a,b)
i=s.index('<style id="studio-pro-theme">'); j=s.index('</style>',i)
blk=s[i:j]; assert blk.count(':root[data-theme="pro"]')==3
blk=blk.replace(':root[data-theme="pro"]',':root[data-theme="pro"],:root[data-theme="garden"]')
css=open('/home/claude/gbuild/garden.css').read()+'\n'+open('/home/claude/gbuild/assets.css').read()
s=s[:i]+blk+'</style>\n<style id="garden-theme">\n'+css+'\n</style>'+s[j+len('</style>'):]
rep('themeOrder = ["pro",','themeOrder = ["garden","pro",')
rep('const themeLabels = {pro:"Studio",','const themeLabels = {garden:"Garden",pro:"Studio",')
rep('''    let savedTheme = "pro";
    try { savedTheme = localStorage.getItem("shmungThemeV2") || "pro"; } catch (_) {}''',
'''    let savedTheme = "garden";
    try { savedTheme = localStorage.getItem("shmungThemeV2") || "garden";
      /* EXP 0.3.20: Garden becomes the default Look, once, for anyone still on Studio */
      if(!localStorage.getItem("shmungGardenV1")){localStorage.setItem("shmungGardenV1","1");if(savedTheme==="pro"){savedTheme="garden";localStorage.setItem("shmungThemeV2","garden");}}
    } catch (_) {}''')
pro_btn=re.search(r'<button class="theme-choice" type="button" role="menuitemradio" aria-checked="false" data-theme-choice="pro">.*?</button>',s,re.S).group(0)
gb=pro_btn.replace('data-theme-choice="pro"','data-theme-choice="garden"').replace('<b>Studio</b>','<b>Garden</b>').replace(re.search(r'<small>[^<]*</small>',pro_btn).group(0),'<small>Warm black, gold line work, jewel modules</small>')
assert s.count(pro_btn)==2; s=s.replace(pro_btn,gb+'\n           '+pro_btn)
rep('<title>Shmung Machine — EXP 0.3.19 Studio','<title>Shmung Machine — EXP 0.3.20 Garden')
rep('SHMUNG MACHINE · EXP 0.3.19 STUDIO','SHMUNG MACHINE · EXP 0.3.20 GARDEN')
rep('<span>Shmung Machine · EXP 0.3.19 Studio','<span>Shmung Machine · EXP 0.3.20 Garden')
rep('theme-color" content="#18181b"','theme-color" content="#0b0906"')
rep('<!--\nEXP 0.3.19 — IPHONE','<!--\nEXP 0.3.20 — GARDEN LOOK (15 Nov 2026)\nNew default Look from the Garden of Earthly Sounds: warm black and gold, Outfit and Poiret One, each module a jewel colour;\nthe tab bar is a skyline of eight fractal crowns (one sacred-geometry figure per module); the module in view sets the page\nbackground: its figure as line work, its crown as a watermark, its colour as a wash. Studio and the other Looks are kept.\n\nEXP 0.3.19 — IPHONE')
k=s.rindex('</body>'); s=s[:k]+open('/home/claude/gbuild/garden.js').read()+'\n'+s[k:]
open(dst,'w').write(s); print('ok',len(s))
