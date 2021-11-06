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
		
		System.out.println("L'élément " + tableau.peek() + " est le dernier élément du tableau");
		tableau.push("fleur");
		System.out.println("L'élément " + tableau.pop() + " est le dernier élément du tableau et a été supprimé");
		System.out.println(tableau.isEmpty());
	}

}
