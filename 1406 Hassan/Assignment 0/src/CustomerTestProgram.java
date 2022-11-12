public class CustomerTestProgram {
	public static void main(String args[]) {
		Customer c;

		c = new Customer("Bob");
		System.out.println(c.name);
		System.out.println(c.age);
		System.out.println(c.money);
	}
}
