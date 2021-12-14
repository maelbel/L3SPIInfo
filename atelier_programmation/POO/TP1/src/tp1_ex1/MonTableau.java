/**
 * 
 */
package tp1_ex1;

/**
 * @author maelb
 *
 */
public class MonTableau implements EstComparable {

	private int [] a;
	
	
	public MonTableau(int[] a) {
		if (a==null){
			throw new NullPointerException("Error: Object is null!");
		}else{
			this.a = a;
		}
	}
	
	public int [] getA() {
		return a;
	}

	@Override
	public int compareA(Object o) {
		int sommeA = 0;
		int sommeB = 0;
		int result = 0;
		
		for(int i = 0; i < this.a.length; i++) {
			sommeA += a[i];
		}
		
		int [] b = ((MonTableau) o).getA();
		
		for(int i = 0; i < b.length; i++) {
			sommeB += b[i];
		}
		
		if(sommeA<sommeB) {
			result = -1;
		} else if(sommeA==sommeB){
			result = 0;
		} else {
			result = 1;
		}
		
		return result;
	}

}
