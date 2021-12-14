/**
 * 
 */
package tp1_ex2;

import tp1_ex2.TestCiterne.Liquide;

/**
 * @author maelb
 *
 */
public class CiterneSecurisee extends Citerne implements EstComparable{

	private TropPlein cuve;
	private double capacite;
	private Liquide typeLiquide;
	private double volOccupe;
	
	public CiterneSecurisee(double capacite, Liquide liquide, double capaciteCuve) {
		super(capacite, liquide);
		this.capacite = capacite;
		this.typeLiquide = liquide;
		
		this.cuve = new TropPlein(capacite, liquide, capaciteCuve);
	}
	
	public void ajouterLiquide(double quantite) {
		super.ajouterLiquide(quantite);
		
		double reste = 0.0;
		
		if(quantite > 1) {
			reste = (volOccupe + quantite) - capacite;
		} else {
			reste = (volOccupe - capacite + (quantite*this.capacite));
		}
		this.volOccupe = this.capacite;
		cuve.ajouterLiquide(reste);
	}
	
	public void enleverLiquide(double quantite) {
		double volCuve = this.cuve.getVol();
		double reste = 0.0;
		
		if(volCuve>0) {
			reste = quantite - volCuve;
			this.cuve.enleverLiquide(quantite);
			super.enleverLiquide(reste);
		} else {
			super.enleverLiquide(quantite);
		}
	}
	
	public String toString() {
		String message = super.toString() + "\n" + cuve.toString();
		
		return message;
		}

	@Override
	public int compareA(Object o) {
		int result = 0;
		double volOccupeC2 = ((CiterneSecurisee) o).getVolOccupe();
		double capCapaciteC2 = ((CiterneSecurisee) o).getCapacite();
		
		double volCuveC1 = this.cuve.getVol();
		double capCuveC1 = this.cuve.getCapacite();
		double volCuveC2 = ((CiterneSecurisee) o).cuve.getVol();
		double capCuveC2 = ((CiterneSecurisee) o).cuve.getCapacite();
		
		if(this.volOccupe + volCuveC1 > volOccupeC2 + volCuveC2) {
			if(this.capacite + capCuveC1 > capCapaciteC2 + capCuveC2) {
				result = 1;
			} else {
				result = -1;
			}
		} else {
			result = -1;
		}
		
		return result;
	}
	
	@Override
	public CiterneSecurisee clone() throws CloneNotSupportedException {
		return (CiterneSecurisee)super.clone();
	}
	
}
