/**
 * 
 */
package Ex1;

/**
 * @author maelb
 *
 */
public class Genericite<N,G> {
	
	private N nombre;
	private G date;
	
	public Genericite(N nombre, G date) {
		this.nombre = nombre;
		this.date = date;
	}
	
	public N getNombre() {
		return nombre;
	}
	
	public void setNombre(N nombre) {
		this.nombre = nombre;
	}
	
	public G getDate() {
		return date;
	}
	
	public void setDate(G date) {
		this.date = date;
	}
}
