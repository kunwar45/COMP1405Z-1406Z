public class CustomerAdmissionTestProgram {
	public static void main(String[] args) {
		Customer c1, c2, c3, c4;
		c1 = new Customer("Bob", 17, 100);
		c2 = new Customer("Dottie", 3, 10);
		c3 = new Customer("Jane", 24, 40);
		c4 = new Customer("Sam", 72, 5);
		System.out.println("Here is the money before going into the circus:");
		System.out.println(" Bob has $" + c1.money);
		System.out.println(" Dottie has $" + c2.money);
		System.out.println(" Jane has $" + c3.money);
		System.out.println(" Sam has $" + c4.money);
		System.out.println(" Bob has been admitted ... " + c1.admitted);
		System.out.println(" Dottie has been admitted ... " + c2.admitted);
		System.out.println(" Jane has been admitted ... " + c3.admitted);
		System.out.println(" Sam has been admitted ... " + c4.admitted);
		c1.payAdmission();
		System.out.println(" Bob has been admitted ... " + c1.admitted);
		c2.payAdmission();
		System.out.println(" Dottie has been admitted ... " + c2.admitted);
		c3.payAdmission();
		System.out.println(" Jane has been admitted ... " + c3.admitted);
		c4.payAdmission();
		System.out.println(" Sam has been admitted ... " + c4.admitted);
		System.out.println("Here is the money after going into the circus:");
		System.out.println(" Bob has $" + c1.money);
		System.out.println(" Dottie has $" + c2.money);
		System.out.println(" Jane has $" + c3.money);
		System.out.println(" Sam has $" + c4.money);
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c3);
		System.out.println(c4);
	}
}
