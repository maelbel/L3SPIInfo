package ExerciceException;

import java.net.URI;
import java.net.URISyntaxException;

public class TestURI {

	public static void main(String[] args) {
		
		String url = "https:";
		
		try {
			URI uriString = new URI(url);
			System.out.println("La création de l'URI s'est bien passé:"+ uriString);
		}
		catch(URISyntaxException e) {
			System.err.println("Problème lors de la création, il semble que "+ url +" ne soit pas un URI correct.");
		}
	}
}
