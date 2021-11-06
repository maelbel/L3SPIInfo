package a1_exercice_1;

public class TestDe {
	
	public static void main(String[] args){
		Des de1 = new Des("Strong", 8);
		Des de2 = new Des("Normal dice");
		Des de3 = new Des(100);
		Des de4 = new Des("Normal dice");
		Des de5 = null;
		
		try {
			de5 = new Des("", -5);
		} catch(IllegalArgumentException e) {
			System.err.println(e);
		} catch(NullPointerException e) {
			System.err.println(e);
		}
		
		//de.setNbFace(2);
		System.out.println("Le dé 2 à fait: " + de2.lancer());
		System.out.println("Le dé 2 à fait: " + de2.lancer(10));
		
		System.out.println(de1);
		System.out.println(de2);
		System.out.println(de3);
		
		System.out.println(de2 == de3);
		System.out.println(de2.equals(de3));
		System.out.println(de2.equals(de4));
		
		DePipe dePipe = new DePipe("Cheated dice", 8, 6);
		System.out.println(dePipe);
		System.out.println("Le dé pipé à fait: " + dePipe.lancer());
		
		DeMemoire deMemoire = new DeMemoire("Memory dice", 10);
		System.out.println(deMemoire);
		System.out.println("Le dé mémoire à fait: " + deMemoire.lancer());
	}
	
}
