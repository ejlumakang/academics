import javax.swing.JOptionPane;

public class TernarySearch {
    public static void main(String[] args) {

        String input = JOptionPane.showInputDialog("Enter a sorted array:");
        String[] elements = input.split(" ");                           //the elements that the user inputs separated by white spaces

        int[] array = new int[elements.length];             //the size of elements stored to the array
        for (int i = 0; i < elements.length; i++) {
            array[i] = Integer.parseInt(elements[i]);       //allocate each element to array
        }

        int target = Integer.parseInt(JOptionPane.showInputDialog("Enter the target value:"));

        int result = ternarySearch(array, target);
        if (result == -1) {
            JOptionPane.showMessageDialog(null, "Target value not found in the array.");
        } else {
            JOptionPane.showMessageDialog(null, "Target value found at index: " + result);
        }
    }

    private static int ternarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid1 = left + (right - left) / 3;       //find m1
            int mid2 = right - (right - left) / 3;      //find m2

            if (array[mid1] == target) {                //if key is in m1
                return mid1;
            }

            if (array[mid2] == target) {                //if key is in m2
                return mid2;
            }

            if (target < array[mid1]) {             //if key is less than m1
                right = mid1 - 1;                   //if key is between left and m1
            } else if (target > array[mid2]) {      //if key is greater than m2
                left = mid2 + 1;                    //if key is between m2 and r
            } else {
                left = mid1 + 1;                    //if key is lies between m1
                right = mid2 - 1;                   //if key is lies between m2
            }
        }

        return -1;
    }
}
