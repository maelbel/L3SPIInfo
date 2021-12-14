package ex2;

public class Mere implements Cloneable{
	private int i;
	private String unObjet; //Clonable
	
	public Mere(int unI, String string){
		i = unI; unObjet = string;
	}
	
	@Override
	public Mere clone() throws CloneNotSupportedException {
		return (Mere)super.clone();
	}
	
	public int getEntier() {
		return i;
	}
	    
	public void setEntier(int i) {
	    	this.i = i;
	}
	
	public Object getObjet() {
		return unObjet;
	}
	    
	public void setObjet(String unObjet) {
	    	this.unObjet = unObjet;
	}
}