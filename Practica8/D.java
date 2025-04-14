package Practica8;
public class D {
    private A a;
    private B b;
    public D(int x, int y, int z) {
        a = new A(x, z);
        b = new B(y, z);
    }
    public void incrementaXYZ() {
        a.incrementaXZ();
        b.incrementaYZ();
    }
    public void mostrar() {
        a.mostrar();
        b.mostrar();
    }
}
