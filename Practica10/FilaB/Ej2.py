class Ministerio:
    def __init__(self, nombre="", direccion=""):
        self.nombre = nombre
        self.direccion = direccion
        self.nro_empleados = 0
        self.empleados = []
        self.edades = []
        self.sueldos = []
        
        if nombre and direccion:
            self.agregar_empleado("pedro", "rojas", "luna", 35, 2500)
            self.agregar_empleado("lucy", "sosa", "rios", 43, 3250)
            self.agregar_empleado("ana", "perez", "rojas", 26, 2700)
            self.agregar_empleado("saul", "arce", "calle", 29, 2500)

    def agregar_empleado(self, nombre, paterno, materno, edad, sueldo):
        self.empleados.append((nombre, paterno, materno))
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nro_empleados += 1

    def eliminar_por_edad(self, edad_objetivo):
        i = 0
        while i < self.nro_empleados:
            if self.edades[i] == edad_objetivo:
                del self.empleados[i]
                del self.edades[i]
                del self.sueldos[i]
                self.nro_empleados -= 1
            else:
                i += 1

    def transferir_empleado(self, otro, nombre_empleado):
        for i in range(otro.nro_empleados):
            if otro.empleados[i][0] == nombre_empleado:
                self.empleados.append(otro.empleados[i])
                self.edades.append(otro.edades[i])
                self.sueldos.append(otro.sueldos[i])
                self.nro_empleados += 1
                # Eliminar del otro ministerio
                del otro.empleados[i]
                del otro.edades[i]
                del otro.sueldos[i]
                otro.nro_empleados -= 1
                break

    def mostrar_menor_edad(self):
        if not self.edades:
            print("No hay empleados.")
            return
        menor = min(self.edades)
        print(f"Empleados con menor edad ({menor}):")
        for i in range(self.nro_empleados):
            if self.edades[i] == menor:
                print(self.empleados[i], f"Edad: {self.edades[i]}")

    def mostrar_menor_sueldo(self):
        if not self.sueldos:
            print("No hay empleados.")
            return
        menor = min(self.sueldos)
        print(f"Empleados con menor sueldo ({menor}):")
        for i in range(self.nro_empleados):
            if self.sueldos[i] == menor:
                print(self.empleados[i], f"Sueldo: {self.sueldos[i]}")

    def __str__(self):
        info = f"Ministerio: {self.nombre}, Dirección: {self.direccion}\n"
        for i in range(self.nro_empleados):
            nom, pat, mat = self.empleados[i]
            info += f"Nombre: {nom} {pat} {mat}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        return info

# a) Instanciar de 2 formas
m1 = Ministerio()  # sin datos
m2 = Ministerio("Ministerio de Salud", "Av. Central #123") 

# b) Eliminar empleados con edad 29
m2.eliminar_por_edad(29)

# c) Transferir al empleado "ana" de m2 a m1
m1.transferir_empleado(m2, "ana")

# d) Mostrar menor edad y sueldo
m1.mostrar_menor_edad()
m2.mostrar_menor_sueldo()

# Imprimir estados finales
print(m1)
print(m2)
