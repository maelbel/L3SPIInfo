package ex2;

public class TestClonable {

	public static void main(String[] args) {
		ObjetClonable I = new ObjetClonable();
		ObjetClonable J = null;
	      
		try {
			J = I.clone();
		} catch (CloneNotSupportedException e) {
			e.printStackTrace();
		}
		
	      System.out.println("Dans l'original " + I.getI() + " " +
	    		  I.getMere().getEntier() +  " " + 
		    	  I.getMere().getObjet() + " " +
				  I.getFille().getEntier() + " " +
				  I.getFille().getObjet());
	      
	      System.out.println("Dans la copie   " + J.getI() + " " +
				 J.getMere().getEntier() +  " " + 
	    		 J.getMere().getObjet() + " " +
				 J.getFille().getEntier() + " " +
				 J.getFille().getObjet());
	
	      
	      I.setI(2);
	      I.getMere().setEntier(20);
	      I.getFille().setEntier(2000);
	      System.out.println("\nApres changement de tout ce que contient l'original :");
	      System.out.println("Dans l'original " + I.getI() + " " +
	    		  I.getMere().getEntier() +  " " + 
		    	  I.getMere().getObjet() + " " +
				  I.getFille().getEntier() + " " +
				  I.getFille().getObjet());
	      
	      System.out.println("Dans la copie   " + J.getI() + " " +
				 J.getMere().getEntier() +  " " + 
	    		 J.getMere().getObjet() + " " +
				 J.getFille().getEntier() + " " +
				 J.getFille().getObjet());

	}

}
