class Cola:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
        self.elementos = 0

    def insert(self, e):
        if self.isFull():
            print("Cola Llena")
        else:
            self.fin = (self.fin + 1) % self.n  
            self.arreglo[self.fin] = e
            self.elementos += 1

    def remove(self):
        if self.isEmpty():
            print("Cola Vacía")
            return None  
        else:
            dato = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n 
            self.elementos -= 1
            return dato

    def peek(self):
        if self.isEmpty():
            print("Cola Vacía")
            return None  
        else:
            return self.arreglo[self.inicio]

    def isEmpty(self):
        return self.elementos == 0

    def isFull(self):
        return self.elementos == self.n

    def size(self):
        return self.elementos


A = Cola(5)
A.insert(22)
A.insert(5)
A.insert(10)
A.insert(11)

B = Cola(5) # PRIMOS
C = Cola(5) # NO PRIMOS 

total = 100  

#CRIBA
criba = [True] * (total + 1)
criba[0] = criba[1] = False 

for i in range(2, int(total ** 0.5) + 1):
    if criba[i]:  
        for j in range(i * i, total + 1, i):
            criba[j] = False



while not A.isEmpty():
    e = A.remove()
    if criba[e]:  
        B.insert(e)
    else:
        C.insert(e)

print("B... PRIMOS")
while not B.isEmpty():
    print(B.remove())

print("C... NO PRIMOS")
while not C.isEmpty():
    print(C.remove())
