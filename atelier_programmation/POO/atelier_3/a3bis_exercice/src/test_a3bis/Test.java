package test_a3bis;

import a3bis_exercice.Proprietaire;
import a3bis_exercice.Appartement;
import a3bis_exercice.Studio;
import a3bis_exercice.MultiPiece;
import a3bis_exercice.Agence;

public class Test {
	
	public static void main(String[] args){
		Proprietaire proprietaire1 = new Proprietaire("De Miranda Lopes", "15 avenue des champs-élysées");
		System.out.println(proprietaire1);
		
		Appartement appart1 = new Studio(proprietaire1);
		System.out.println(appart1);
		System.out.println("Le loyer est de " + appart1.loyer() + "€");
		
		Appartement appart2 = new MultiPiece(proprietaire1, 3);
		System.out.println(appart2);
		System.out.println("Le loyer est de " + appart2.loyer() + "€");
		
		Agence agence = new Agence("MaelBell");
		agence.ajoutAppartement(appart1);
		agence.ajoutAppartement(appart2);
		System.out.println(agence.afficher());
	}
	
}
