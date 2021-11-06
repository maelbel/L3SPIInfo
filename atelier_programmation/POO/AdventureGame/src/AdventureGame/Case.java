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
		this.perso = null;
	}
	public Case(int gain) {
		/*this.gain = gain;
		this.obs = null;
		this.perso = null;*/
		this(null, gain);
	}
	
	//Methode
	public int getPenalite() {
		int penalite = 0;
		if(obs!=null) penalite = obs.getPenalite();
		
		return penalite;
	}
	
	public void placerPersonnage(Personnage perso) {
		this.perso = perso;
	}
	
	public void placerObstacle(Obstacle obs) {
		this.obs = obs;
	}
	
	public void enleverPersonnage() {
		perso = null;
	}
	
	public boolean estLibre() {
		boolean libre = false;
		
		if(obs==null&&perso==null) libre = true;
				
		return libre;
	}
	
	public boolean sansObstacle() {
		boolean absent = false;
		if(obs==null) absent = true;
		return absent;
	}
	
	public boolean sansPerso() {
		boolean absent = false;
		if(perso==null) absent = true;
		return absent;
	}

	public String toString() {
		String message;
		if(estLibre()) message = "Libre (gain = " + gain + ")";
		else if(sansObstacle() == false) message = "Obstacle (penalité = " + getPenalite() + ")";
		else message = perso.toString() + "(penalité = " + -gain + ")";
		
		return message;
	}
}
