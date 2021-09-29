package a3bis_exercice;

public class Proprietaire {
	protected String nom;
	private String adresse;
	
	public Proprietaire(String nom, String adresse) {
		this.nom = nom;
		this.adresse = adresse;
	}
	
	public String getNom() {
		return nom;
	}
	public String getAdresse() {
		return adresse;
	}
	public void setAdresse(String valeur) {
		adresse = valeur;
	}
	public String toString() {
		String message = nom + "(" + adresse + ")";
		return message;
	}
}