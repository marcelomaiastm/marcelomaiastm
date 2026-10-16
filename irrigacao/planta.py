import math, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Wedge, Circle, Rectangle
from matplotlib.path import Path
from matplotlib.patches import PathPatch

OUT = "/home/user/marcelomaiastm/irrigacao/planta-aspersores.png"
fig, ax = plt.subplots(figsize=(13, 19), dpi=130)
ax.set_aspect("equal"); ax.set_xlim(-1.5, 30.5); ax.set_ylim(-4.5, 38.5); ax.axis("off")

GR="#8bc34a"; CON="#e0a030"; PAV="#ece6c8"; CAN="#e75480"; HOU="#b0b0b0"; TK="#5b8fb9"
def poly(pts, fc, ec="#555", lw=0.8, z=1, alpha=1):
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=ec, lw=lw, zorder=z, alpha=alpha))
def txt(x, y, s, fs=9, **k):
    ax.text(x, y, s, fontsize=fs, ha="center", va="center", zorder=20, **k)

# pavimentos de fundo
poly([(0,-3.5),(24,-3.5),(24,37.5),(0,37.5)], PAV)
txt(12,-2.2,"VARANDA COBERTA  (depósito com quadro e controlador)",10,weight="bold")
txt(12,36.8,"CALÇADA DA FRENTE / RUA",9,weight="bold")
txt(23,18,"CALÇADA",8,rotation=90)
txt(10.5,31,"ENTRADA\nDE CARROS",8,color="#777")
# casa
poly([(7,10.5),(24,10.5),(24,26.1),(7,26.1)], HOU, z=2); txt(15.5,18.5,"CASA",16,weight="bold",color="#444")
# gramados
poly([(0,0),(7,0),(7,26.1),(7.9,36),(0,36)], GR, z=2)
poly([(9,0),(22,0),(22,10.5),(9,10.5)], GR, z=2)
# E (cunha com borda curva)
verts=[(11.6,26.1),(19.4,26.1),(18.2,31.6),(14.1,34.1),(12.6,33.8),(11.6,26.1)]
codes=[Path.MOVETO,Path.LINETO,Path.CURVE3,Path.CURVE3,Path.LINETO,Path.CLOSEPOLY]
ax.add_patch(PathPatch(Path(verts,codes),fc=GR,ec="#555",lw=0.8,zorder=2))
poly([(15.0,36),(22.2,36),(22.2,28.1)], GR, z=2)
# concregrama
poly([(0,-0.5),(22,-0.5),(22,0),(0,0)], CON, z=3)
poly([(7,0),(9,0),(9,10.5),(7,10.5)], CON, z=3)
poly([(9.8,8.5),(12.8,8.5),(12.8,10.5),(9.8,10.5)], CON, z=3)
# canteiros, caixa
poly([(13.3,10.1),(20.3,10.1),(20.3,10.5),(13.3,10.5)], CAN, z=3)
poly([(0.6,0),(1.6,0),(1.6,4),(0.6,4)], CAN, z=3)
poly([(0,4),(2,4),(2,6),(0,6)], TK, z=4)
txt(1,5,"CAIXA\n1000 L",6.5,color="white",weight="bold")
ax.add_patch(Rectangle((0.5,6.0),1.0,0.6,fc="#333",ec="black",zorder=16)); txt(1.0,6.3,"B",6,color="white",weight="bold")
txt(1.0,7.2,"bomba",7,weight="bold")
# rótulos de áreas
txt(3.6,15,"B\ngramado lateral\n7 × 36 m",10,weight="bold")
txt(15.5,4.6,"A  gramado dos fundos  13 × 10,5 m",10,weight="bold")
txt(16.8,11.0,"C canteiro 7 × 0,4 m",7)
txt(11.3,9.5,"F",8,weight="bold")
txt(8,5,"concregrama",6.5,rotation=90)
txt(11,-0.25,"faixa de concregrama 23 × 0,5 m",6.5)
txt(1.1,2.0,"G\nhorta",6.5,rotation=90,weight="bold")
txt(15.0,29.0,"E",11,weight="bold"); txt(20.6,33.4,"D",11,weight="bold")

# árvores
trees=[(2.4,30.6,1.6),(2.4,26.8,1.4),(2.5,23.3,1.2),(6.1,30.8,0.8),(4.3,5.4,1.5),(13.6,32.4,1.0),(14.8,29.6,0.9),(19.4,34.3,1.0)]
for x,y,r in trees:
    ax.add_patch(Circle((x,y),r,fc="#3d6b2a",ec="#2b4d1e",alpha=0.55,zorder=5))

