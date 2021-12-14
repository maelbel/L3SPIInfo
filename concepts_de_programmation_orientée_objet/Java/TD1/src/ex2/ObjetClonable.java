package ex2;

import java.lang.CloneNotSupportedException;

public class ObjetClonable implements Cloneable{
	
	public int i = 1;
    private Mere mere = new  Mere(i, "Mere");
    private Fille fille = new  Fille(i, "Fille", "Sensible");

	@Override	
    public ObjetClonable clone() throws CloneNotSupportedException {   
		ObjetClonable copie = (ObjetClonable)super.clone();
		
		copie.mere = mere.clone();
		return copie;
    }
	
	public int getI() {
		return i;
	}
	    
	public void setI(int i) {
		this.i = i;
	}
	    
	public Mere getMere() {
		return mere;
	}
	    
	    
	public Fille getFille() {
		return fille;
	}
}
