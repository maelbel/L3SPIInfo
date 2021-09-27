package a2_exercice;

import java.time.*;
import java.util.*;

public class Employe extends Personne{

	private double salaire;
	private LocalDate dateEmbauche;

	protected Employe(String leNom, String lePrenom, GregorianCalendar dateNaissance, Adresse lAdresse, double salaire, LocalDate dateEmbauche) {
		super(leNom, lePrenom, dateNaissance, lAdresse);
		this.salaire = salaire;
		this.dateEmbauche = dateEmbauche;
	}

	public Object createEmploye(GregorianCalendar dateNaissance) {
		LocalDate ld = dateNaissance.toZonedDateTime().toLocalDate();
	    LocalDate dateEmbauche = LocalDate.now();
	    
	    Period ageP = Period.between(ld, dateEmbauche);
	    
	    int age = ageP.getYears();
	    
	    if(age >= 16 && age < 65) {
	    	new Employe(nom, prenom, dateNaissance, adresse, salaire, dateEmbauche);
	    } else {
	    	System.err.println("Error: You can't be an employe");
	    }
	    return null;
	}
}