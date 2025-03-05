class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1; 
    }

    public void push(long e) {
        if (isFull()) {
            System.out.println("Pila Llena");
        } else {
            top++;
            arreglo[top] = e;
        }
    }

    public long pop() {
        if (isEmpty()) {
            System.out.println("Pila Vacía");
            return -1; 
        } else {
            long dato = arreglo[top];
            top--;
            return dato;
        }
    }

    public long peek() {
        if (isEmpty()) {
            System.out.println("Pila Vacía");
            return -1;
        } else {
            return arreglo[top];
        }
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }
    
    public static void main(String[] args) {
        Pila pila = new Pila(5);
            
        pila.push(10);
        pila.push(20);
        pila.push(30);

        System.out.println("Peek: " + pila.peek());
        System.out.println("Pop: " + pila.pop());

        System.out.println("¿Está vacía? " + pila.isEmpty());
        System.out.println("¿Está llena? " + pila.isFull());
    }
}



