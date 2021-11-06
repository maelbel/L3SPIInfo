package ExerciceException;

import java.net.URI;
import java.net.URISyntaxException;

public class TestURI {

	public static void main(String[] args) {
		
		String url = "https:";
		
		try {
			URI uriString = new URI(url);
			System.out.println("La cr�ation de l'URI s'est bien pass�:"+ uriString);
		}
		catch(URISyntaxException e) {
			System.err.println("Probl�me lors de la cr�ation, il semble que "+ url +" ne soit pas un URI correct.");
		}
	}
}
