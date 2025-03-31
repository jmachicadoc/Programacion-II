public class AlgebraVectorial3D {
    private double x, y, z;
    public AlgebraVectorial3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    
    public AlgebraVectorial3D suma(AlgebraVectorial3D otro) {
        return new AlgebraVectorial3D(this.x + otro.x, this.y + otro.y, this.z + otro.z);
    }
    
    public AlgebraVectorial3D multiplicarEscalar(double r) {
        return new AlgebraVectorial3D(r * this.x, r * this.y, r * this.z);
    }
    
    public double longitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public AlgebraVectorial3D normalizar() {
        double magnitud = this.longitud();
        return new AlgebraVectorial3D(this.x / magnitud, this.y / magnitud, this.z / magnitud);
    }

    public double productoEscalar(AlgebraVectorial3D otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }

    public AlgebraVectorial3D productoVectorial(AlgebraVectorial3D otro) {
        return new AlgebraVectorial3D(
            this.y * otro.z - this.z * otro.y,
            this.z * otro.x - this.x * otro.z,
            this.x * otro.y - this.y * otro.x
        );
    }
    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }
    public static void main(String[] args) {
        AlgebraVectorial3D a = new AlgebraVectorial3D(3, -2, 5);
        AlgebraVectorial3D b = new AlgebraVectorial3D(1, 4, -3);

        System.out.println("Suma: " + a.suma(b));
        System.out.println("Multiplicación por escalar (2): " + a.multiplicarEscalar(2));
        System.out.println("Longitud de a: " + a.longitud());
        System.out.println("Vector normalizado de a: " + a.normalizar());
        System.out.println("Producto escalar a·b: " + a.productoEscalar(b));
        System.out.println("Producto vectorial a x b: " + a.productoVectorial(b));
    }
}
