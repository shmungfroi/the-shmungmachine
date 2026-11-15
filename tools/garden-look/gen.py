import sys,math,numpy as np,json,re,urllib.parse
src=open('/home/claude/garden/src/build.py').read()
a=src.index('# ---- crowns: a sacred-geometry'); b=src.index("CROWN_STYLE = os.environ")
code=src[a:b].replace('if R < 2.2: return g, c','if R < MINR: return g, c').replace('while y < P + FADE and r > .8:','while y < P + FADE*PEND and r > .8:').replace('while len(circles) < 160:','while len(circles) < MAXC:')
G={'math':math,'np':np,'os':__import__('os'),'GOLD':'#c9a24a','GOLD_HI':'#f0d48a','INK':'#0b0906','PRESENT':130.0,'MAXC':160,'PEND':1,'MINR':4.5}
exec(code,G)
MOD=[('daybreak','song','#9b7be8'),('pads','stage','#e0604d'),('keyboard','chamber','#e46d9c'),('synth','sacred','#3fb6a8'),
     ('sequencer','orch','#4d8fe0'),('mixer','commons','#6fbf5a'),('effects','concerto','#ec9640'),('guide','keyboard','#e0b44d')]
def enc(svg):
    svg=re.sub(r'\s+',' ',svg)
    return 'url("data:image/svg+xml,'+urllib.parse.quote(svg,safe=" =:/,.-;()'")+'")'
def crown(fig,col,w,maxc):
    G['MAXC']=maxc; P=130.0; x0=10
    body=G['crown3'](fig,x0,w,col)
    H=max(46,min(108,w*.58))
    vb=(x0-4,P-H-16,w+8,H+16+46)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]} {vb[1]:.1f} {vb[2]} {vb[3]:.1f}">{body}</svg>'
def tile(fig,col):
    R=34; W=R*2.1; H=W*math.sqrt(3)
    parts=[]
    for (x,y) in [(0,0),(W,0),(W/2,H/2),(0,H),(W,H)]:
        g,c=G['figure'](fig,x,y,R); parts.append((g,c))
    gd=''.join(''.join(g) for g,c in parts); cd=''.join(''.join(c) for g,c in parts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.1f}" height="{H:.1f}" viewBox="0 0 {W:.1f} {H:.1f}">'
            f'<path d="{gd}" fill="none" stroke="#c9a24a" stroke-width=".7"/><path d="{cd}" fill="none" stroke="{col}" stroke-width=".8"/></svg>'), W, H
css=[]; sizes={}; MX=int(sys.argv[1])
for tab,fig,col in MOD:
    G['PEND']=.55; sk=crown(fig,col,150,MX); t,W,H=tile(fig,col)
    sizes[tab]=(len(sk),len(t))
    css.append(f':root[data-theme="garden"]{{--gc-{tab}:{enc(sk)};--gt-{tab}:{enc(t)};--gt-{tab}-w:{W:.1f}px;--gt-{tab}-h:{H:.1f}px}}')
open('assets.css','w').write('\n'.join(css))
print(sizes, sum(len(x) for x in css))
