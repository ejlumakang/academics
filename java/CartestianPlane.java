import java.util.Scanner;
class CartesianPlane {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x, y;
        System.out.print("x: ");
        x = sc.nextInt();
        System.out.print("y: ");
        y = sc.nextInt();

        if (x > 0 && y > 0)
            System.out.print("First Quadrant");
        else if (x < 0 && y > 0)
            System.out.print("Second Quadrant");
        else if (x < 0 && y < 0)
            System.out.print("Third Quadrant");
        else if (x > 0 && y < 0)
            System.out.print("Fourth Quadrant");
        else if (x == 0 && y > 0)
            System.out.print("Positive y-axis");
        else if (x == 0 && y < 0)
            System.out.print("Negative y-axis");
        else if (y == 0 && x < 0)
            System.out.print("Negative x-axis");
        else if (y == 0 && x > 0)
            System.out.print("Positive x-axis");
        else
            System.out.print("Origin");
    }
}