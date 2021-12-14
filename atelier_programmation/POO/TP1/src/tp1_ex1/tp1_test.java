/**
 * 
 */
package tp1_ex1;

/**
 * @author maelb
 *
 */
public class tp1_test {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = null;
		int[] b = new int[] {-1,2,-3,4,5};
		MonTableau m1 = null;
		MonTableau m2 = null;
		
		try {
			m1 = new MonTableau(a);
			m2 = new MonTableau(b);
		} catch (NullPointerException e) {
			System.err.println(e);
		}
		
		System.out.println(m1.compareA(m2)); //Affiche 1,
		//car 1+2+3+4 > -1+2-3+4+5
	}

}
