package a3bis_exercice;

public class MultiPiece extends Appartement{
	
	private static final double LOYER_PIECE = 200;
	private int nbPieces;
	
	public MultiPiece(Proprietaire proprietaire, int nbPieces) {
		super(proprietaire);
		this.nbPieces = nbPieces;
	}
	
	public double loyer() {
		return LOYER_PIECE*nbPieces;
	}
	public String toString() {
		String message = nbPieces + " pièces " + super.toString();
		return message;
	}
}
