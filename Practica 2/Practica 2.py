import math
import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return (self.x, self.y)
        
    def coord_polares(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return (r, theta)
    
    def __str__(self):
        return f"Punto {self.x}, {self.y}"
    

class Linea:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Linea desde {self.p1} hasta {self.p2}"
    
    def dibujeLinea(self):
        plt.plot([self.p1, self.p2], [self.p1, self.p2], marker='o', linestyle='-')
        plt.show()

class Circulo:
    def __init__(self, c: Punto, r: float):
        self.centro = c
        self.radio = r

    def __str__(self):
        return f"Circulo con centro {self.centro} y radio de {self.radio}"
    
    def dibujaCirculo(self):
        centro = (self.centro.x, self.centro.y)
        radio = self.radio
        
        fig, ax = plt.subplots()
        
        circulo = plt.Circle(centro, radio, color='b', fill=False)
        
        ax.add_patch(circulo)

        ax.scatter(self.centro.x, self.centro.y, color='r', s=10, label="Centro")

        ax.set_xlim(centro[0] - radio - 1, centro[0] + radio + 1)
        ax.set_ylim(centro[1] - radio - 1, centro[1] + radio + 1)

        ax.set_aspect('equal')

        plt.show()

#Salida Punto
p1 = (0,0)
p2 = (5,5)
linea = Linea(p1,p2)
print(linea)
linea.dibujeLinea()

#Salida Circulo
p = Punto(5,5)
circulo = Circulo(p, 3)
print(circulo)
circulo.dibujaCirculo()   