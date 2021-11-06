package ex2;

public class Fille extends Mere{
	private Object unObjetSensible;
	
	public Fille(int unI, UneClasse unObj, Object unObjSens){
		super(unI,unObj);
		unObjetSensible = unObjSens;
	}

	public Object clone() {
		
	}
}