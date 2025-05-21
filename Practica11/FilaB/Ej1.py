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

    def incrementar_precio(self, incremento):
        self.precio += incremento

class Pintura:
    def __init__(self, genero):
        self.genero = genero

class Obra(Pintura):
    def __init__(self, titulo, material, genero, artista1, artista2, anuncio):
        super().__init__(genero)
        self.titulo = titulo
        self.material = material
        self.artista1 = artista1
        self.artista2 = artista2
        self.anuncio = anuncio

    def get_artistas(self):
        return [self.artista1, self.artista2]

    def get_precio_venta(self):
        return self.anuncio.get_precio() if self.anuncio else 0

    def incrementar_precio_si_artista_es(self, nombre_artista, incremento):
        if self.artista1.get_nombre() == nombre_artista or self.artista2.get_nombre() == nombre_artista:
            self.anuncio.incrementar_precio(incremento)

    def __str__(self):
        return f"Título: {self.titulo}, Precio: {self.anuncio.get_precio()} Bs"

# Inciso a) Crear dos pinturas CON anuncios

# Artistas
a1 = Artista("Joel", "9922469", 6)
a2 = Artista("María", "654321", 9)
a3 = Artista("Pedro", "789456", 4)
a4 = Artista("Lucía", "321789", 7)

# Anuncios
an1 = Anuncio(1, 2000)
an2 = Anuncio(2, 3500)

# Pinturas con anuncios
pintura1 = Obra("Paisaje Andino", "Óleo", "Paisaje", a1, a2, an1)
pintura2 = Obra("Retrato Moderno", "Acrílico", "Retrato", a3, a4, an2)

# Inciso b) Calcular promedio de experiencia de los artistas de ambas pinturas

todos_los_artistas = pintura1.get_artistas() + pintura2.get_artistas()
total_experiencia = sum([art.get_experiencia() for art in todos_los_artistas])
promedio = total_experiencia / len(todos_los_artistas)

print("Promedio de experiencia de todos los artistas:", promedio, "años")

# Inciso c) Incrementar precio de la pintura si hay un artista con nombre X

nombre_buscado = "Joel"
incremento = 500

pintura1.incrementar_precio_si_artista_es(nombre_buscado, incremento)
pintura2.incrementar_precio_si_artista_es(nombre_buscado, incremento)
# Mostrar 
print(pintura1)
print(pintura2)