zones = {
 "Z1":dict(name="Gramado B – fundos", color="#1f77b4", kind="MP3000"),
 "Z2":dict(name="Gramado B – frente", color="#17becf", kind="MP3000"),
 "Z3":dict(name="Gramado A – fundos", color="#9467bd", kind="MP3500"),
 "Z4":dict(name="Jardins da frente D + E", color="#ff7f0e", kind="MP2000"),
 "Z5":dict(name="Canteiro C (gotejo)", color="#d62728", kind="gotejo"),
 "Z6":dict(name="Horta G (gotejo)", color="#8c564b", kind="gotejo"),
 "Z7":dict(name="Árvores (anéis de gotejo)", color="#2ca02c", kind="gotejo"),
}
Q360={"MP2000":0.45,"MP3000":0.80,"MP3500":1.10}
heads=[
 # Z1 – MP3000 r7
 ("Z1",6.9,0,90,180,7),("Z1",1.8,0,0,90,7),("Z1",0,7.0,0,90,7),
 ("Z1",6.9,6,90,270,7),("Z1",6.9,12,90,270,7),("Z1",6.9,18,90,270,7),
 ("Z1",0,12,-90,90,7),("Z1",0,18,-90,90,7),
 # Z2 – MP3000 r7
 ("Z2",6.9,24,90,270,7),("Z2",7.4,30,95,275,7),("Z2",0,24,-90,90,7),("Z2",0,30,-90,90,7),
 ("Z2",0,36,-90,0,7),("Z2",7.8,36,180,270,7),
 # Z3 – MP3500 r10,6
 ("Z3",7.2,-0.5,0,90,10.6),("Z3",14.6,-0.5,0,180,9.4),("Z3",22,-0.5,90,180,10.6),
 ("Z3",7.2,10.5,-90,0,10.6),("Z3",14.6,10.1,180,360,9.4),("Z3",22,10.5,180,270,10.6),
 # Z4 – MP2000 (D)
 ("Z4",22.2,36,180,270,5.5),("Z4",18.6,36,180,360,4.5),("Z4",22.2,32,90,270,4.5),("Z4",18.6,32.05,-47.7,132.3,4.5),
 # Z4 – MP2000 (E)
 ("Z4",11.6,26.1,0,82.6,6),("Z4",15.5,26.1,0,180,5),("Z4",13.3,33.95,180,360,6.4),("Z4",17.6,30.6,123,303,4.5),
]
summary={}
for z,x,y,a1,a2,r in heads:
    c=zones[z]["color"]
    ax.add_patch(Wedge((x,y),r,a1,a2,fc=c,ec=c,alpha=0.10,lw=0.6,zorder=6))
    ax.plot(x,y,marker="o",ms=7,mfc=c,mec="black",mew=0.8,zorder=15)
    arc=(a2-a1)%360 or 360
    s=summary.setdefault(z,dict(n=0,arcs=[],q=0.0)); s["n"]+=1; s["arcs"].append(round(arc))
    s["q"]+=Q360[zones[z]["kind"]]*arc/360

pipes={
 "MAIN":[[(1.0,6.35),(2.3,6.35),(2.3,-0.2),(3.0,-0.2),(6.7,-0.2),(6.7,24.5)]],
 "Z1":[[(3.0,-0.3),(6.55,-0.3),(6.55,18)],[(3.0,-0.3),(2.45,-0.3),(2.45,6.5),(0.3,7.0),(0.3,18)]],
 "Z2":[[(6.55,24.5),(6.55,26.1),(7.6,35.8),(0.3,35.8),(0.3,24)],[(6.55,24.5),(6.55,24)]],
 "Z3":[[(3.0,-0.4),(22,-0.4),(22,10.4),(14.6,10.0)],[(7.4,-0.4),(7.4,10.4),(7.2,10.5)]],
 "Z4":[[(6.8,24.5),(6.8,27),(11.8,27)],[(11.8,26.3),(19.2,26.3)],[(11.8,27),(12.7,33.7),(13.5,33.9),(15.3,35.7),(18.6,32.05),(22.0,28.4),(22.0,35.8),(18.6,35.8)],[(16.5,26.3),(17.6,30.6)]],
 "Z5":[[(3.0,-0.45),(7.6,-0.45),(7.6,10.35),(13.3,10.35)],[(13.3,10.3),(20.3,10.3)]],
 "Z6":[[(3.0,-0.2),(1.1,-0.2),(1.1,0.1)],[(0.75,0.1),(1.45,0.1)],[(0.75,0.1),(0.75,3.9)],[(1.1,0.1),(1.1,3.9)],[(1.45,0.1),(1.45,3.9)]],
 "Z7":[[(6.85,24.5),(6.85,5.6),(5.8,5.4)],[(6.9,24.5),(6.9,26.1),(7.75,35.65),(0.45,35.65),(0.45,23.3)],[(0.45,30.6),(0.8,30.6)],[(0.45,26.8),(1.0,26.8)],[(0.45,23.3),(1.3,23.3)],[(7.3,30.8),(6.9,30.8)],[(6.85,27.1),(11.8,27.1),(13.1,31.5),(13.3,33.8),(15.3,35.6),(19.4,35.6),(19.4,35.3)],[(13.1,29.6),(13.9,29.6)]],
}
def plen(pl): return sum(math.dist(a,b) for a,b in zip(pl,pl[1:]))
lens={}
for k,pls in pipes.items():
    c="black" if k=="MAIN" else zones[k]["color"]
    lw=3.2 if k=="MAIN" else (2.0 if zones[k]["kind"]!="gotejo" else 1.4)
    ls="-" if k in ("MAIN",) or zones.get(k,{}).get("kind")!="gotejo" else (0,(3,1.5))
    for pl in pls:
        xs,ys=zip(*pl); ax.plot(xs,ys,color=c,lw=lw,ls=ls,zorder=10,solid_capstyle="round")
    lens[k]=round(sum(plen(p) for p in pls),1)
