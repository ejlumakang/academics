import java.util.Scanner;
public class Exam {
    public static void main(String[] args) {

        int grade;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Grade: ");
        grade = sc.nextInt();

        if (grade >= 60) {
            System.out.print("Passed");
        } else {
            System.out.print("Failed");
        }
    }
}