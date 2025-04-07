package Practica7.Ej2;
import java.util.Scanner;
import java.util.Random;
class JuegoAdivinaNumero extends Juego {
    protected int numeroAAdivinar;
    private Scanner scanner = new Scanner(System.in);
    private Random random = new Random();
    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas);
    }
    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }
    public void juega() {
        reiniciaPartida();
        do {
            numeroAAdivinar = random.nextInt(11);
        } while (!validaNumero(numeroAAdivinar));
        System.out.println("Adivina un numero entre 0 y 10:");
        while (true) {
            int intento = scanner.nextInt();
            if (!validaNumero(intento)) {
                System.out.println("Numero invalido. Intenta de nuevo.");
                continue;
            }
            if (intento == numeroAAdivinar) {
                System.out.println("¡Acertaste!!");
                actualizaRecord();
                break;
            } else {
                boolean tieneVidas = quitaVida();
                if (!tieneVidas) {
                    System.out.println("Perdiste. El número era: " + numeroAAdivinar);
                    break;
                } else {
                    if (intento < numeroAAdivinar) {
                        System.out.println("El numero a adivinar es mayor.");
                    } else {
                        System.out.println("El numero a adivinar es menor.");
                    }
                    System.out.println("Intenta de nuevo:");
                }
            }
        }
    }
    
}
