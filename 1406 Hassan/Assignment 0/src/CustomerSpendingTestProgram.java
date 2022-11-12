public class CustomerSpendingTestProgram {
	public static void main(String[] args) {
		Customer c1, c2, c3;

		c1 = new Customer("Bob", 25, 50.00f);
		System.out.println(c1.money);
		c2 = new Customer("Dottie", 53, 100.00f);
		System.out.println(c2.money);
		c3 = new Customer("Jane", 21, 25.00f);
		System.out.println(c3.money);
		if (!c1.spend(10.00f))
			System.out.println("Unable to spend $10");
		if (!c1.spend(4.75f))
			System.out.println("Unable to spend $4.75");
		if (!c1.spend(15.25f))
			System.out.println("Unable to spend $15.25");
		if (!c1.spend(100.00f))
			System.out.println("Unable to spend $100");
		System.out.println(c1.money);
		System.out.println("Bob has more money than Dottie: " +
				c1.hasMoreMoneyThan(c2));
		System.out.println("Dottie has more money than Jane: " +
				c2.hasMoreMoneyThan(c3));
	}
}
