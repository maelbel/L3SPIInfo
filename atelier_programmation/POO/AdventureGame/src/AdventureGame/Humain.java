package AdventureGame;

public class Humain extends Personnage{
	
	//Attributs
	private int nbDeplacements;
	private int niveau;
	
	public Humain(String nom, int age) {
		super(nom, age);
		nbDeplacements = 0;
		niveau = 1;
	}
	
	public void deplacer(int destination, int gain) {
		position = destination;
		getProprietaire().modifierPoints(gain);
		nbDeplacements++;
		if(nbDeplacements == 4) niveau = 2;
		else if(nbDeplacements == 6) niveau = 3;
	}

	@Override
	public int positionSouhaitee() {
		position += niveau * nbDeplacements;

		return position;
	}
	
	public String toString() {
		String message = "Humain " + nom;
		return message;
	}
}
