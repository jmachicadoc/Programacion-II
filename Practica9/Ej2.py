import tkinter as tk
import random
from abc import ABC, abstractmethod

# Definición de clases

class Coloreado(ABC):

    @abstractmethod
    def comoColorear(self):
        pass
class Figura(ABC):
    def __init__(self, color):
        self.__color = color
    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color
    def __str__(self):
        return f"Color: {self.getColor()}"
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados."

    def __str__(self):
        return f"Cuadrado - Lado: {self.lado}, {super().__str__()}"

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.1416 * self.radio

    def __str__(self):
        return f"Circulo - Radio: {self.radio}, {super().__str__()}"

# Funciones de la app

def generar_figuras():
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja"]
    figuras = []

    for _ in range(5):
        tipo = random.randint(1, 2)
        color = random.choice(colores)

        if tipo == 1:
            lado = random.randint(1, 10)
            figura = Cuadrado(lado, color)
        else:
            radio = random.randint(1, 10)
            figura = Circulo(radio, color)

        figuras.append(figura)

    return figuras

def mostrar_figuras():
    figuras = generar_figuras()
    salida_texto.delete("1.0", tk.END)

    for idx, figura in enumerate(figuras):
        salida_texto.insert(tk.END, f"Figura {idx+1}:\n")
        salida_texto.insert(tk.END, f"{figura}\n")
        salida_texto.insert(tk.END, f"Área: {figura.area():.2f}\n")
        salida_texto.insert(tk.END, f"Perímetro: {figura.perimetro():.2f}\n")

        if isinstance(figura, Coloreado):
            salida_texto.insert(tk.END, f"Cómo colorear: {figura.comoColorear()}\n")
        
        salida_texto.insert(tk.END, "-"*30 + "\n")

# Interfaz Gráfica

ventana = tk.Tk()
ventana.title("Coloreado")
ventana.geometry("500x500")
ventana.resizable(False, False)

titulo = tk.Label(ventana, text="Figuras Aleatorias", font=("Arial", 18, "bold"))
titulo.pack(pady=10)
boton_generar = tk.Button(ventana, text="Generar Figuras", command=mostrar_figuras, width=20, bg="lightblue")
boton_generar.pack(pady=10)
salida_texto = tk.Text(ventana, width=60, height=20)
salida_texto.pack(pady=10)
ventana.mainloop()
