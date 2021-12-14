package ex2;

public class Fille extends Mere{
	private Object unObjetSensible;
	
	public Fille(int unI, String unObj, Object unObjSens){
		super(unI,unObj);
		unObjetSensible = unObjSens;
	}
	
	public Object getObjet() {
		return unObjetSensible;
	}

	public void setObjet(Object unObjetSensible) {
	    	this.unObjetSensible = unObjetSensible;
	}

}