import math
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return (self.x, self.y)
        
    def coord_polares(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return (f"Radio: {r}, Angulo: {theta}")
    
    def __str__(self):
        return f"Punto {self.x}, {self.y}"

p = Punto(3,4)
print("Cartesianas:", p.coord_cartesianas())  
print("Polares:", p.coord_polares())
print("Texto:", p.__str__())