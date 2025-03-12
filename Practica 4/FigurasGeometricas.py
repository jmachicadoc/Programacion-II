#POLIMORFISMO 
#SOBRE CARGA DE FUNCIONES
import math
class FiguraGeometrica:
    def area(self, *args):
        # Círculo
        if len(args) == 1:  
            radio = args[0]
            return math.pi * radio * radio
        # Trapecio
        elif len(args) == 3:  
            base_mayor = args[0]
            base_menor = args[1]
            altura = args[2]
            return (base_mayor + base_menor) * altura / 2
        # Triángulo Rectángulo
        elif len(args) == 2:
            if isinstance(args[0], float) and isinstance(args[1], float):
                base = args[0]
                altura = args[1]
                return (base * altura) / 2
        # Pentágono
            elif isinstance(args[1], float):  
                perimetro = args[0]
                apotema = args[1]
                return (perimetro * apotema) / 2
        # Rectángulo
            else: 
                base = args[0]
                altura = args[1]
                return base * altura
        else:
            raise ValueError("Parámetros no válidos")

f1 = FiguraGeometrica()
f2 = FiguraGeometrica()
f3 = FiguraGeometrica()
f4 = FiguraGeometrica()
f5 = FiguraGeometrica()

print("Círculo:", f1.area(1))
print("Rectángulo:", f2.area(2, 3)) 
print("Triángulo Rectángulo:", f3.area(2.0, 3.0))  
print("Trapecio:", f4.area(2, 2, 5)) 
print("Pentágono:", f5.area(2, 4.0))  