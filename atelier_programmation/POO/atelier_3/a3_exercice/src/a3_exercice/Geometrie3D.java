package a3_exercice;

public abstract class Geometrie3D extends Geometrie2D{

	public Geometrie3D(String nom) {
		super(nom);
	}
	
	public abstract double Volume();

}