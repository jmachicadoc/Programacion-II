import javax.swing.*;
import java.awt.*;

public class Practica2 {

    // Clase Punto
    public static class Punto {
        public float x;
        public float y;

        public Punto(float x, float y) {
            this.x = x;
            this.y = y;
        }

        public String coord_cartesianas() {
            return "(" + x + ", " + y + ")";
        }

        public String coord_polares() {
            double r = Math.sqrt(x * x + y * y);
            double theta = Math.atan2(y, x);
            return ("Radio: " + r + " Angulo: " + theta);
        }

        public String toString() {
            return "Punto: " + x + ", " + y;
        }
    }

    // Clase Linea
    public static class Linea extends JPanel {
        public Punto p1;
        public Punto p2;

        public Linea(Punto p1, Punto p2) {
            this.p1 = p1;
            this.p2 = p2;
        }

        public String toString() {
            return "Linea desde " + p1 + " hasta " + p2;
        }

        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g;
            g2d.drawLine((int) p1.x + 50, (int) p1.y + 50, (int) p2.x + 50, (int) p2.y + 50);

        }

        public static void dibujaLinea(Punto p1, Punto p2) {
            JFrame frame = new JFrame("Dibujando una Línea");
            Linea panel = new Linea(p1, p2);
            frame.add(panel);
            frame.setSize(400, 400);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        }
    }

    // Clase Circulo
    public static class Circulo extends JPanel {
        public Punto centro;
        public float radio;

        public Circulo(Punto c, float r) {
            this.centro = c;
            this.radio = r;
        }

        public String toString() {
            return "Circulo con centro: " + centro + " y radio de: " + radio;
        }

        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g;
            int x = (int) (centro.x - radio);
            int y = (int) (centro.y - radio);
            int diametro = (int) (2 * radio);
            g2d.drawOval(x, y, diametro, diametro);
        }

        public static void dibujaCirculo(Punto centro, float radio) {
            JFrame frame = new JFrame("Dibujando un Círculo");
            Circulo panel = new Circulo(centro, radio);
            frame.add(panel);
            frame.setSize(2 * (int) radio + 100, 2 * (int) radio + 100);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        }
    }

    public static void main(String[] args) {
        // Crear puntos para los objetos
        Punto p1 = new Punto(0, 0);
        Punto p2 = new Punto(5, 5);
        Punto centro = new Punto(200, 200);

        // Crear y mostrar la linea
        Linea linea = new Linea(p1, p2);
        System.out.println(linea.toString());
        Linea.dibujaLinea(p1, p2);

        // Crear y mostrar el círculo
        Circulo circulo = new Circulo(centro, 150.0f);
        System.out.println(circulo.toString());
        Circulo.dibujaCirculo(centro, 150.0f);
    }
}
