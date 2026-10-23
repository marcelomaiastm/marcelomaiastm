import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Ellipse
OUT="/home/user/marcelomaiastm/irrigacao/casa-de-bombas.png"
fig,ax=plt.subplots(figsize=(14,10),dpi=130); ax.set_xlim(0,140); ax.set_ylim(-12,100); ax.axis("off")
P="#8a6d3b"; MET="#555"; W="#1565c0"
def box(x,y,w,h,label,fc="#fff",fs=8.5,n=None):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.4",fc=fc,ec="black",lw=1.2,zorder=5))
    ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=fs,zorder=6)
    if n: 
        ax.add_patch(Ellipse((x-2.2,y+h/2),4,4,fc="#c62828",ec="white",zorder=7))
        ax.text(x-2.2,y+h/2,str(n),color="white",ha="center",va="center",fontsize=8,weight="bold",zorder=8)
def pipe(pts,c=MET,lw=6,ls="-",z=2):
    xs,ys=zip(*pts); ax.plot(xs,ys,color=c,lw=lw,ls=ls,solid_capstyle="round",zorder=z)
# chão
ax.add_patch(Rectangle((0,-12),140,12,fc="#d7ccc8",ec="none")); ax.text(70,-6,"piso de concregrama + brita (dreno)  —  linha principal segue enterrada até a CV-A",ha="center",fontsize=9)
# caixa
ax.add_patch(Rectangle((4,0),42,62,fc="#64b5f6",ec="#0d47a1",lw=1.5,zorder=1)); ax.text(25,40,"CAIXA\n1000 L",ha="center",fontsize=14,weight="bold",color="#0d47a1")
ax.add_patch(Rectangle((4,0),42,8,fc="#a1887f",alpha=0.5,ec="none",zorder=1)); ax.text(25,4,"areia decanta aqui",ha="center",fontsize=7.5)
# entrada da 3000 L (existente)
pipe([(8,-12),(8,66),(14,66),(14,60)],c=P,lw=4); ax.text(9.5,70,"entrada vinda da caixa de 3000 L\n(existente, com boia)",fontsize=7.5)
# sucção
pipe([(46,12),(58,12)],c=MET); box(48,14,8,5,"registro\n1\"",fs=7,n=1); box(56,5,5,5,"união",fs=6.5,n=2)
ax.text(30,13.5,"saída a 10–15 cm do fundo\n(com crivo)",fontsize=7.5,ha="center")
# bomba
ax.add_patch(Rectangle((58,6),14,12,fc="#43a047",ec="black",zorder=4)); ax.add_patch(Rectangle((72,5),26,14,fc="#212121",ec="black",zorder=4))
ax.text(65,12,"bomba",color="white",fontsize=8,ha="center",zorder=6); ax.text(85,12,"motor FAMAC 3 cv\n(chumbar numa base,\n10 cm acima do chão)",color="white",fontsize=7.5,ha="center",zorder=6)
# recalque: sobe, passa sobre o motor
pipe([(66,18),(66,40),(104,40),(104,4),(104,-8)])
box(62.5,21,7,4,"união",fs=6.5,n=3)
box(59,30,14,6,"manômetro\n0–16 bar",fs=7,n=4)
# bypass
pipe([(80,40),(80,52),(40,52),(40,62)],c=W,lw=3,ls="--"); box(73,46,14,5,"registro globo 3/4\"\n(BYPASS ~2,5 m³/h)",fs=7,n=5)
ax.text(42,56,"retorno ao topo da caixa\n(longe da sucção)",fontsize=7.5,color=W)
# painel na parede
ax.add_patch(Rectangle((98,-1),30,45,fc="#efebe9",ec="#6d4c41",lw=1,zorder=0)); ax.text(113,44.5,"tábua fixada na parede (lado do muro)",fontsize=7.5,ha="center")
box(99,32,10,5,"filtro Y\nbronze",fs=7,n=6)
box(98,23,12,6,"VRP 1\"\nsaída 4,5 bar",fs=7.5,fc="#fff59d",n=7)
box(108,17,15,5,"manômetro 0–10 bar",fs=7,n=8)
box(108,10,16,5,"válv. alívio 6 bar",fs=7,fc="#ffcdd2",n=9)
pipe([(108,12.5),(126,12.5),(126,60),(46,60)],c=W,lw=2.5,ls=":")
ax.text(88,62,"descarga do alívio → topo da caixa",fontsize=7.5,color=W)
box(108,3,17,5,"pressostato 6,5 bar\n(corta a bomba)",fs=7,fc="#ffcdd2",n=10)
box(98.5,-2,11,4.5,"filtro disco 1\"",fs=7,n=11)
ax.text(106,-10.5,"registro geral 1\" + adaptador p/ PEAD 32 mm",fontsize=7.5)
ax.text(70,96,"Casa de bombas — montagem dentro do abrigo (esquema, sem escala)",ha="center",fontsize=13,weight="bold")
ax.text(70,91,"Tudo entre a bomba e a VRP (itens 3 a 7) em METAL PN16 (galvanizado ou bronze).  Depois da VRP: pressão ≤ 4,5 bar normal, ≤ 6 bar no máximo.",ha="center",fontsize=9)
ax.text(70,87,"Ordem de montagem: siga os números 1 a 11. Tudo com rosca + fita veda-rosca; uniões permitem tirar a bomba sem esvaziar a caixa.",ha="center",fontsize=9)
plt.savefig(OUT,bbox_inches="tight")
