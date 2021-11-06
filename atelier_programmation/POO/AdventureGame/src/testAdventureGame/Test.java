package testAdventureGame;

import AdventureGame.Humain;
import AdventureGame.Jeu;
import AdventureGame.Joueur;
import AdventureGame.Tauren;

public class Test {

	public static void main(String[] args) {
		
		Jeu jeu = new Jeu("AtelierPoo", 4, 10);
		
		Joueur paul = new Joueur("Paul");
		
		Tauren hector = new Tauren("Hector", 15, 10);
		Humain jean = new Humain("Jean", 10);
		
		paul.ajouterPersonnage(hector);
		paul.ajouterPersonnage(jean);
		
		Joueur lucien = new Joueur("Lucien");
		
		Humain marie = new Humain("Marie", 10);
		Tauren hercule = new Tauren("Hercule", 20, 5);
		
		lucien.ajouterPersonnage(marie);
		lucien.ajouterPersonnage(hercule);
		
		jeu.ajouterJoueur(paul);
		jeu.ajouterJoueur(lucien);
		
		jeu.lancerJeu();
		
		jeu.afficherResultats();
	}
}
