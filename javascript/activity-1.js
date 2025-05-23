/* Create a simple Grading System. Ask the user to input (using prompt) for Midterm Grade and Final Grade. The program then output (using alert) the Subject Grade, Equivalent and Remarks.
 Subject Grade = (Midterm + Finals) divided by 2
 Remarks = ""PASSED" grade>=60, otherwise "FAILED" */

 let midterm = Number(prompt("Enter Midterm Grade:"));
 let final = Number(prompt("Enter Final Grade:"));
 let subjectGrade = (midterm + final) / 2;
 let equivalent;

 if (subjectGrade >= 98) {
        equivalent = 4.00;
    } else if (subjectGrade >= 95) {
        equivalent = 3.75;
    } else if (subjectGrade >= 92) {
        equivalent = 3.50;
    } else if (subjectGrade >= 89) {
        equivalent = 3.25;
    } else if (subjectGrade >= 86) {
        equivalent = 3.00;
    } else if (subjectGrade >= 83) {
        equivalent = 2.75;
    } else if (subjectGrade >= 80) {
        equivalent = 2.50;
    } else if (subjectGrade >= 77) {
        equivalent = 2.25;
    } else if (subjectGrade >= 74) {
        equivalent = 2.00;
    } else if (subjectGrade >= 71) {
        equivalent = 1.75;
    } else if (subjectGrade >= 68) {
        equivalent = 1.50;
    } else if (subjectGrade >= 64) {
        equivalent = 1.25;
    } else if (subjectGrade >= 60) {
        eqyuivalent = 1.00;
    } else {
        equivalent = 0.00;
    }

if (subjectGrade >= 60) {
    alert(`Midterm Grade: ${midterm.toFixed(2)}\nFinal Grade: ${final.toFixed(2)}\n\nSubject Grade: ${subjectGrade.toFixed(2)}\nEquivalent: ${equivalent.toFixed(2)}\nRemarks: PASSED`);
}
    else {
        alert(`Midterm Grade: ${midterm.toFixed(2)}\nFinal Grade: ${final.toFixed(2)}\n\nSubject Grade: ${subjectGrade.toFixed(2)}\nEquivalent: ${equivalent.toFixed(2)}\nRemarks: FAILED`);
    }