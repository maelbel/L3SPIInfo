package AdventureGame;

public class Case {
	
	//Attributs
	private int gain;
	private Personnage perso;
	private Obstacle obs;
	
	//Constructeur
	public Case(Obstacle obs, int gain) {
		this.obs = obs;
		this.gain = gain;
	}
	public Case(int gain) {
		this.gain = gain;
		this.obs = null;
	}
	
	//Method
	public int getPenalite() {
		int penalite = 0;
		if(obs!=null) penalite = obs.getPenalite();
		
		return penalite;
	}
	
	public void placerPersonnage(Personnage perso) {
		
	}
	public void placerObstacle(Obstacle obs) {
		
	}
	public void enleverPersonnage() {
		perso = null;
	}
	public boolean estLibre() {
		libre = false;
		
		return libre;
	}
	public boolean sansObstacle() {
		
	}
	public boolean sansPerso() {
		
	}
	public String toString() {
		String message;
		if(estLibre()) message = "Libre (gain = " + gain + ")";
		else if(sansObstacle() == false) message = "Obstacle (penalité = " + getPenalite() + ")";
		else message = perso.toString() + "(penalité = " + -gain + ")";
	}
}
