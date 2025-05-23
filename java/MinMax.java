import java.util.Scanner;
public class MinMax {
    public static void main(String[] args) {

        int num1,num2,num3;
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter first number: ");
        num1 = scan.nextInt();
        System.out.print("Enter second number: ");
        num2 = scan.nextInt();
        System.out.print("Enter third number: ");
        num3 = scan.nextInt();

        int maximum = MinMax.maximum(num1, num2, num3);
        int minimum = MinMax.minimum(num1, num2, num3);

        System.out.println("The maximum number is: " + maximum);
        System.out.println("The minimum number is: " + minimum);

    }
        public static int maximum(int num1, int num2, int num3) {
        int max = num1;
        if (num2 > max) {
            max = num2;
        }
        if(num3 > max) {
            max = num3;
        }
        return max;
        }

        public static int minimum(int num1, int num2, int num3) {
        int min = num1;
        if (num2 < min) {
            min = num2;
        }
        if (num3 < min) {
            min = num3;
        }
        return min;
        }
    }