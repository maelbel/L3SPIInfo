package AdventureGame;

import java.util.ArrayList;

public class Joueur {
	
	//Attributs
	private String nom;
	private String code;
	private int nbJoueurs;
	private int nbPoints;
	private ArrayList<Personnage> listePersos;
	
	//Constructeur
	public Joueur(String nom) {
		this.nom = nom;
		nbJoueurs++;
		code = "J" + nbJoueurs;
		this.nbPoints = 0;
		this.listePersos = new ArrayList<Personnage>();
	}
	
	public void ajouterPersonnage(Personnage pers){
		listePersos.add(pers);
	}
	
	public int modifierPoints(int nb) {
		nbPoints = nbPoints + (nb);
		
		return nbPoints;
	}
	
	public boolean peutJouer() {
		boolean valide = true;
		
		if(listePersos.isEmpty()) valide = false;
		
		return valide;
	}
	
	public String toString() {
		//J1 Paul(15 points) avec 2 personnages
		String message = code + " " +  nom + "(" + nbPoints + " points)" + " avec " + listePersos.size() + " personnages";
		
		//Si le joueur n'a pas de personnage
		//J1 Paul (0 point) aucun personnage
		if(peutJouer() == false) message = code + " " +  nom + "(0 point)" + " aucun personnages";
		
		return message;
	}

	public ArrayList<Personnage> getListPerso() {
		return listePersos;
	}
}
