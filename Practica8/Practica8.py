class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    def incrementaXZ(self):
        self.x = self.x + 1
        self.z = self.z + 1
    def incrementaZ(self):
        self.z = self.z + 1
    def mostrar(self):
        print(f"A: x={self.x}, z={self.z}")

class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z
    def incrementaYZ(self):
        self.y = self.y + 1
        self.z = self.z + 1
    def incrementaZ(self):
        self.z = self.z + 1
    def mostrar(self):
        print(f"B: y={self.y}, z={self.z}")

class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)
    def incrementaXYZ(self):
        self.incrementaXZ()
        self.incrementaYZ()
    def mostrar(self):
        A.mostrar(self)
        B.mostrar(self)

d = D(1, 2, 3)
d.mostrar()
print("Incrementando XYZ...")
d.incrementaXYZ()
d.mostrar()
