package Practica7.Ej1;
public class Juego {
    private int numeroDeVidas;
    private int record;
    public Juego(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
        this.record = 0;
    }
    public void reiniciaPartida() {
        this.numeroDeVidas = 3;
    }
    public void actualizaRecord() {
        if (numeroDeVidas > record) {
            record = numeroDeVidas;
        }
    }
    public boolean quitaVida() {
        if (numeroDeVidas > 1) {
            numeroDeVidas--;
            System.out.println("Te quedan " + numeroDeVidas + " vidas.");
            return true;
        } else {
            System.out.println("No tienes más vidas.");
            return false;
        }
    }
}
