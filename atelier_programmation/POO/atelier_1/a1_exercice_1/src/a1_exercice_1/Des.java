package a1_exercice_1;

import java.util.*;

public class Des {
	//Variables
	protected String name;
	protected int nbFace = 6;
	protected static Random r = new Random();
	protected static int nbDe = 0;
	
	//Constructors
	//Constructor's when 2 parameters entered
	public Des(String name, int nbFace) throws IllegalArgumentException, NullPointerException{
		if (name == "") {
			throw new IllegalArgumentException("Error: name is empty");
		} else if (name == null) {
			throw new NullPointerException("Error: name is null");
		} else {
			this.name = name;
		}
		if (nbFace >= 3 && nbFace <= 120) {
			this.nbFace = nbFace;
		} else {
			throw new IllegalArgumentException("Error: nbFace is not between 3 and 120");
		}
		nbDe++;
	}
	
	//Constructor's when parameter name was entered
	public Des(String name) {
		this.name = name;
		nbDe++;
	}
	
	//Constructor's when parameter nbFace was entered
	public Des(int nbFace) {
		if (nbFace >= 3 && nbFace <= 120) {
			this.nbFace = nbFace;
		} else {
			System.err.println("Error: number of face not valid for dice: " + name + ". Please try again.");
		}
		nbDe++;
		this.name = "Dé n°" + nbDe;
	}
	
	//Methods
	//Method to change the number of face of the dice
	public void setNbFace(int nbFace_souhaitee){
		if (nbFace_souhaitee >= 3 && nbFace_souhaitee <= 120) {
			nbFace = nbFace_souhaitee;
		} else {
			System.err.println("Error: number of face not valid for dice: " + name + ". Please try again.");
		}
	}
	//Method to get the number of face of the dice
	public int getNbFace(){
		return nbFace;
	}
	
	//Method to throw the dice
	public int lancer() {
		int nbRandom= r.nextInt(nbFace+1);
		
		return nbRandom;
	}
	//Method to throw nbLance times the dice
	public int lancer(int nbLance) {
		
		int nbRandom;
		int nbRandomMax = 0;
		
		for (int i=0; i<(nbLance-1);i++) {
			nbRandom = lancer();
			if(nbRandom > nbRandomMax){
				nbRandomMax = nbRandom;
			}
		}
		
		return nbRandomMax;
	}
	
	//Overload of toString()
	public String toString() {
		String message = "Name of dice: " + name + "\n"
						+ "Number of face: " + nbFace;
		return message;
	}
	//Overload of equals()
	public boolean equals(Object obj) {
	    if (this == obj)
	     return true;
	    if (obj == null)
	      return false;
	    if (getClass() != obj.getClass())
	      return false;
	    
	    Des other = (Des) obj;
	    
	    if (name == null) {
		      if (other.name != null)
		        return false;
		    } else if (!name.equals(other.name)) 
		    	return false;
	    
	    if (nbFace != other.nbFace) return false;
	    
	    return true;
	  }
}
