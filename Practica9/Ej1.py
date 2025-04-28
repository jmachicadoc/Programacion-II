import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
# Definición de clases
class Boleto(ABC):
    def __init__(self, numero_boleto):
        self.__numero_boleto = numero_boleto
        self.__precio = 0.0

    @abstractmethod
    def mostrar_informacion(self):
        pass

    def get_numero_boleto(self):
        return self.__numero_boleto

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


class Palco(Boleto):
    def __init__(self, numero_boleto):
        super().__init__(numero_boleto)
        self.set_precio(100.0)

    def mostrar_informacion(self):
        return f"Numero: {self.get_numero_boleto()}, Precio: {self.get_precio()}"


class Platea(Boleto):
    def __init__(self, numero_boleto, dias_anticipacion):
        super().__init__(numero_boleto)
        if dias_anticipacion >= 10:
            self.set_precio(50.0)
        else:
            self.set_precio(60.0)

    def mostrar_informacion(self):
        return f"Numero: {self.get_numero_boleto()}, Precio: {self.get_precio()}"


class Galeria(Platea):
    def __init__(self, numero_boleto, dias_anticipacion):
        super().__init__(numero_boleto, dias_anticipacion)
        if dias_anticipacion >= 10:
            self.set_precio(25.0)
        else:
            self.set_precio(30.0)

    def mostrar_informacion(self):
        return f"Numero: {self.get_numero_boleto()}, Precio: {self.get_precio()}"

# Interfaz gráfica

def vender_boleto():
    try:
        numero = int(entrada_numero.get())
        tipo = tipo_boleto.get()

        if tipo == "Palco":
            boleto = Palco(numero)
        else:
            dias = int(entrada_dias.get())
            if tipo == "Platea":
                boleto = Platea(numero, dias)
            elif tipo == "Galeria":
                boleto = Galeria(numero, dias)
            else:
                messagebox.showerror("Error", "Seleccione un tipo de boleto válido.")
                return

        etiqueta_info.config(text=boleto.mostrar_informacion())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Teatro Municipal")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Título principal
titulo = tk.Label(ventana, text="Teatro Municipal", font=("Arial", 20, "bold"), fg="blue4")
titulo.pack(pady=10)

# Frame para datos del boleto
frame_datos = tk.LabelFrame(ventana, text="Datos del Boleto", padx=10, pady=10)
frame_datos.pack(padx=10, pady=10)

# RadioButtons para elegir tipo de boleto
tipo_boleto = tk.StringVar(value="Palco")

radiopalco = tk.Radiobutton(frame_datos, text="Palco", variable=tipo_boleto, value="Palco")
radioplatea = tk.Radiobutton(frame_datos, text="Platea", variable=tipo_boleto, value="Platea")
radiogaleria = tk.Radiobutton(frame_datos, text="Galeria", variable=tipo_boleto, value="Galeria")

radiopalco.grid(row=0, column=0, padx=5, pady=5)
radioplatea.grid(row=0, column=1, padx=5, pady=5)
radiogaleria.grid(row=0, column=2, padx=5, pady=5)

# Entrada para número de boleto
etiqueta_numero = tk.Label(frame_datos, text="Número:")
etiqueta_numero.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entrada_numero = tk.Entry(frame_datos)
entrada_numero.grid(row=1, column=1, padx=5, pady=5)

# Entrada para cantidad de días
etiqueta_dias = tk.Label(frame_datos, text="Cant. Días para el Evento:")
etiqueta_dias.grid(row=2, column=0, sticky="e", padx=5, pady=5)

entrada_dias = tk.Entry(frame_datos)
entrada_dias.grid(row=2, column=1, padx=5, pady=5)

# Botones de acción
boton_vende = tk.Button(ventana, text="Vende", command=vender_boleto, width=10)
boton_salir = tk.Button(ventana, text="Salir", command=salir, width=10)

boton_vende.pack(pady=5)
boton_salir.pack(pady=5)

# Etiqueta para mostrar la información
etiqueta_info = tk.Label(ventana, text="", font=("Arial", 15, "bold"), fg="blue4")
etiqueta_info.pack(pady=20)

ventana.mainloop()
