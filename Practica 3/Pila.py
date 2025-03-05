class Pila:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.top = -1  

    def push(self, e):
        if self.is_full():
            print("Pila Llena")
        else:
            self.top += 1
            self.arreglo[self.top] = e

    def pop(self):
        if self.is_empty():
            print("Pila Vacía")
            return None  
        else:
            dato = self.arreglo[self.top]
            self.top -= 1
            return dato

    def peek(self):
        if self.is_empty():
            print("Pila Vacía")
            return None  
        else:
            return self.arreglo[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.n - 1

    def mostrar_pila(self):
        if self.is_empty():
            print("Pila Vacía")
        else:
            print("Pila:", self.arreglo[:self.top + 1])

pila = Pila(5)

pila.push(10)
pila.push(20)
pila.push(30)
pila.mostrar_pila()

print("Peek:", pila.peek())
print("Pop:", pila.pop())
pila.mostrar_pila()

print("¿Está vacía?", pila.is_empty())
print("¿Está llena?", pila.is_full())
