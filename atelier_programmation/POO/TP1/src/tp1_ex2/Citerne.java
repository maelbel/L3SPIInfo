/**
 * 
 */
package tp1_ex2;

import java.time.LocalDate;

import tp1_ex2.TestCiterne.Liquide;

/**
 * @author maelb
 *
 */
public class Citerne implements EstComparable, Cloneable {

	private static int numCuve = 0;
	private double capacite = 0.0;
	private static final int capaciteMax = 20000;
	private int tempCons;
	private Liquide typeLiquide;
	private LocalDate date;
	private String cuvRef;
	private double volOccupe = 0.0;
	
	
	public Citerne(double capacite, Liquide liquide) {
		
		if(capacite < 0) {
			throw new InternalError("Error: Negative capacity!");
		} else if(capacite==0) {
			throw new NullPointerException("Error: Capacity is null!");
		} else if(capacite>capaciteMax) {
			throw new InternalError("Error: Capacity superior at capacity max!");
		} else {
			this.capacite = capacite;
		}
		
		switch (liquide) {
	        case EAU:
	        	this.typeLiquide = liquide;
	            this.tempCons = 10;
	            break;
	
	        case VIN:
	        	this.typeLiquide = liquide;
	        	this.tempCons = 15;
	            break;
	
	        case HUILE:
	        	this.typeLiquide = liquide;
	        	this.tempCons = 9;
	            break;
	
	        default:
	            throw new InternalError("Error: Incompatible liquid!");
		}
		
		numCuve++;
		this.date = LocalDate.now();
		this.cuvRef = "Citerne n°"+ numCuve;
	}
	
	public LocalDate getDate() {
		return date;
	}
	
	public String getRef() {
		return cuvRef;
	}
	
	public String plusAncienne(Object c1, Object c2) {
		LocalDate dateC1 = ((Citerne) c1).getDate();
		LocalDate dateC2 = ((Citerne) c2).getDate();
		
		String result;
		
		if(dateC1.isAfter(dateC2)) {
			result = ((Citerne) c1).getRef(); 
		} else if (dateC1.equals(dateC2)) {
			result = "The both tank have been create the same day";
		} else {
			result = ((Citerne) c2).getRef(); 
		}
		
		return result;
	}
	
	public void getCuve() {
		System.out.println("Quantité de liquide stockée: "+ this.volOccupe +", "
				+ "Type de liquide stocké: "+ this.typeLiquide +", "
				+ "Mise en service: "+ this.date);
	}
	
	public int getNumCuve() {
		return numCuve;
	}
	
	public double getVolOccupe() {
		return this.volOccupe;
	}
	
	public double getCapacite() {
		return this.capacite;
	}
	
	public void nettoyage() {
		this.volOccupe = 0;
		this.typeLiquide = null;
	}
	
	public void setLiquide(Liquide liquide) {
		if(this.typeLiquide!=null) {
			throw new InternalError("Error: You must clean your tank!");
		} else {
			this.typeLiquide = liquide;
		}
	}
	
	public void ajouterLiquide(double quantite) {
		int reste = 0;
		
		if(typeLiquide==null) {
			throw new NullPointerException("Error: You must choose a liquid for your tank!");
		}
		
		if(quantite > 1 && this.capacite > quantite + volOccupe) {
			this.volOccupe += quantite;
		} else if (quantite > 0 && this.capacite > (quantite*this.capacite) + volOccupe) {
			this.volOccupe += quantite*this.capacite;
		} else if (quantite <= 0) {
			throw new InternalError("Error Citerne: Quantity cannot be negative or egal 0");
		} else {
			if(quantite > 1) {
				reste = (int) (volOccupe + quantite - capacite);
			} else {
				reste = (int) (volOccupe - capacite + (quantite*this.capacite));
			}
			this.volOccupe = capacite;
			System.err.println("Error Citerne: Capacity is full! Extra of: "+ reste);
		}
	}
	
	public void enleverLiquide(double quantite) {
		int reste = 0;
		
		if(quantite > 1 && 0 < volOccupe - quantite) {
			this.volOccupe -= quantite;
		} else if (quantite > 0 && 0 < volOccupe - (quantite*this.capacite)) {
			this.volOccupe -= quantite*this.capacite;
		} else if (quantite <= 0) {
			throw new InternalError("Error: Quantity cannot be negative or egal 0");
		} else {
			if(quantite > 1) {
				reste = (int) (quantite - volOccupe);
				this.volOccupe = 0;
			} else {
				reste = (int) ((quantite*this.capacite) - volOccupe);
				this.volOccupe = 0;
			}
			System.err.println("Error: Tank is void! There miss: "+ reste);
		}
	}
	
	//Overload of equals()
		public boolean equals(Object o) {
		    if (this == o)
		     return true;
		    if (o == null)
		      return false;
		    if (getClass() != o.getClass())
		      return false;
		    
		    Citerne other = (Citerne) o;
		    
		    if (typeLiquide == null) {
			      if (other.typeLiquide != null)
			        return false;
			    } else if (!typeLiquide.equals(other.typeLiquide)) 
			    	return false;
		    
		    if (capacite != other.capacite) return false;
		    
		    if (volOccupe != other.volOccupe) return false;
		    
		    if (date == null) {
			      if (other.date != null)
			        return false;
			    } else if (!date.equals(other.date)) 
			    	return false;
		    
		    return true;
		  }
	
	public String toString() {
		String message;
		
		message = this.cuvRef +", "
				+ this.typeLiquide +", "
				+ "capacité : "+ this.capacite +" m3, "
				+ "mise en service : "+ this.date +", "
				+ "volume occupé :"+ this.volOccupe;
		
		return message;
	}

	@Override
	public int compareA(Object o) {
		int result = 0;
		double volOccupeC2 = ((Citerne) o).getVolOccupe();
		
		
		if(this.volOccupe > volOccupeC2) {
			result = 1;
		} else {
			result = -1;
		}
		
		return result;
	}
}
