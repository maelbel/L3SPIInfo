package AdventureGame;

import java.util.ArrayList;

public class Jeu {
	
	//Attributs
	private String titre;
	private static final int NB_JOUEUR_MAX = 6;
	private static final int NB_CASES = 50;
	private ArrayList<Joueur> listeJoueurs;
	private Case[] cases;
	private int nbEtapes;
	private int nbObstacles;
	private int scoreMax;
	
	//Constructeur
	public Jeu(String titre, int nbEtapes, int nbObstacles) {
		this.titre = titre;
		this.nbEtapes = nbEtapes;
		this.nbObstacles = nbObstacles;
		this.listeJoueurs = new ArrayList<Joueur>();
		this.cases = new Case[NB_CASES];
	}
	
	//Methodes
	public void ajouterJoueur(Joueur j) {
		listeJoueurs.add(j);
	}
	
	public ArrayList<Personnage> tousLesPersos() {
		ArrayList<Personnage> listeToutLesPersos = new ArrayList<Personnage>();
		ArrayList<Personnage> listePersos;
		
		for(Joueur j:listeJoueurs) {
			listePersos = j.getListPerso();
			for(Personnage perso:listePersos) {
				listeToutLesPersos.add(perso);
			}
		}
		
		return listeToutLesPersos;
	}
	
	public void initialiserCases() {
		int rand_gain;
		int nbObstacle = 0;
		
		for(Case c:cases) {
			rand_gain = (int)(Math.random() * NB_CASES) + 1;
			System.out.println(c);
			if(rand_gain %5 == 0 && nbObstacle <= nbObstacles) {
				c =  new Case(new Obstacle(rand_gain*2), rand_gain);
				nbObstacle = nbObstacle + 1;
			}else c = new Case(rand_gain);
		}
	}
	
	public void lancerJeu() {
		ArrayList<Personnage> listePersos = tousLesPersos();
		boolean placer;
		int compteur = 0;

		for(Personnage perso:listePersos) {
			System.out.println(cases[compteur]);
			placer = false;
			while(!placer) {
				if(cases[compteur].sansObstacle()) {
					placer = true;
				}else compteur += 1;
			}
			//placer le perso dans la case compteur
			cases[compteur].placerPersonnage(perso);
		}
	}
	
	public String afficherCases() {
		String message = "";
		int compteur = 0;
		
		for(Case c:cases) {
			message += "Case " + compteur + ": " + c.toString() + "\n";
			compteur += 1;
		}
		
		return message;
	}
	
	public String afficherParticipants() {
		String message = "LISTE DES JOUEURS \n";
		
		for (Joueur j:listeJoueurs) {
			message += "----------------------------\n"
					+ j.toString() + "\n"; 
		}
		
		return message;
	}
	public String afficherResultats(){
		afficherParticipants();
		String message = "JEU " + titre + "\n"
						+ "***********************************************"
						+ "RESULTATS\n"
						+ "";
		
		return message;
	}
}
