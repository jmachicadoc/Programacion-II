# Clase Planta
class Planta:
    def __init__(self, nombre_cientifico, tipo_semilla, zona_climatica, tolerancia_climatica):
        self.nombre_cientifico = nombre_cientifico
        self.tipo_semilla = tipo_semilla
        self.zona_climatica = zona_climatica
        self.tolerancia_climatica = tolerancia_climatica  # 0 a 1

    def prospera_en(self, entorno):
        return entorno.zona == self.zona_climatica and entorno.nivel_compatibilidad() >= self.tolerancia_climatica

    def obtener_indice_adaptacion(self):
        return self.tolerancia_climatica * 100

# Clase Clima
class Clima:
    def __init__(self, temperatura_promedio, humedad, precipitacion, zona):
        self.temperatura_promedio = temperatura_promedio
        self.humedad = humedad
        self.precipitacion = precipitacion
        self.zona = zona

    def es_apto_para(self, planta):
        return planta.prospera_en(self)

    def variar_condiciones(self, nueva_temp, nueva_humedad, nueva_precipitacion):
        self.temperatura_promedio = nueva_temp
        self.humedad = nueva_humedad
        self.precipitacion = nueva_precipitacion

    def nivel_compatibilidad(self):
        # Valor simplificado: cuanto más cerca de 25°C, 70% humedad y 100mm lluvia, mejor.
        compat_temp = max(0, 1 - abs(25 - self.temperatura_promedio) / 25)
        compat_humedad = max(0, 1 - abs(70 - self.humedad) / 70)
        compat_lluvia = max(0, 1 - abs(100 - self.precipitacion) / 100)
        return (compat_temp + compat_humedad + compat_lluvia) / 3

# Clase BarreraGeografica
class BarreraGeografica:
    def __init__(self, tipo_barrera, region, intensidad_barrera, extension_km):
        self.tipo_barrera = tipo_barrera
        self.region = region
        self.intensidad_barrera = intensidad_barrera  # 0 a 1
        self.extension_km = extension_km

    def restringe_dispersion(self, planta):
        # Si la intensidad supera 0.7, se considera una barrera crítica
        return self.intensidad_barrera >= 0.7

    def evaluar_impacto(self):
        if self.intensidad_barrera >= 0.9:
            return "Alta restricción a la biodiversidad"
        elif self.intensidad_barrera >= 0.5:
            return "Restricción moderada"
        else:
            return "Barrera poco significativa"


# Plantas
p1 = Planta("Pimpinella Anisum", "semilla pequeña", "templado", 1)
p2 = Planta("Acacia senegal", "vaina", "seco", 0)
p3 = Planta("Papaver rhoeas", "cápsula", "alpino", 0)
    
# Climas
clima1 = Clima(22, 65, 90, "templado")
clima2 = Clima(35, 30, 40, "seco")
clima3 = Clima(10, 80, 120, "alpino")

# Barreras
b1 = BarreraGeografica("cordillera", "Andes", 0.85, 3000)
b2 = BarreraGeografica("océano", "Pacífico", 0.95, 12000)
b3 = BarreraGeografica("desierto", "Sahara", 0.6, 5000)

print("--- Prueba de Prosperidad en Climas ---")
for planta in [p1, p2, p3]:
    for clima in [clima1, clima2, clima3]:
        resultado = planta.prospera_en(clima)
        print(f"{planta.nombre_cientifico} en clima {clima.zona}: {'Prospera' if resultado else 'No prospera'}")

print("\n--- Evaluación de Barreras ---")
for barrera in [b1, b2, b3]:
    print(f"{barrera.tipo_barrera} en {barrera.region} → {barrera.evaluar_impacto()}")
    for planta in [p1, p2, p3]:
        restringe = barrera.restringe_dispersion(planta)
        print(f"  - ¿{planta.nombre_cientifico} restringida? {'Sí' if restringe else 'No'}")
