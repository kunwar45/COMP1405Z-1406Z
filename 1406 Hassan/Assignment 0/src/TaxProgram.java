import java.util.Scanner;
public class TaxProgram {
    public static void main(String[] args) {
        double income, fedTax, provTax, base, deductions;
        int dependents;

            Scanner input = new Scanner(System.in);
            System.out.print("Please enter your taxable income: ");
            income = input.nextDouble();
            System.out.print("Please enter your number of dependents: ");
            dependents = input.nextInt();
            fedTax = 0.0;
            provTax = 0.0;
            base = 0.0;
            deductions = 0.0;

            //fedTax calculations
            if (income<=29590.0){
                fedTax = income * 0.17;
            }else if (income>29590 && income<59180){
                fedTax = (29590.0*0.17) + (income-29590.0)*0.26;
            }else if (income>=59180.0){
                fedTax = (29590.0*0.17) + (29590.0*0.26) + (income-59180.0)*0.29;
            }

            //provTax calculations
            base = (fedTax*0.425);
            deductions = (160.50 + (328.0*dependents));
            if (base<deductions){
                provTax = 0;
            }else{
                provTax = base - deductions;
            }

            //Tax Breakdown formatting
            System.out.println("Here is your tax breakdown: ");
            String strIncome = String.format("%s%,1.2f", "$",income);
            System.out.printf("%s","Income");
            System.out.printf("%47s%n",String.format("%s%,1.2f", "$",income));
            System.out.printf("%s","Dependants");
            System.out.printf("%43s%n",""+dependents);
            System.out.print("-----------------------------------------------------\n");
            System.out.printf("%s","Federal Tax");
            System.out.printf("%42s%n",String.format("%s%,1.2f", "$",fedTax));
            System.out.printf("%s","Provincial Tax");
            System.out.printf("%39s%n",String.format("%s%,1.2f", "$",provTax));
            System.out.print("=====================================================\n");
            System.out.printf("%s","Total Tax");
            System.out.printf("%44s%n",String.format("%s%,1.2f", "$",fedTax+provTax));
    }
}