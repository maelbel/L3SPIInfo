/**
 * 
 */
package td;

/**
 * @author maelb
 *
 */
public interface AStack {
	
	boolean isEmpty();
	void push(Object o);
	
	Object peek();	
	
	Object pop();
}
