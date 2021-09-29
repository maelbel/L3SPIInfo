package a3bis_exercice;

public class GestionAgence {

	public static void main(String[] args) {
		
		Proprietaire proprio1 = new Proprietaire("Toto", "Corte");
		Proprietaire proprio2 = new Proprietaire("Titi", "Ajaccio");
		Proprietaire proprio3 = new Proprietaire("Tata", "Bastia");
		
		Agence agence1 = new Agence("ESPADONBLEU");

		Appartement appart1 = new Studio(proprio1);
		agence1.ajoutAppartement(appart1);
		
		Appartement appart2 = new MultiPiece(proprio1, 2);
		agence1.ajoutAppartement(appart2);
		
		Appartement appart3 = new MultiPiece(proprio2, 4);
		agence1.ajoutAppartement(appart3);
		
		System.out.println(agence1.afficher());
		
		Agence agence2 = new Agence("CROUS");
		
		Appartement appart4 = new Studio(proprio3);
		agence2.ajoutAppartement(appart4);
		
		Appartement appart5 = new MultiPiece(proprio3, 5);
		agence2.ajoutAppartement(appart5);
		
		System.out.println(agence2.afficher());
		
		System.out.println("Nombres total d'appartements dans les agences " + Agence.getNbAppTotal());
		
	}

}
