/**
 * 
 */
package Ex1;

import java.io.*;
import java.util.*;

/**
 * @author maelb
 *
 */
public class TestGenericite {
	/**
	 * @param
	 */
	public static void main(String[] args) {
		
		//Question 1
		System.out.println("#######################");
		System.out.println("##     Question 1    ##");
		System.out.println("#######################");
		
		Integer i = null;
		GregorianCalendar g = null;
		Genericite<Integer,GregorianCalendar> g1 = new Genericite<Integer, GregorianCalendar>(i, g);
		g1.setNombre(new Integer(5));
		g1.setDate(new GregorianCalendar(2018, 6, 27, 16, 16, 47));
		
		//Question 2
		System.out.println("\n#######################");
		System.out.println("##     Question 2    ##");
		System.out.println("#######################");
		
		try{
			Scanner scan = new Scanner(new File("dictionary.txt"));
			anagramme(scan, 8);
		}catch(FileNotFoundException e){
			System.err.println("Le fichier n'a pas ete trouve...");
		}
		
		//Question 3
		System.out.println("\n#######################");
		System.out.println("##     Question 3    ##");
		System.out.println("#######################");
		
		ListesTriees(5);
		
		//Question 4
		System.out.println("\n#######################");
		System.out.println("##     Question 4    ##");
		System.out.println("#######################");
		
		Comparaison();
		
		//Question 5
		System.out.println("\n#######################");
		System.out.println("##     Question 5    ##");
		System.out.println("#######################");
				
		Personne pers1 = new Personne("Mael", "Belliard", 20);
		Personne pers2 = new Personne("Alexandre", "De Miranda Lopes", 23);
		Personne pers3 = new Personne("Aurèle", "Véron-Guaitella", 20);
		
		
		List<Personne> listPers = Arrays.asList(pers1, pers2, pers3);
		Collections.sort(listPers);
		System.out.println(listPers);
	}
	
	public static void anagramme(Scanner scan, int i) {
		// Read words from file and put into simulated multimap 
		Map<String, List<String>> m = new HashMap<String, List<String>>();
		
		String word;
		while(scan.hasNext()){ 
			String alpha = alphabetize(word = scan.next()); 
			List<String> list = m.get(alpha); 
			if (list==null) m.put(alpha, list=new ArrayList<String>());
			list.add(word);
			
			if(list.size()>=i) {
				System.out.println(list.size() + ": " + list);
			}
		}
		
	}
	
	private static String alphabetize(String s){ 
		int count[] = new int[256]; 
		int len = s.length(); 
		for (int i=0; i<len; i++) count[s.charAt(i)]++; 
		StringBuffer result = new StringBuffer(len); 
		for (char c='a'; c<='z'; c++) 
		for (int i=0; i<count[c]; i++) result.append(c); 
		
		return result.toString();
	}
	
	public static void ListesTriees(int nombre) {
		int min = 0;
		int max = 1000;
		
		List<Integer> list = new ArrayList<Integer>();
		Set<Integer> listSet = new TreeSet<Integer>();
		
		for(int i = 0; i < nombre; i++) {
			int randint = (int)(Math.random()*(max-min+1)+min);
			
			list.add(new Integer(randint));
			listSet.add(new Integer(randint));
		}
		Collections.sort(list);
		
		System.out.println("\n## Première Version ##");
		for (Integer i : list){
			System.out.println(i + ", ");
		}
		
		System.out.println("\n## Seconde Version ##");
		for (Integer i : listSet) {
			System.out.println(i + ", ");
		}
		
	}
	
	public static void Comparaison() {
		List<String> list = new ArrayList<String>();
		list.add("cette");
		list.add("chaine");
		list.add("avec");
		list.add("quelques");
		list.add("autres");
		list.add("toutes");
		list.add("differentes");
		
		System.out.println("args avant tri:"+ list);
		
		Collections.sort(list);
		System.out.println("tri lexico:"+ list);
		
		list.sort(Comparator.comparing(String::length).thenComparing(String::compareTo));
		System.out.println("tri militaire:"+ list);
		
		Collections.sort(list);
		Collections.reverse(list);
		System.out.println("tri inverse lexico:"+ list);
	}
}
