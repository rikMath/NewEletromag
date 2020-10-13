from campo import *

import matplotlib.pylab as plt
import numpy as np

cargas = []

print("Vamos começar a simulação\n")


#Adicionamos as cargas deixadas pelo Usuário
while True:
    carga = int(input("Digite quantos coloumbs possui a carga\n"))
    pos_x = int(input("Digite a posição no eixo X da carga\n"))
    pos_y = int(input("Digite a posição no eixo Y da carga\n"))
    cargas.append(Carga(carga, (pos_x, pos_y)))
    keep = input("Deseja adicionar outra carga? (s, n)\n")
    if keep == "n":
        break

"""
    As posições do gráfico são referentes as posiçoes das cargas deixadas pelo usuário
    O mínimo no eixo x é o valor mínimo que uma carga se situa no eixo x menos 1, assim como no eixo y
    O mesmo se aplica para o valor máximo para ambos os eixos
"""
x0, x1=min([c.position[0] for c in cargas]) - 1, max([c.position[0] for c in cargas]) + 1
y0, y1=min([c.position[1] for c in cargas]) - 1, max([c.position[1] for c in cargas]) + 1

# Funções referentes à criação de matrizes para as pposições de linhas de campo
x=np.linspace(x0, x1, 64)
y=np.linspace(y0, y1, 64)
x, y=np.meshgrid(x, y)

# Cálculo das cargas e plotagem no gráfico
Ex, Ey = E_total(x, y, cargas).get_campos_eixos()
color = 2 * np.log(np.hypot(Ex, Ey))
plt.streamplot(x,y,Ex,Ey,color=color, linewidth=1, cmap=plt.cm.inferno)


# Posicionamento das cargas pontuais no Gráfico
for C in cargas:
    if C.load>0:
        plt.plot(C.position[0],C.position[1],'bo',ms=8*np.sqrt(C.load))
    if C.load<0:
        plt.plot(C.position[0],C.position[1],'ro',ms=8*np.sqrt(-C.load))

plt.show()
