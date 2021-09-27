package exercice_1;

public class ManipRob {
	
  public static void main(String[] args) {
    Robot r1 = new Robot("Toto", 10, 20, 3);
    Robot r2 = new Robot("Titi", 0, 0, 1);

    r1.modifOrientation(4);
    r1.deplacement();
    r2.modifOrientation(3);
    r2.deplacement();
    
    r1.afficheToi();
    r2.afficheToi();
    
    System.out.println(r1);
    System.out.println(r2);
  }

}
