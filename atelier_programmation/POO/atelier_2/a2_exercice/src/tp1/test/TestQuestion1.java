package tp1.test;

import a2_exercice.Personne;
import a2_exercice.Employe;

public class TestQuestion1 {
	
	public static void main(String[] args){
		Personne pers1 = new Personne("de Miranda Lopes","Alexandre", 3, 4, 1998, 21, "Jefferson Street", "20250", "Corte");
		System.out.println(pers1);
		
		Personne pers2 = new Personne("Belliard","Mael", 21, 07, 2001, 5, "Avenue de la République", "20250", "Corte");
		System.out.println(pers2);
		
		Personne pers3 = new Personne("Belliard","Mael", 21, 07, 2001, 2, "Lieu-dit Campucciu", "20213", "Penta-di-Casinca");
		System.out.println(pers3);
		
		System.out.println("Il y a actuellement " + Personne.getNbPersonne() + " personnes");
		
		System.out.println("Est-ce que la personne 1 est plus agé que la personne 2 ?\n" 
							+ Personne.plusAgee(pers1.getDateNaissance(), pers2.getDateNaissance()));
		
		System.out.println("Est-ce que la personne 2 est plus agé que la personne 1 ?\n" 
				+ pers2.plusAgeeQue(pers1.getDateNaissance()));
		
		System.out.println("Est-ce que la personne n°2 est identique à la personne n°3 ?\n" 
							+ pers2.equals(pers3));
		
		System.out.println("Création de l'employé : " + pers1.getNom() + "\n");
		//Employe.createEmploye(pers1.getDateNaissance());
		//System.out.println("L'employé : " +  + "vient d'être créé\n");
	}
	
}
