class Pila:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.top = -1  

    def push(self, e):
        if self.isFull():
            print("Pila Llena")
        else:
            self.top += 1
            self.arreglo[self.top] = e

    def pop(self):
        if self.isEmpty():
            print("Pila Vacía")
            return None  
        else:
            dato = self.arreglo[self.top]
            self.top -= 1
            return dato

    def peek(self):
        if self.isEmpty():
            print("Pila Vacía")
            return None  
        else:
            return self.arreglo[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1

#Ver si la PILA es par se va a B si es impar a C
A = Pila(5)

A.push(13)
A.push(22)
A.push(7)

B = Pila(5) # Pares
C = Pila(5) # Impares

while not A.isEmpty():
    e = A.pop()
    if e % 2 == 0:
        B.push(e)
    else:
        C.push(e)

print("B...")
while not B.isEmpty():
    print(B.pop())

print("C...")
while not C.isEmpty():
    print(C.pop())
    

#/print("Peek:", A.peek())
#print("Pop:", A.pop())

#print("¿Está vacía?", A.isEmpty())
#print("¿Está llena?", A.isFull())
