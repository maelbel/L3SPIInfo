package td;

public class Main {

	public static void main(String[] args) {

		ConcreteStack tableau = new ConcreteStack(5);
		
		tableau.push("hey");
		tableau.push(59);
		tableau.push("stack in stack");
		tableau.push(4);
		tableau.push("Chhhhheeeeeeeeeesse");
		
		tableau.peek();
		
		System.out.println("###ELEMENTS OF STACK###");
		
		System.out.println(tableau);
		
		System.out.println("L'�l�ment " + tableau.peek() + " est le dernier �l�ment du tableau");
		tableau.push("fleur");
		System.out.println("L'�l�ment " + tableau.pop() + " est le dernier �l�ment du tableau et a �t� supprim�");
		System.out.println(tableau.isEmpty());
	}

}
