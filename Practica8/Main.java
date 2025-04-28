package Practica8;
public class Main {
    public static void main(String[] args) {
        D d = new D(1, 2, 3);
        d.mostrar();
        System.out.println("Incrementando XYZ...");
        d.incrementaXYZ();
        d.mostrar();
    }
}
/*Consideremos que en java no es posible 
directamente la herencia multiple en si, 
se puede usar interfaces pero con el problema 
dado no es posible ya que tiene constructores, 
y no puede tener atributos de instancia. */
