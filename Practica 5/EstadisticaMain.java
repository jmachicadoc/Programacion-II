/**
* Clase Calcular Promedio y Desviacion Estandar.
*
* @author Joel Jesus Machicado Colque
* @version 1.0 
*
*/
import java.util.Locale;
import java.util.Scanner;

class Estadistica {
    private double[] numeros;
    public Estadistica(double[] numeros) {
        this.numeros = numeros;
    }
    public double promedio() {
        double suma = 0;
        for (double x_i : numeros) {
            suma = suma + x_i;
        }
        return suma / numeros.length;
    }
    public double desviacion() {
        double promedio = promedio();
        double suma = 0;
        int n = numeros.length;
        for (double x_i : numeros) {
            suma = suma + (Math.pow(x_i - promedio, 2));
        }
        return Math.sqrt(suma / (n - 1));
    }
}

public class EstadisticaMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.US); //Para ingresar con punto

        String[] valores = scanner.nextLine().split(" ");
        double[] numeros = new double[valores.length];

        for (int i = 0; i < valores.length; i++) {
            numeros[i] = Double.parseDouble(valores[i]);
        }

        Estadistica estadistica = new Estadistica(numeros);
        System.out.println("El promedio es " + estadistica.promedio());
        System.out.println("La desviación estándar es " + estadistica.desviacion());

        scanner.close();
    }
}
