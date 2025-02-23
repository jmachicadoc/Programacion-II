public class Practica1 {
    
    public static class Punto {
        public float x;
        public float y;
        
        public Punto(float x, float y){
            this.x = x;
            this.y = y;
        }
    
        public String coord_cartesianas(){
            return "(" + x +","+ y + ")";
        }
    
        public String coord_polares(){
            double r = Math.sqrt(x*x + y*y);
            double theta = Math.atan2(y,x);
            return ("Radio: "+ r +" Angulo: " + theta);
        }
        public String toString(){
            return ("Punto: " + x + ", " + y );
        }
        public static void main(String[] args){
            Punto p = new Punto(3, 4);
            System.out.println("Cartesianas: " + p.coord_cartesianas());
            System.out.println("Polares: " + p.coord_polares());
            System.out.println("Texto: " + p.toString());
        }
    }
}
