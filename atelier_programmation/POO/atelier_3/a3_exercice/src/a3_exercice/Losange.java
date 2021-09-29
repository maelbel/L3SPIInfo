package a3_exercice;

public class Losange extends Geometrie2D {
    
	private double c;
	private double D;
	private double d;
	
    public Losange(String nom, double c, double D, double d) {
        super(nom);
        this.c = c;
        this.D = D;
        this.d = d;
    }

    @Override
    public double Surface() {
        double surface = (D*d)/2;
        return surface;
    }

    @Override
    public double Perimetre() {
        double perimetre = c * 4;
        return perimetre;
    }

    public String toString() {
        String message = "Vous venez de construire un losange"
                    	+ "\nSon Périmètre est de " + Perimetre() + "m"
                    	+ "\nSa surface est de " + Surface() + "m²";
        return message;
    }

}
