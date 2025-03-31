public class AlgebraVectorial {
    private double x;
    private double y;
    public AlgebraVectorial(double x, double y) {
        this.x = x;
        this.y = y;
    }
    public boolean esPerpendicular(AlgebraVectorial otro) {
        return this.x * otro.x + this.y * otro.y == 0;
    }

    public boolean esParalelo(AlgebraVectorial otro) {
        return (this.x * otro.y - this.y * otro.x) == 0;
    }

    public AlgebraVectorial proyeccionSobre(AlgebraVectorial otro) {
        double productoPunto = this.x * otro.x + this.y * otro.y;
        double magnitudCuadrado = otro.x * otro.x + otro.y * otro.y;
        double escalar = productoPunto / magnitudCuadrado;
        return new AlgebraVectorial(escalar * otro.x, escalar * otro.y);
    }

    public double componenteEn(AlgebraVectorial otro) {
        double productoPunto = this.x * otro.x + this.y * otro.y;
        double magnitudOtro = Math.sqrt(otro.x * otro.x + otro.y * otro.y);
        return productoPunto / magnitudOtro;
    }

    public static void main(String[] args) {
        AlgebraVectorial v1 = new AlgebraVectorial(3, 4);
        AlgebraVectorial v2 = new AlgebraVectorial(-4, 3);
        System.out.println("Son perpendiculares? " + v1.esPerpendicular(v2));
        System.out.println("Son paralelas? " + v1.esParalelo(v2));
        AlgebraVectorial proyeccion = v1.proyeccionSobre(v2);
        System.out.println("Proyeccion de v1 sorbe v2: (" + proyeccion.x + ", " + proyeccion.y + ")");
        double componente = v1.componenteEn(v2);
        System.out.println("Componente de v1 en la direccion v2: " + componente);
    }
}
