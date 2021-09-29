package AdventureGame;

import java.util.ArrayList;

import a3bis_exercice.Appartement;

public class Jeu {
	
	//Attributs
	private String titre;
	private static final int NB_JOUEUR_MAX = 6;
	private static final int NB_CASES = 50;
	private ArrayList<Joueur> listeJoueurs;
	private Case[] cases = new Case[NB_CASES];
	private int nbEtapes;
	private int nbObstacles;
	private int scoreMax;
	
	//Constructeur
	public Jeu(String titre, int nbEtapes, int nbObstacles) {
		this.titre = titre;
		this.nbEtapes = nbEtapes;
		this.nbObstacles = nbObstacles;
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
		
		for(Case c:cases) {
			rand_gain = (int)(Math.random() * NB_CASES) + 1;
			if(rand_gain%5==0) {
				c =  new Case(new Obstacle(rand_gain*2), rand_gain);
			}else c = new Case(rand_gain);
		}
	}
	public void lancerJeu() {
		ArrayList<Personnage> listePersos = tousLesPersos();
		
		for(int i = 0; i<listePersos.size(); i++) {
			if(cases[i].sansObstacle()) {
				listePersos.placerPersonnage();
			}else break;
		}
	}
}
