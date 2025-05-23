// Create a GUI-based Java program implementation of nPr, nCr, and Fibonacci series.

import javax.swing.*;

public class MathFunctions {

    public static void main(String[] args) {
        String inputN;
        String inputR;
        int n;
        int r;

        inputN = JOptionPane.showInputDialog("Enter n: ");
        n = Integer.parseInt(inputN);
        inputR = JOptionPane.showInputDialog("Enter r: ");
        r = Integer.parseInt(inputR);

        JOptionPane.showMessageDialog(null, n + "P" + r + " = " + nPr(n, r) + "\n" + n + "C" + r + " = " + nCr(n, r) + "\n" + "The " +n+ "th term is " +fib(n));

    }

    public static int factorial(int n) {
        if ((n == 0) || (n == 1)) {
            return 1;
        } else
            return n * factorial(n - 1);
    }

    public static int nPr(int n, int r) {
        if (n == r) {
            return 0;
        } else return factorial(n) / factorial(n - r);
    }

    public static int nCr(int n, int r) {
        return factorial(n) / (factorial(n - r) * factorial(r));
    }

    static int fib(int n) {
        if (n <= 1)
            return n;
        return fib(n - 1) + fib(n - 2);
    }
}