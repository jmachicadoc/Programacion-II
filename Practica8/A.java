package Practica8;
public class A {
    public int x;
    public int z;
    public A (int x, int z) {
        this.x = x;
        this.z = z;
    }
    public void incrementaXZ(){
        x++;
        z++;
    }
    public void incrementaZ (){
        z++;
    }
    public void mostrar (){
        System.out.println("A: x=" + x + ", Z=" + z);
    }
}
