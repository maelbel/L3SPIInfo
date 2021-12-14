/**
 * 
 */
package tp1_ex2;

/**
 * @author maelb
 *
 */
public class TestCiterne {

	public enum Liquide{
		EAU, VIN, HUILE
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Citerne c1 = new Citerne(10000, Liquide.EAU);
		Citerne c2 = new Citerne(8000, Liquide.EAU);
		
		System.out.println(c1);
		System.out.println(c2);
		
		c1.ajouterLiquide(0.5);
		c1.ajouterLiquide(7000);
		
		c2.ajouterLiquide(4000);
		c2.enleverLiquide(5000);
		
		System.out.println("C1 equals C2? "+ c1.equals(c2));
		System.out.println("Compare C1 to C2: "+ c1.compareA(c2));
		System.out.println(c2.plusAncienne(c1, c2));
		
		c1.nettoyage();
		c1.ajouterLiquide(5000);
		c1.setLiquide(Liquide.HUILE);
		
		System.out.println(c1);
		System.out.println(c2);
		
		CiterneSecurisee c3 = new CiterneSecurisee(5000, Liquide.VIN, 0);
		c3.ajouterLiquide(5300);
		System.out.println(c3);
		
		CiterneSecurisee c4 = new CiterneSecurisee(7500, Liquide.EAU, 500);
		c4.ajouterLiquide(8500);
		System.out.println(c4);
		c4.enleverLiquide(1000);
		System.out.println(c4);
		
		Citerne c5 = null;
		
		try {
			c5 = c4.clone();
		} catch (CloneNotSupportedException e) {
			e.printStackTrace();
		}
		
		System.out.println(c5);
		
		System.out.println("Compare C5 to C3: "+ c5.compareA(c3));
	}

}
