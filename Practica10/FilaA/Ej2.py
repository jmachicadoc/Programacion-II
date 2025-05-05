class LineaTeleferico:
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=4):
        self.__color = color
        self.__tramo = tramo
        self.__nroCabinas = nroCabinas
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [["pedro", "rojas", "luna"],
                            ["lucy", "sosa", "rios"],
                            ["ana", "perez", "rojas"],
                            ["saul", "arce", "calle"]]
        self.__edades = [35, 43, 26, 29]
        self.__sueldos = [2500.0, 3250.0, 2700.0, 2500.0]

    def __str__(self):
        cad = f"Color: {self.__color}, Tramo: {self.__tramo}, nroCabinas: {self.__nroCabinas}, nroEmpleados: {self.__nroEmpleados}\n"
        cad += "Empleados:\n"
        for i in range(len(self.__empleados)):
            cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}\n"
        return cad

    def eliminarPorApellido(self, x):
        for i in reversed(range(len(self.__empleados))):
            if self.__empleados[i][1] == x or self.__empleados[i][2] == x:
                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -= 1

    def __add__(self, datos):
        otro, nombre = datos
        for i in range(len(self.__empleados)):
            if self.__empleados[i][0] == nombre:
                otro.__empleados.append(self.__empleados[i])
                otro.__edades.append(self.__edades[i])
                otro.__sueldos.append(self.__sueldos[i])
                otro.__nroEmpleados += 1

                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -= 1
                break
        return otro

    def mostrarMayoresPorEdad(self):
        if not self.__edades:
            print("No hay empleados.")
            return
        mayor = max(self.__edades)
        print("Empleados con la mayor edad:")
        for i in range(len(self.__empleados)):
            if self.__edades[i] == mayor:
                print(f"{self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}")

    def mostrarMayoresPorSueldo(self):
        if not self.__sueldos:
            print("No hay empleados.")
            return
        mayor = max(self.__sueldos)
        print("Empleados con el mayor sueldo:")
        for i in range(len(self.__empleados)):
            if self.__sueldos[i] == mayor:
                print(f"{self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}")

# ==== Prueba de funcionamiento ====
if __name__ == "__main__":
    # Instanciación
    t1 = LineaTeleferico("Rojo", "Estación Central - 16 de Julio", 20, 4)
    t2 = LineaTeleferico("Verde", "Estación Irpavi - Estación Alto Obrajes", 15, 0)

    print("==== Teleférico 1 ====")
    print(t1)
    print("==== Teleférico 2 ====")
    print(t2)

    print("\nEliminando empleados con apellido 'rojas':")
    t1.eliminarPorApellido("rojas")
    print(t1)

    print("\nTransferir 'saul' de t1 a t2:")
    t1 + (t2, "saul")
    print("==== Teleférico 1 ====")
    print(t1)
    print("==== Teleférico 2 ====")
    print(t2)

    print("\nMostrar empleados con mayor edad en t2:")
    t2.mostrarMayoresPorEdad()

    print("\nMostrar empleados con mayor sueldo en t2:")
    t2.mostrarMayoresPorSueldo()
