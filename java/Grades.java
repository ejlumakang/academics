import java.util.Scanner;
public class Grades {
    public static void main(String[] args) {
    }
    {   Scanner sc = new Scanner(System.in);
        int total = 0;
        int counter = 0;
        int grade = 0;
        float average;

        System.out.println("Enter grade: ");
        grade = sc.nextInt();

        while (grade != -1) {
            total = total + grade;
            counter++;
        }
        if (counter != 0) {
            average = (float) total / counter;
            System.out.print("Class average is " + average);
        }

        else {
        System.out.print("No grades were entered)");
    }
    }
}