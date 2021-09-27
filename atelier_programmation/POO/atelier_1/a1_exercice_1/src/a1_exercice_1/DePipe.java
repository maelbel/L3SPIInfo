package a1_exercice_1;

public class DePipe extends Des{

	//Variables
	private final int borneMin;
	
	//Constructor
	public DePipe(String name, int nbFace, int borneMin) {
		super(name, nbFace); //Call of parent's constructor
		if (borneMin >= 1 && borneMin < nbFace) {
			this.borneMin = borneMin;
		} else {
			this.borneMin = 1;
		}
		nbDe++;
	}
	
	//Method to throw the dice
		public int lancer() {
			int nbRandom = borneMin + r.nextInt((nbFace + 1) - borneMin);
			
			return nbRandom;
		}
}
