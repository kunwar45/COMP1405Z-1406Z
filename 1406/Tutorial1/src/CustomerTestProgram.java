public class CustomerTestProgram {
    public static void main(String[] args) {
        Customer c;

        c = new Customer();
        c.name = "Bob";
        c.age = 27;
        c.money = 50;
        System.out.println(c.name);
        System.out.println(c.age);
        System.out.println(c.money);
    }
}
