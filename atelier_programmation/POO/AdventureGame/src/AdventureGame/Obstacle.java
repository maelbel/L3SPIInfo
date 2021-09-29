package AdventureGame;

public class Obstacle {

	//Attributs
	private int penalite;
	
	//Constructor
	/**
	 * Construction d'un obstacle
	 * @param penalite Représente la penalite a soustraire au point du joueur
	 */
	public Obstacle(int penalite) {
		this.penalite = penalite;
	}

	/**
	 * @return the penalite
	 */
	public int getPenalite() {
		return penalite;
	}
}