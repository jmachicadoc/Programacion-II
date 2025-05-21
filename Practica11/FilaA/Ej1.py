class Artista:
    def __init__(self, nombre, ci, años_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.años_experiencia = años_experiencia

    def get_experiencia(self):
        return self.años_experiencia

    def get_nombre(self):
        return self.nombre


class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def get_precio(self):
        return self.precio


class Pintura:
    def __init__(self, genero):
        self.genero = genero


class Obra(Pintura):
    def __init__(self, titulo, material, genero, artista1, artista2, anuncio=None):
        super().__init__(genero)
        self.titulo = titulo
        self.material = material
        self.artista1 = artista1
        self.artista2 = artista2
        self.anuncio = anuncio

    def get_artista_mas_experimentado(self):
        if self.artista1.get_experiencia() > self.artista2.get_experiencia():
            return self.artista1
        else:
            return self.artista2

    def get_precio_venta(self):
        return self.anuncio.get_precio() if self.anuncio else 0

    def agregar_anuncio(self, anuncio):
        self.anuncio = anuncio


# Inciso a) Crear dos objetos pintura, uno con anuncio y otro sin anuncio

# Artistas
a1 = Artista("Carlos", "123456", 5)
a2 = Artista("Lucía", "654321", 8)
a3 = Artista("Ana", "789456", 4)
a4 = Artista("Miguel", "321789", 10)

# Anuncio para la primera pintura
anuncio1 = Anuncio(1, 2500)

# Pintura con anuncio
pintura1 = Obra("Atardecer", "Óleo", "Paisaje", a1, a2, anuncio1)

# Pintura sin anuncio
pintura2 = Obra("Retrato", "Acrílico", "Retrato", a3, a4)

# Inciso b) Mostrar el nombre del artista con más experiencia de ambas pinturas

experto1 = pintura1.get_artista_mas_experimentado()
experto2 = pintura2.get_artista_mas_experimentado()

print("Artista más experimentado de la pintura 1:", experto1.get_nombre())
print("Artista más experimentado de la pintura 2:", experto2.get_nombre())

# Inciso c) Agregar un anuncio a la pintura sin anuncio y mostrar el monto total de venta

# Nuevo anuncio
anuncio2 = Anuncio(2, 1800)
pintura2.agregar_anuncio(anuncio2)

# Calcular el total
total_venta = pintura1.get_precio_venta() + pintura2.get_precio_venta()
print("Monto total de venta de ambas pinturas:", total_venta, "Bs")
