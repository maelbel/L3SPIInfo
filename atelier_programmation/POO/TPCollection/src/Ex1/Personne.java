/**
 * 
 */
package Ex1;

/**
 * @author maelb
 *
 */
public class Personne implements Comparable<Personne> {

	private String name;
	private String lastName;
	private int age;
	
	public Personne(String name, String lastName, int age) {
		this.name = name;
		this.lastName = lastName;
		this.age = age;
	}
	
	public int getAge() {
		return age;
	}
	
	public String getName() {
		return name;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	@Override
	public int compareTo(Personne p) {
		int age1 = this.getAge();
		int age2 = p.getAge();
		int result;
		
		if(age1>age2) {
			result = 1;
		} else if(age2>age1) {
			result = -1;
		} else {
			
			result = name.compareTo(p.name);
			
			if(result == 0) {
				result = lastName.compareTo(p.lastName);
			}
		}
		
		return result;
	}
	
	public String toString() {
		String message;
		
		message = "Personne(name: "+ name +", lastname: "+ lastName +", age: "+ age +")\n";
		
		return message;
		
	}
	
	
}
