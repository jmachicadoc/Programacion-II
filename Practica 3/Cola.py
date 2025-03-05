class Cola:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
        self.elementos = 0

    def insert(self, e):
        if self.is_full():
            print("Cola Llena")
        else:
            self.fin = (self.fin + 1) % self.n  
            self.arreglo[self.fin] = e
            self.elementos += 1

    def remove(self):
        if self.is_empty():
            print("Cola Vacía")
            return None  
        else:
            dato = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n 
            self.elementos -= 1
            return dato

    def peek(self):
        if self.is_empty():
            print("Cola Vacía")
            return None  
        else:
            return self.arreglo[self.inicio]

    def is_empty(self):
        return self.elementos == 0

    def is_full(self):
        return self.elementos == self.n

    def size(self):
        return self.elementos

    def mostrar_cola(self):
        if self.is_empty():
            print("Cola Vacía")
        else:
            print("Cola:", [self.arreglo[(self.inicio + i) % self.n] for i in range(self.elementos)])

cola = Cola(5)

cola.insert(10)
cola.insert(20)
cola.insert(30)
cola.mostrar_cola()

print("Peek:", cola.peek())
print("Remove:", cola.remove())
cola.mostrar_cola()

print("¿Está vacía?", cola.is_empty())
print("¿Está llena?", cola.is_full())
print("Tamaño:", cola.size())
