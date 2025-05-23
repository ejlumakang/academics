import java.util.Scanner;
public class ArraySum {
    private static int sum;

    public static void main(String[] args) {

        System.out.println("Enter the elements of the array: ");

        int[] array = new int[5];
        Scanner scan = new Scanner(System.in);

        for (int i = 0; i < array.length; i++) {

            array[i] = scan.nextInt();
        }
            arraySum(array);
        }
        public static void arraySum (int[] array){
            for (int i : array) {
                sum += i;
            }
        System.out.println("The sum is: " +sum);
            }
    }