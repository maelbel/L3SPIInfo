/**
 * 
 */
package td;

/**
 * @author maelb
 *
 */
public class ConcreteStack implements AStack {
	
	private Object [] stack;
	private int sizeStack;
	private int iPeek;
	
	public ConcreteStack(int taille) {
		this.stack = new Object [taille];
		this.sizeStack = taille;
		this.iPeek = 0;
	}
	
	@Override
	public boolean isEmpty() {
		// TODO Auto-generated method stub
		return iPeek == 0;
	}

	@Override
	public void push(Object o) {
		// TODO Auto-generated method stub
		if(iPeek < sizeStack-1) {
			stack[iPeek] = o;
			iPeek++;
		} else {
			System.err.println("Error: Stack is full.\n"
							+ "This object '" + o + "' wasn't push in the stack.");
		}
	}

	@Override
	public Object peek() {
		// TODO Auto-generated method stub
		if(!isEmpty()) return stack[iPeek];
		else return null;
	}

	@Override
	public Object pop() {
		// TODO Auto-generated method stub
		if(!isEmpty()) {
			Object o = stack[iPeek];
			stack[iPeek] = null;
			iPeek--;
			return o;
		}
		else return null;
	}
	
	public String toString() {
		String message = "";
		
		for(Object element : stack) {
			if(element == null) message += "void \n";
			else message += element + "\n";
		}
				
		return message;
	}

}
