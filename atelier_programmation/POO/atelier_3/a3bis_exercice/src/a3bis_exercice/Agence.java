package a3bis_exercice;

import java.util.ArrayList;

public class Agence {
	
	private String nom;
	private int nbApp;
	private ArrayList<Appartement> appartement;
	private static int nbAppTotal = 0;
	
	public Agence(String nom) {
		this.nom = nom;
		nbApp = 0;
		appartement = new ArrayList<Appartement>();
	}
	
	public void ajoutAppartement(Appartement a) {
		appartement.add(a);
		nbApp++;
		nbAppTotal++;
	}
	
	private double totalLoyer() {
		double somme = 0;
		
		//for(int i = 0; i < appartement.size() ; i++) {
		//	somme += appartement.get(i).loyer();
		//}
		for(Appartement a:appartement) {
			somme += a.loyer();
		}
		
		return somme;
	}
	
	public static int getNbAppTotal() {
		return nbAppTotal;
	}
	
	public String afficher() {
		String message = "AGENCE " + nom + " - " + nbApp + " appartements\n"
						+ "LISTE DES APPARTEMENTS";
		
		for(int i = 0; i < appartement.size() ; i++) {
			message += "\n" + appartement.get(i);
		}
		
		message += "\nTotal des loyers de l'agence " + totalLoyer() + " euros"; 
		
		return message;
	}
}
