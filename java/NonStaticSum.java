//Module 4 - Methods
//Non-Static Method
//Addition Program

import javax.swing.*;

public class NonStaticSum
{
    public static void main(String args[])
    {
        String num1, num2;
        int n1, n2, sum;

        num1 = JOptionPane.showInputDialog(null,"Enter first integer:");
        n1 = Integer.parseInt(num1);

        num2 = JOptionPane.showInputDialog(null,"Enter second integer:");
        n2 = Integer.parseInt(num2);

        NonStaticSum ADD = new NonStaticSum();

//Create an Object ADD to call the Non-static Method Addition

        sum = ADD.Addition(n1, n2);

//METHOD CALL - calls the method Addition using the ADD object and pass the values of n1 and n2 to a and b

        JOptionPane.showMessageDialog(null,"The sum is " + sum);

    }

    public int Addition(int n1, int n2) //Non-Static Method Addition
    {
        int sum;
        sum = n1 + n2;
        return sum;
    }
}