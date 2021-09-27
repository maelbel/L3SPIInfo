package exercice_1;

public class Robot {
  //Variables
  private String reference;
  private String name;
  private int posX;
  private int posY;
  private int orientation;
  private static int nbRobot = 0;
  private String str_orientation;

  //Constructeurs
  public Robot(String name, int posX, int posY, int orientation){
    this.name = name;
    this.posX = posX;
    this.posY = posY;
    this.orientation = orientation;
    nbRobot++;
    this.reference = "ROB"+nbRobot;
  }
  public void initPosition(String name){
    this.name = name;
    posX = 0;
    posY = 0;
    orientation = 1;
  }

  //Methodes
  public void modifOrientation(int orientation_souhaite){
    orientation = orientation_souhaite;
    //System.out.println("Orientation modifi�");
  }
  public void deplacement(){
    if (posX == 0 && orientation == 4){
      posX = 0;
      //System.out.println("Voiture bloqu�e !");
    }else if(posY == 0 && orientation == 3){
      posY = 0;
      //System.out.println("Voiture bloqu�e !");
    }else{
      switch (orientation){ //Selon l'orientation
        case 1: //Orient� Nord
          posY++;
          break;
        case 2: //Orient� Est
          posX++;
          break;
        case 3: //Orient� Sud
          posY--;
          break;
        case 4: //Orient� Ouest
          posX--;
          break;

        default:
        	break;
      }
      //System.out.println("d�placement effectu�");
    }
  }
  public void afficheToi() {
	switch(orientation) {
	  	case 1:
	  		str_orientation = "Nord";
	  		break;
	  	case 2:
	  		str_orientation = "Est";
	  		break;
	  	case 3:
	  		str_orientation = "Sud";
	  		break;
	  	case 4:
	  		str_orientation = "Ouest";
	  		break;
	  	default:
	          break;
	}
  	String message = "Nom: " + this.name + "\n"
  					+ "R�f�rence: " + this.reference + "\n"
  					+ "Position: " + this.posX + "x - " + this.posY + "y \n"
  					+ "Orientation: " + this.str_orientation;
  	System.out.println(message);
  }
  public String toString(){
	  switch(orientation) {
	  	case 1:
	  		str_orientation = "Nord";
	  		break;
	  	case 2:
	  		str_orientation = "Est";
	  		break;
	  	case 3:
	  		str_orientation = "Sud";
	  		break;
	  	case 4:
	  		str_orientation = "Ouest";
	  		break;
	  	default:
	          break;
	}
		String message = "Le Robot s'appelle "+ name
						+ ". Sa r�f�rence est " + reference
						+ ". Sa position est " + posX + " en ordonn� et " + posY + " en abscisse"
						+ ". Il est orient� direction " + str_orientation;

		return message;
}
}
