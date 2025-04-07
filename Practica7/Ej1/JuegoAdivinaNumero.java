package Practica7.Ej1;
import java.util.Scanner;
import java.util.Random;
public class JuegoAdivinaNumero extends Juego {
    private int numeroAAdivinar;
    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas);
    }
    public void juega() {
        reiniciaPartida();
        Random random = new Random();
        numeroAAdivinar = random.nextInt(11);
        System.out.println("Adivina un número entre 0 y 10:");
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                int intento = scanner.nextInt();
            if (intento == numeroAAdivinar) {
                System.out.println("¡Acertaste!!");
                actualizaRecord();
                break;
            } else {
                boolean quedanVidas = quitaVida();
                if (!quedanVidas) {
                    System.out.println("Perdiste. El número era: " + numeroAAdivinar);
                    break;
                } else {
                    if (intento < numeroAAdivinar) {
                        System.out.println("El número es mayor. Intenta de nuevo:");
                    } else {
                        System.out.println("El número es menor. Intenta de nuevo:");
                        }
                    }
                }
            }
        }
    }
}
