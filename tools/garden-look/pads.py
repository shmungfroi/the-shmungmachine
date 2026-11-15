import math,urllib.parse,json
C=50;R=40
def P(r,a): return (C+r*math.cos(a),C+r*math.sin(a))
def circ(x,y,r): return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}"/>'
def dot(x,y,r=2.6): return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="#000" stroke="none"/>'
def poly(pts,close=True): return '<path d="M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in pts)+(' Z' if close else '')+'"/>'
def star(n,k,r=R*.92): 
    pts=[P(r,-math.pi/2+2*math.pi*i/n) for i in range(n)]
    seen=set();out=[]
    for s in range(math.gcd(n,k)):
        i=s;seq=[]
        while i not in seen: seen.add(i);seq.append(pts[i]);i=(i+k)%n
        out.append(poly(seq))
    return ''.join(out)
def tri_dots(rows,size=R*.95):
    out=[];h=size*1.6/(rows)
    for r in range(rows):
        for c in range(r+1):
            x=C+(c-r/2)*h; y=C-size*.62+r*h*.87+ (h*.1)
            out.append(dot(x,y,2.4 if rows>4 else 3))
    return ''.join(out)
F={}
F[1]=circ(C,C,R)+dot(C,C,4)
F[2]=circ(C,C,R)+circ(C-R*.3,C,R*.6)+circ(C+R*.3,C,R*.6)
F[3]=circ(C,C,R)+poly([P(R,-math.pi/2+2*math.pi*i/3) for i in range(3)])+circ(C,C,R*.5)
F[4]=circ(C,C,R)+poly([P(R,-math.pi/4+math.pi/2*i) for i in range(4)])+circ(C,C,R*.707)+poly([P(R*.707,math.pi/2*i) for i in range(4)])
F[5]=circ(C,C,R)+star(5,2)
F[6]=circ(C,C,R)+''.join(circ(*P(R/2,math.pi/3*i),R/2) for i in range(6))
F[7]=circ(C,C,R)+circ(C,C,R/2)+''.join(circ(*P(R/2,math.pi/3*i-math.pi/2),R/2) for i in range(6))
F[8]=circ(C,C,R)+star(8,3)
F[9]=circ(C,C,R)+star(9,4)
F[10]=circ(C,C,R)+tri_dots(4)
F[11]=circ(C,C,R)+star(11,4)
F[12]=circ(C,C,R)+''.join(circ(*P(R/2,math.pi/6*i),R/2) for i in range(12))
r=R/6.2; pts=[(C,C)]+[P(2*r,math.pi/3*i-math.pi/2) for i in range(6)]+[P(4*r,math.pi/3*i-math.pi/2) for i in range(6)]
F[13]=circ(C,C,R)+''.join(circ(x,y,r) for x,y in pts)+poly(pts[7:])
F[14]=circ(C,C,R)+star(14,5)
F[15]=circ(C,C,R)+tri_dots(5)
g=R*.34; F[16]=circ(C,C,R)+''.join(f'<rect x="{C-1.5*g+i*g-g*.36:.2f}" y="{C-1.5*g+j*g-g*.36:.2f}" width="{g*.72:.2f}" height="{g*.72:.2f}" rx="1.5"/>' for i in range(4) for j in range(4))
svgs={n:f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="none" stroke="#000" stroke-width="1.6" stroke-linejoin="round">{b}</g></svg>' for n,b in F.items()}
css=[]
for n,sv in svgs.items():
    u='url("data:image/svg+xml,'+urllib.parse.quote(sv,safe=" =:/,.-;()'")+'")'
    css.append(f':root[data-theme="garden"] .pad[data-pad="{n-1}"]{{--pfig:{u}}}')
open('pads_assets.css','w').write('\n'.join(css))
# contact sheet
names={1:'Monad',2:'Vesica',3:'Triad',4:'Tetrad',5:'Pentagram',6:'Rosette',7:'Seed of life',8:'Octagram',9:'Enneagram',10:'Tetractys',11:'Hendecagram',12:'Rose',13:"Metatron",14:'Star of 14',15:'Triangle of 15',16:'The grid'}
cols=['#e0604d']*4+['#ec9640']*4+['#4d8fe0']*4+['#9b7be8']*4
cells=''.join(f'<div class="c"><div class="f" style="background:{cols[n-1]};-webkit-mask:url(\'data:image/svg+xml,{urllib.parse.quote(svgs[n])}\') center/contain no-repeat"></div><b>{n:02d}</b><span>{names[n]}</span></div>' for n in range(1,17))
open('sheet.html','w').write(f'''<html><head><style>@font-face{{font-family:P;src:url(file:///home/claude/garden/fonts/PoiretOne-Regular.ttf)}}@font-face{{font-family:O;src:url(file:///home/claude/garden/fonts/Outfit-Regular.ttf)}}
body{{margin:0;background:#0b0906;color:#ece2c8;font-family:O;padding:36px}}h1{{font-family:P;font-weight:400;letter-spacing:.3em;font-size:22px;margin:0 0 24px;color:#f0d48a}}
.g{{display:grid;grid-template-columns:repeat(4,200px);gap:14px}}.c{{background:#12100b;border:1px solid #2a2418;border-radius:4px;padding:14px;height:190px;display:flex;flex-direction:column;align-items:center;justify-content:space-between}}
.f{{width:120px;height:120px}}b{{font-size:12px;color:#9c927c;letter-spacing:.1em}}span{{font-family:P;letter-spacing:.18em;text-transform:uppercase;font-size:12px;margin-top:-14px}}</style></head>
<body><h1>THE SIXTEEN PADS · THE NUMBER MADE VISIBLE</h1><div class="g">{cells}</div></body></html>''')
print('ok')
