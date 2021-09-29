package a3bis_exercice;

public abstract class Appartement {

	private static int nbAppartements = 0;
	private Proprietaire proprietaire;
	private String code;
	
	public Appartement(Proprietaire proprietaire) {
		this.proprietaire = proprietaire;
		nbAppartements++;
		this.code = "APP"+nbAppartements;
	}
	
	public abstract double loyer();
	
	public String toString() {
		String message = code + " appartenant à " + proprietaire;
		return message;
	}
}
