class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int elementos;

    public Cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.elementos = 0;
    }

    public void insert(long e) {
        if (isFull()) {
            System.out.println("Cola Llena");
        } else {
            fin = (fin + 1) % n; 
            arreglo[fin] = e;
            elementos++;
        }
    }

    public long remove() {
        if (isEmpty()) {
            System.out.println("Cola Vacía");
            return -1; 
        } else {
            long dato = arreglo[inicio];
            inicio = (inicio + 1) % n;  
            elementos--;
            return dato;
        }
    }

    public long peek() {
        if (isEmpty()) {
            System.out.println("Cola Vacía");
            return -1; 
        } else {
            return arreglo[inicio];
        }
    }

    public boolean isEmpty() {
        return elementos == 0;
    }

    public boolean isFull() {
        return elementos == n;
    }

    public int size() {
        return elementos;
    }

    public static void main(String[] args) {
        Cola cola = new Cola(5);
        
        cola.insert(10);
        cola.insert(20);
        cola.insert(30);

        System.out.println("Peek: " + cola.peek());
        System.out.println("Remove: " + cola.remove());

        System.out.println("¿Está vacía? " + cola.isEmpty());
        System.out.println("¿Está llena? " + cola.isFull());
        System.out.println("Tamaño: " + cola.size());
    }
    
}

