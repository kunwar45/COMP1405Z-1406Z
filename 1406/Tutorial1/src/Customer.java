public class Customer {

    String name;
    int age;
    float money;
    float fee;
    boolean admitted;

    public Customer(String initName){
        name = initName;
        age = 0;
        money = 0.0f;
        admitted = false;
    }

    public Customer(String initName, int initAge){
        name = initName;
        age = initAge;
        money = 0.0f;
        admitted = false;
    }

    public Customer(String initName, int initAge, float initMoney){
        name = initName;
        age = initAge;
        money = initMoney;
        admitted = false;
    }

    public Customer(){
        name = "Bob";
        age = 0;
        money = 0.0f;
        admitted = false;
    }

    public float computeFee(){
        if (age<=3){
            fee = 0;
        } else if (age > 3 && age <=17){
            fee = 8.50f;
        } else if (age >=18 && age < 65){
            fee = 12.75f;
        } else {
            fee = 6.375f;
        }

        return fee;
    }

    public boolean spend(float amount){
        if (amount <= money){
            money = money - amount;
            return true;
        }
        return false;
    }

    public boolean hasMoreMoneyThan(Customer c){
        if (money > c.money){
            return true;
        }
        return false;
    }

    public void payAdmission(){
        admitted = spend(computeFee());
    }

    @Override
    public String toString() {
        if (admitted){
            return "Customer " + name + ": a " + age + " year old with $" + money + "who has been admitted";
        } else {
            return "Customer " + name + ": a " + age + " year old with $" + money + "who has not been admitted";
        }
    }
}
