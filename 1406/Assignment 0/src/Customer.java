public class Customer {
	//Class Attributes
	String name;
	int age;
	float money;
	boolean admitted;

	//Constructors
	public Customer(String initName) {
		name = initName;
		age = 0;
		money = 0.0f;
		admitted = false;
	}
	public Customer(String initName, int initAge) {
		name = initName;
		age = initAge;
		money = 0.0f;
		admitted = false;
	}
	public Customer(String initName, int initAge, float initMoney) {
		name = initName;
		age = initAge;
		money = initMoney;
		admitted = false;
	}
	public Customer() {
		name = "Blank";
		age = 0;
		money = 0.0f;
		admitted = false;
	}

	//Instance Methods

	//Computes the fee of the customer dependent on their age
	public float computeFee(){
		if (this.age >=18 && this.age <65){
			return 12.75F;
		}else if (this.age >=4 && this.age <=17){
			return 8.50F;
		}else if (this.age <=3){
			return 0;
		}else{
			return 6.38F;
		}
	}

	//Allows the customer to spend the amount of money indicated in the parameter
	public boolean spend(float amount){
		if (this.money>=amount && amount>=0){
			this.money -= amount;
			return true;
		}
		return false;
	}

	//Checks if a Customer has more money than another Customer
	public boolean hasMoreMoneyThan(Customer c){
		return this.money > c.money;
	}

	//Uses the computeFee and spend methods to pay for an admission to an event
	public void payAdmission(){
		if (this.spend(this.computeFee())){
			this.admitted = true;
		}
    }

	//Tostring method
//	@Override
    public String toString() {
		if (this.admitted){
			return "Customer " + name + ": a " + age + " year old with $" + (double)money + " who has been admitted";
		}
		return "Customer " + name + ": a " + age + " year old with $" + (double)money + " who has not been admitted";
    }

}
