import java.util.Scanner;

public class TaxProgram {

    public static void main(String[] args) {
        double income, fedTax, provTax;
        int dependents;

        Scanner input = new Scanner(System.in);
        System.out.print("Please enter your taxable income: ");
        income = input.nextDouble();

        System.out.println();

        System.out.print("Please enter your number of dependents: ");
        dependents = input.nextInt();
        System.out.println();

        fedTax = 0.0;
        provTax = 0.0;

        if (income <= 29590){
            fedTax = (0.17*income);
        } else if (income > 29590 && income <=59179.99){
            fedTax = (0.17*29590) + (0.26*(income-29590));
        } else if (income >= 59180){
            fedTax = (0.17*29590) + (0.26*(29590)) + (0.29*(income-59180));
        }

        double base = (0.425 * fedTax);
        double deductions = (160.5 + (328*dependents));

        if (base < deductions){
            provTax = 0.0;
        } else {
            provTax = base - deductions;
        }

        double totalTax = fedTax + provTax;
        System.out.println(String.format("Income: %15s%.2f", "$", income));
        System.out.println(String.format("Dependents: %18d", dependents));
        System.out.println("------------------------------");
        System.out.println(String.format("Federal Tax: %11s%.2f", "$", fedTax));
        System.out.println(String.format("Provincial Tax: %10s%.2f", "$", provTax));
        System.out.println("==============================");
        System.out.println(String.format("Total Tax: %14s%.2f", "$", totalTax));

    }
}
