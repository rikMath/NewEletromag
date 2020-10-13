from campo import *

import matplotlib.pylab as plt
import numpy as np

cargas = [Carga(1, [-1, 0]), Carga(-1, [1, 0])]

x0, x1=-2, 2
y0, y1=-1.5, 1.5
x=np.linspace(x0, x1, 64)
y=np.linspace(y0, y1, 64)
x, y=np.meshgrid(x, y)
Ex, Ey=E_total(x, y, cargas)
# linhas de campo usando streamplot
color = 2 * np.log(np.hypot(Ex, Ey))
plt.streamplot(x,y,Ex,Ey,color=color, linewidth=1, cmap=plt.cm.inferno,)


#cargas pontuais
for C in cargas:
    if C.load>0:
        plt.plot(C.position[0],C.position[1],'bo',ms=8*np.sqrt(C.load))
    if C.load<0:
        plt.plot(C.position[0],C.position[1],'ro',ms=8*np.sqrt(-C.load))

plt.show()
