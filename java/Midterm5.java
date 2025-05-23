import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class Midterm5 {

	public static void main (String args[]) throws FileNotFoundException
	{
		Scanner A = new Scanner (new FileReader("Student.txt"));
		PrintWriter B = new PrintWriter("Report.txt");
		
		B.println("ITCS123 - Intermediate Programming");
		B.println("BIT22");
		B.println("1st Semester, SY 2021-2022");
		B.println("by: Eloiza Lumakang");
		B.println("--------------------");
		B.println("Name\t\t\t\tMidterm\t\t\t\tFinals\t\t\t\tAverage\t\t\t\tRemarks");
		
		String name, remarks;
		double midterm, finals, average = 0;
			
			for (int i=1; i<=10; i++){
					
			name= A.next();
			midterm = A.nextDouble();
			finals = A.nextDouble();
			average = (midterm + finals)/2;
		
				if (average>=60){
					remarks = "Passed";
					}
				else {
					remarks ="Failed";
					}
		B.println(name  +"\t\t\t"+  midterm  +"\t\t\t"+ finals  +"\t\t\t"+ average +"\t\t\t"+ remarks);
			}
	
		A.close();
		B.close();
}
}