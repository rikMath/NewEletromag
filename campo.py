class Carga(object):
    """
        Classe responsável por armazenar um objeto contendo informações de uma carga pontual
        Váriaveis armazenadas: Carga em coloumbs, posição em um campo cartesiano em metros do poto (0,0)
    """

    def __init__(self, load, position):

        self.load = load
        self.position = position #  Tupla de valores (X, Y)


class E_carga_pontual:
    def __init__(self, carga_coloumbs,position,x,y):
        self.carga_coloumbs = carga_coloumbs
        self.position = position
        self.x = x
        self.y = y


    def campo_x(self):
        # Cálculo campo eixo X
        return self.carga_coloumbs*(self.x-self.position[0])/((self.x-self.position[0])**2+(self.y-self.position[1])**2)**(1.5)

    def campo_y(self):
        # Cálculo campo eixo Y
        return self.carga_coloumbs*(self.y-self.position[1])/((self.x-self.position[0])**2+(self.y-self.position[1])**2)**(1.5)

    def all_campos(self):
        # Retorno do valor do campo no eixo X e Y
        return (self.campo_x(), self.campo_y())

# Campo Eletrico total
class E_total:
    # Superposição dos valores indivíduais dos campos em um campo total
    def __init__(self, x,y,cargas):
        self.Ex, self.Ey=0, 0
        for C in cargas:
            E = E_carga_pontual(C.load, C.position, x, y).all_campos()
            self.Ex=self.Ex+E[0]
            self.Ey=self.Ey+E[1]

    def get_campos_eixos(self):
        # Retorno dos valores do campo total nos eixos X e Y
        return (self.Ex, self.Ey)
