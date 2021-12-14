/**
 * 
 */
package tp1_ex2;

import tp1_ex2.TestCiterne.Liquide;

/**
 * @author maelb
 *
 */
public class TropPlein {

	private double capacite;
	private Liquide liquide;
	private double volOccupe;
	
	public TropPlein(double capacite, Liquide liquide, double capaciteCuve) {
		this.liquide = liquide;
		
		if(capaciteCuve<capacite && capaciteCuve > 0) {
			this.capacite = capaciteCuve;
		} else {
			System.err.println("Error TropPlein: Wrong capacity for TropPlein!");
			this.capacite = capacite*0.10;
		}
	}
	
	public void ajouterLiquide(double quantite) {
		if(quantite > 1 && this.capacite > quantite + volOccupe) {
			this.volOccupe += quantite;
		} else if (quantite > 0 && this.capacite > (quantite*this.capacite) + volOccupe) {
			this.volOccupe += quantite*this.capacite;
		} else if (quantite <= 0) {
			throw new InternalError("Error TropPlein: Quantity cannot be negative or egal 0");
		} else {
			this.volOccupe = this.capacite;
			System.err.println("Error TropPlein: Capacity is full!!!");
		}
		
		if(volOccupe == capacite/2) {
			System.err.println("Watch Out! Half full!");
		}
	}
	
	public double getVol() {
		return volOccupe;
	}
	
	public double getCapacite() {
		return this.capacite;
	}
	
	public void enleverLiquide(double quantite) {
		int reste = 0;
		
		if(quantite > 1 && 0 < volOccupe - quantite) {
			this.volOccupe += quantite;
		} else if (quantite > 0 && 0 < volOccupe - (quantite*this.capacite)) {
			this.volOccupe -= quantite*this.capacite;
		} else if (quantite <= 0) {
			throw new InternalError("Error Trop Plein: Quantity cannot be negative or egal 0");
		} else {
			if(quantite > 1) {
				reste = (int) (quantite - volOccupe);
				this.volOccupe = 0;
			} else {
				reste = (int) ((quantite*this.capacite) - volOccupe);
				this.volOccupe = 0;
			}
			System.err.println("Error TropPlein: Tank is void! There miss: "+ reste);
		}
	}
	
	public String toString() {
		String message;
		
		message = "TropPlein, capacité : "+ capacite + "m3, "+ liquide + ", " + volOccupe;
		
		return message;
	}
}
