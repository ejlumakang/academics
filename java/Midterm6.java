import java.util.Scanner;
class Midterm6 {

    public static void main(String[] args) {
        int x1, x2, y1, y2;
        double distance;

        Scanner sc = new Scanner(System.in);
        System.out.print("X1: ");
        x1 = sc.nextInt();
        System.out.print("Y1: ");
        y1 = sc.nextInt();
        System.out.print("X2: ");
        x2 = sc.nextInt();
        System.out.print("Y2: ");
        y2 = sc.nextInt();

        Midterm6 l = new Midterm6();
        distance = l.calculate_distance(x1, y1, x2, y2);
        System.out.println("Distance: " +String.format("%.2f", distance));

    }
    public double calculate_distance(int x1, int y1, int x2, int y2)
    {
        return Math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
    }
}