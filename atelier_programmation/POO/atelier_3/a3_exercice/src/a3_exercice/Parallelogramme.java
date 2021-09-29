package a3_exercice;

public class Parallelogramme extends Geometrie2D {
	
	private double a;
	private double b;
	private double hauteur;
	
	public Parallelogramme(String nom, double a, double b, double hauteur) {
		super(nom);
		this.a = a;
		this.b = b;
		this.hauteur = hauteur;
	}
	
	public double Surface() {
		double surface = b*hauteur;
		return surface;
	}
	
	public double Perimetre() {
		double perimetre = a + a + b + b;
		return perimetre;
	}
	
	public String toString() {
		String message = "Vous venez de construire un parallelogramme"
						+ "\nSon Périmètre est de " + Perimetre() + "m"
						+ "\nSa surface est de " + Surface() + "m²";
		return message;
	}
}
