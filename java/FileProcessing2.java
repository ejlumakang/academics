import java.util.*;
import java.io.*;

public class FileProcessing2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner inFile = new Scanner (new FileReader("/Users/eloizajoy/Desktop/grade.dat"));

        PrintWriter outfile = new PrintWriter("average.txt");
        String firstName;
        String lastName;

        double sum = 0;

        firstName = inFile.next();
        lastName = inFile.next();

        while(inFile.hasNextInt()){
            sum += inFile.nextInt();
        }

        outfile.println(firstName+ " " +lastName+ "'s average grade is: " +sum/5+ "!");

        inFile.close();
        outfile.close();

    }
}