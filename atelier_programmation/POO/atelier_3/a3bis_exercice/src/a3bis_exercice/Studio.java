package a3bis_exercice;

public class Studio extends Appartement {

	private static final int LOYER_STUDIO = 300;
	
	public Studio(Proprietaire proprietaire) {
		super(proprietaire);
	}
	
	public double loyer() {
		return LOYER_STUDIO;
	}
	
	public String toString() {
		String message = "Studio " + super.toString();
		return message;
	}
	
}
