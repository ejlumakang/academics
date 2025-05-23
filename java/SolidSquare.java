public class SolidSquare {
    public static void main(String[] args) {
        {
            final int rows = 4,
                    columns = 10;

            for (int i = 1; i <= rows; i++) {
                for (int j = 1; j <= columns; j++) {
                    System.out.print("*");
                }

                System.out.println();
            }
        }
    }
}
