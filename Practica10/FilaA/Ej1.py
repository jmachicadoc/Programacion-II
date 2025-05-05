class ComunidadIndigena:
    def __init__(self, nombre, ubicacion, nivel_contaminacion, cantidad_poblacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__nivel_contaminacion = nivel_contaminacion
        self.__cantidad_poblacion = cantidad_poblacion

    def denunciar_contaminacion(self, nuevo_nivel):
        """Permite actualizar el nivel de contaminación registrado en la comunidad."""
        self.__nivel_contaminacion = nuevo_nivel

    def solicitar_compensacion(self):
        """Calcula un monto de compensación en base al nivel de contaminación y la población."""
        return self.__nivel_contaminacion * self.__cantidad_poblacion * 10

class EmpresaMinera:
    def __init__(self, nombre, tipo_mineria, ubicacion_operaciones, nivel_impacto_ambiental):
        self.__nombre = nombre
        self.__tipo_mineria = tipo_mineria
        self.__ubicacion_operaciones = ubicacion_operaciones
        self.__nivel_impacto_ambiental = nivel_impacto_ambiental

    def generar_contaminacion(self, aumento):
        """Aumenta el nivel de impacto ambiental de la empresa minera."""
        self.__nivel_impacto_ambiental += aumento

    def pagar_compensacion(self, monto):
        """Descuenta el monto de compensación de sus recursos (simulado con un print)."""
        print(f"{self.__nombre} paga Bs {monto} como compensación por daños ambientales.")


class Gobierno:
    def __init__(self, nombre_entidad, responsable, presupuesto_ambiental, plan_accion_contaminacion):
        self.__nombre_entidad = nombre_entidad
        self.__responsable = responsable
        self.__presupuesto_ambiental = presupuesto_ambiental
        self.__plan_accion_contaminacion = plan_accion_contaminacion
        self.__leyes_ambientales = ["Ley de Protección Ambiental", "Ley de Recursos Naturales"]

    def evaluar_comunidad(self, comunidad):
        """Evalúa si la comunidad requiere atención según su nivel de contaminación."""
        return comunidad._ComunidadIndigena__nivel_contaminacion > 5

    def emitir_regulacion(self, comunidad):
        """Emite una regulación si la comunidad está altamente contaminada."""
        if self.evaluar_comunidad(comunidad):
            return f"Regulación emitida por {self.__nombre_entidad} para proteger a la comunidad."
        return "No se requiere regulación por el momento."


comunidad = ComunidadIndigena("San Pedro", "Lago Poopó", 7, 120)
empresa = EmpresaMinera("Minera Andina", "Extracción de oro", "Oruro", 8)
gobierno = Gobierno("Ministerio de Medio Ambiente", "Lic. Rivera", 100000, "Plan Nacional de Mitigación 2025")

# Flujo de interacción
compensacion = comunidad.solicitar_compensacion()
empresa.pagar_compensacion(compensacion)
print(gobierno.emitir_regulacion(comunidad))
