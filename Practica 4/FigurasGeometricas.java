    //POLIMORFISMO 
    //SOBRE CARGA DE FUNCIONES
    public class FigurasGeometricas {
        double area(double radio) {
            return Math.PI * radio * radio; //Circulo
        }
        double area(double base_r, double altura_r) {
            return base_r*altura_r; //Rectangulo
        }
        double area(float base, float altura) {
            return base*altura / 2; //Triangulo rectangulo
        }
        double area(double base_mayor, double base_menor, double altura) {
            return (base_mayor+base_menor)*altura/2; //Trapecio
        }
        double area(float perimetro, int apotema) {
            return perimetro*apotema / 2; //Pentagono
        }
        public static void main(String[] args) {

            FigurasGeometricas f1 = new FigurasGeometricas();
            FigurasGeometricas f2 = new FigurasGeometricas();
            FigurasGeometricas f3 = new FigurasGeometricas();
            FigurasGeometricas f4 = new FigurasGeometricas();
            FigurasGeometricas f5 = new FigurasGeometricas();

            System.out.println("Circulo: " + f1.area(1));
            System.out.println("Rectangulo: " + f2.area(2d,3));
            System.out.println("Triangulo Rectangulo: " + f3.area(2F,3F));
            System.out.println("Trapecio: " + f4.area(2,2,5));
            System.out.println("Pentagono: " + f5.area(2F, 4));

        }

    }
