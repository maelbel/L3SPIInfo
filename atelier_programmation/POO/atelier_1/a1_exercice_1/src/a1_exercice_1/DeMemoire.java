package a1_exercice_1;

public class DeMemoire extends Des{
	
	//Attribute
	private int lancePrecedent = 0;
	
	//Constructor
	public DeMemoire(String name, int nbFace) {
		super(name, nbFace);
	}
	
	//Method to throw the dice
	public int lancer() {
		
		int nbRandom = 0;
		do {
			nbRandom = super.lancer();
			System.out.println("Le lancé a fait: " + nbRandom + " et le lancé précédent était: " + lancePrecedent);
		}while(lancePrecedent == nbRandom);
		lancePrecedent = nbRandom;
		
		return nbRandom;
	}

}
