package a2_exercice;

import java.util.*;
//import a2_exercice.Adresse;


public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    protected String nom;
    protected String prenom;
    private final GregorianCalendar dateNaissance;
    protected Adresse adresse = ADRESSE_INCONNUE;
    private static int nbPersonne = 0;
    private static String nomDernierePersonneCree;
    private static final int AGE_MAJORITE = 18;
    private int ageObtentionDernierDiplome;
	
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom = lePrenom;
		dateNaissance = laDate;
		adresse = lAdresse;
		nbPersonne++;
		nomDernierePersonneCree = nom;
	}
	
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'année de naissance
	 * @param numero le n° de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, new GregorianCalendar(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le prénom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance	 
	 */
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public void setAdresse(Adresse a) {
		adresse = a;
	}
	
	public static int getNbPersonne() {
		return nbPersonne;
	}
	public static final int getAgeMajorite() {
		return AGE_MAJORITE;
	}
	public int getAgeObtentionDernierDiplome() {
		return ageObtentionDernierDiplome;
	}

		
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result = "\nNom : " + nom + "\n"
		+ "Prénom : " + prenom + "\n" +
		"Né(e) le : " + dateNaissance.get(Calendar.DAY_OF_MONTH) +
		"-" + dateNaissance.get(Calendar.MONTH) +
		"-" + dateNaissance.get(Calendar.YEAR) + "\n" +
		"Adresse : " + adresse.toString() + "\n" +
		"Personne n°" + nbPersonne;
		
		return result;
	}
public static boolean plusAgee(GregorianCalendar dateNaissancePers1, GregorianCalendar dateNaissancePers2) {
		
		int anneePers1 = dateNaissancePers1.get(Calendar.YEAR);
		int anneePers2 = dateNaissancePers2.get(Calendar.YEAR);
		int moisPers1 = dateNaissancePers1.get(Calendar.MONTH);
		int moisPers2 = dateNaissancePers2.get(Calendar.MONTH);
		int jourPers1 = dateNaissancePers1.get(Calendar.DAY_OF_MONTH);
		int jourPers2 = dateNaissancePers2.get(Calendar.DAY_OF_MONTH);
		
		boolean resultat = false;
		
		if(anneePers1 < anneePers2) {
			resultat = true;
		}
		
		if(anneePers1 == anneePers2) {
			
			if(moisPers1 == moisPers2) {
				
				if(jourPers1 > jourPers2) {
					resultat = true;
				}
				
			}
			
			if(moisPers1 > moisPers2) {
				resultat = true;
			}
		}
		
		return resultat;
	}
	public boolean plusAgeeQue(GregorianCalendar dateNaissancePers) {
		
		int anneePers1 = this.dateNaissance.get(Calendar.YEAR);
		int anneePers2 = dateNaissancePers.get(Calendar.YEAR);
		int moisPers1 = this.dateNaissance.get(Calendar.MONTH);
		int moisPers2 = dateNaissancePers.get(Calendar.MONTH);
		int jourPers1 = this.dateNaissance.get(Calendar.DAY_OF_MONTH);
		int jourPers2 = dateNaissancePers.get(Calendar.DAY_OF_MONTH);
		
		boolean resultat = false;
		
		if(anneePers1 < anneePers2) {
			resultat = true;
		}
		
		if(anneePers1 == anneePers2) {
			
			if(moisPers1 == moisPers2) {
				
				if(jourPers1 > jourPers2) {
					resultat = true;
				}
				
			}
			
			if(moisPers1 > moisPers2) {
				resultat = true;
			}
		}
		
		return resultat;
	}
	//Overload of equals()
	public boolean equals(Object obj) {
	    if (this == obj)
	     return true;
	    if (obj == null)
	      return false;
	    if (getClass() != obj.getClass())
	      return false;
	    
	    Personne other = (Personne) obj;
	    
	    if (nom == null) {
		      if (other.nom != null)
		        return false;
		    } else if (!nom.equals(other.nom)) 
		    	return false;
	    
	    if (prenom == null) {
		      if (other.prenom != null)
		        return false;
		    } else if (!prenom.equals(other.prenom)) 
		    	return false;
	    
	    if (dateNaissance == null) {
		      if (other.dateNaissance != null)
		        return false;
		    } else if (!dateNaissance.equals(other.dateNaissance)) 
		    	return false;
	    
	    return true;
	  }
}