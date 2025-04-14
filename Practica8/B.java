package Practica8;
public class B {
    public int y;
    public int z;
    public B(int y, int z) {
        this.y = y;
        this.z = z;
    }
    public void incrementaYZ() {
        y++;
        z++;
    }
    public void incrementaZ() {
        z++;
    }
    public void mostrar() {
        System.out.println("B: y=" + y + ", Z=" + z);
    }
}