# anéis de gotejo nas árvores
for x,y,r in trees:
    ax.add_patch(Circle((x,y),0.8,fill=False,ec=zones["Z7"]["color"],lw=1.4,ls=(0,(3,1.5)),zorder=11))
# travessias sob o piso
for (x1,y1,x2,y2) in [(7.4,27.05,11.6,27.05),(14.1,34.4,15.3,35.6)]:
    ax.plot([x1,x2],[y1,y2],color="black",lw=7,alpha=0.25,zorder=9,solid_capstyle="butt")
txt(9.5,27.9,"travessia 1 (camisa)",6.5); txt(13.6,35.5,"travessia 2",6.5)
# caixas de válvulas
for (x,y,lab) in [(3.0,-0.3,"CV-A\nZ1 Z3 Z5 Z6"),(6.7,24.5,"CV-B\nZ2 Z4 Z7")]:
    ax.add_patch(Rectangle((x-0.6,y-0.45),1.2,0.9,fc="white",ec="black",lw=1.5,zorder=16))
    ax.text(x+0.8 if x>5 else x,y+(0 if x>5 else -1.25),lab,fontsize=7.5,weight="bold",zorder=21,
            ha="left" if x>5 else "center",va="center",bbox=dict(fc="white",ec="none",alpha=0.8))
# controlador / cabo
ax.add_patch(Rectangle((4.2,-3.2),1.6,1.0,fc="#ffd54f",ec="black",lw=1.2,zorder=16)); txt(5.0,-2.7,"CTRL",7,weight="bold")
ax.plot([5.0,5.0,3.0],[-2.2,-0.75,-0.75],color="purple",lw=1.2,ls=":",zorder=12)


# legenda lateral
lx=24.8; ly=37.6
ax.text(lx,ly,"LEGENDA",fontsize=12,weight="bold",va="top")
ly-=1.2
for z in zones:
    s=summary.get(z); zz=zones[z]
    ax.plot([lx,lx+0.9],[ly,ly],color=zz["color"],lw=3,ls="-" if zz["kind"]!="gotejo" else (0,(3,1.5)))
    line=f"{z} {zz['name']}"
    ax.text(lx+1.2,ly,line,fontsize=8,va="center",weight="bold")
    sub = (f"{s['n']} × {zz['kind']}  ·  ≈{s['q']:.1f} m³/h" if s else "tubo gotejador 16 mm")
    ax.text(lx+1.2,ly-0.55,sub,fontsize=7.5,va="center")
    ly-=1.45
ax.plot([lx],[ly],marker="o",ms=7,mfc="white",mec="black"); ax.text(lx+1.2,ly,"aspersor pop-up (PRS40) +\nbocal MP Rotator; leque = alcance",fontsize=7.5,va="center"); ly-=1.4
ax.plot([lx,lx+0.9],[ly,ly],color="black",lw=3.2); ax.text(lx+1.2,ly,"linha principal",fontsize=7.5,va="center"); ly-=0.9
ax.add_patch(Rectangle((lx,ly-0.3),0.9,0.6,fc="white",ec="black",lw=1.5)); ax.text(lx+1.2,ly,"caixa de válvulas",fontsize=7.5,va="center"); ly-=0.9
ax.plot([lx,lx+0.9],[ly,ly],color="purple",lw=1.2,ls=":"); ax.text(lx+1.2,ly,"cabo das válvulas",fontsize=7.5,va="center"); ly-=0.9
ax.add_patch(Circle((lx+0.45,ly),0.35,fill=False,ec="#2ca02c",ls=(0,(3,1.5)),lw=1.4)); ax.text(lx+1.2,ly,"anel de gotejo (árvore)",fontsize=7.5,va="center"); ly-=1.2
ax.text(lx,ly,"Nenhum aspersor no meio\ndo gramado: todos no\nperímetro (muro, piso,\nconcregrama, canteiros).",fontsize=7.5,va="top",style="italic")
# escala
ax.plot([24.8,29.8],[-3.5,-3.5],color="black",lw=2); [ax.plot([x,x],[-3.7,-3.3],color="black",lw=1.5) for x in (24.8,29.8)]
txt(27.3,-3.0,"5 m",8)
ax.set_title("Projeto de irrigação — planta de aspersores e setores (preliminar, escala aprox.)",fontsize=13,weight="bold")
plt.savefig(OUT,bbox_inches="tight"); print(json.dumps({"summary":summary,"lens":lens},ensure_ascii=False,indent=0))
