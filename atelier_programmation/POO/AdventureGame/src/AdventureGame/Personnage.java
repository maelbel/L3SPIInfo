package AdventureGame;

public abstract class Personnage {
	
	//Attributs
	protected String nom;
	protected int age;
	protected int position; 
	protected Joueur proprietaire;
	
	public Personnage(String nom, int age) {
		this.nom = nom;
		this.age = age;
	}
	
	public void deplacer(int destination, int gain) {
		position = destination;
		proprietaire.modifierPoints(gain);
	}
	
	public void penaliser(int penalite) {
		proprietaire.modifierPoints(penalite);
	}
	
	public String toString() {
		return nom;
	}
	
	public abstract int positionSouhaitee();

	/**
	 * @return the position
	 */
	public int getPosition() {
		return position;
	}

	/**
	 * @return the proprietaire
	 */
	public Joueur getProprietaire() {
		return proprietaire;
	}
}