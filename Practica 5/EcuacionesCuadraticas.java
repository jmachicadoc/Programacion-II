/**
* Clase Ecuaciones Cuadraticas.
*
* @author Joel Jesus Machicado Colque
* @version 1.0 
*
*/
import java.util.Scanner;

public class EcuacionesCuadraticas {
    private double a, b, c;

    public EcuacionesCuadraticas(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        return Math.pow(b, 2) - 4 * a * c;
    }

    public double getRaiz1() {
        double discriminante = getDiscriminante();
        if (discriminante >= 0) {
            return (-b + Math.sqrt(discriminante)) / (2 * a);
        }
        return Double.NaN;
    }

    public double getRaiz2() {
        double discriminante = getDiscriminante();
        if (discriminante > 0) {
            return (-b - Math.sqrt(discriminante)) / (2 * a);
        }
        return Double.NaN;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //ENTRADA
        System.out.print("Ingrese a, b, c: ");
        String[] valores = scanner.nextLine().split(" ");
        double a = Double.parseDouble(valores[0]);
        double b = Double.parseDouble(valores[1]);
        double c = Double.parseDouble(valores[2]);

        EcuacionesCuadraticas ecuacion = new EcuacionesCuadraticas(a, b, c);
        double discriminante = ecuacion.getDiscriminante();
        //SALIDA
        if (discriminante > 0) {
            System.out.println("La ecuacion tiene dos raices " + ecuacion.getRaiz1() + " y " + ecuacion.getRaiz2());
        } else if (discriminante == 0) {
            System.out.println("La ecuaion tiene una raiz " + ecuacion.getRaiz1());
        } else {
            System.out.println("La ecuacion no tiene raices reales");
        }
        scanner.close();
    }
}
