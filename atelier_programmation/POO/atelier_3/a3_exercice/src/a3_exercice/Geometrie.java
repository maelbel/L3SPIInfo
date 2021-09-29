package a3_exercice;

public abstract class Geometrie {
	
	private String nom;
	private String identifiant;
	private static int nbGeometrie;
	
	public Geometrie(String nom) {
		this.nom = nom;
		nbGeometrie++;
		this.identifiant = nom + "_" + nbGeometrie;
	}
	
	public abstract double Surface();
	
	public String toString() {
		String message = "Construction d'une forme géométrique"
						+ "\n Son identifiant est " + identifiant;
		return message;
	}
}
