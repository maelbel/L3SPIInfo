package AdventureGame;

/**
 * @author maelb
 *
 */
public class Tauren extends Personnage {

	//Attributs
	private int taille;
	
	public Tauren(String nom, int age, int taille) {
		super(nom, age);
		this.taille = taille;
	}
	
	@Override
	public int positionSouhaitee() {
		position = super.getPosition();
		int min = 1;
		int range = taille - min + 1;
		int rand = (int)(Math.random() * range) + min;
		return position + rand;
	}
	
	public String toString() {
		String message = "Tauren " + nom;
		return message;
	}
	
}
