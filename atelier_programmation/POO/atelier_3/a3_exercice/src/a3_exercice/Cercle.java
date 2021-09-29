package a3_exercice;

public class Cercle extends Geometrie2D {
    
	private static final double PI = 3.14;
	private double rayon;
	
    public Cercle(String nom, double rayon) {
        super(nom);
        this.rayon = rayon;
    }

    @Override
    public double Surface() {
        double surface = Math.pow((PI*rayon), 2);
        return surface;
    }

    @Override
    public double Perimetre() {
        double perimetre = 2*PI*rayon;
        return perimetre;
    }

    public String toString() {
        String message = "Vous venez de construire un cercle"
                    	+ "\nSon Périmètre est de " + Perimetre() + "m"
                    	+ "\nSa surface est de " + Surface() + "m²"
                    	+ super.toString();
        return message;
    }

}

