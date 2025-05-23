# Write a python program that will compute the final grade of a student.
# Final Grade is 30% average of 3 quizzes plus 20% average of 3 projects plus 30% of final exam grade plus 10% of assignment grade plus 10% class standing.

q1 = int(input("Quiz 1: "))
q2 = int(input("Quiz 2: "))
q3 = int(input("Quiz 3: "))

p1 = int(input("Project 1: "))
p2 = int(input("Project 2: "))
p3 = int(input("Project 3: "))

final_exam = (int(input("Final Exam: ")))
assignment = (int(input("Assignment: ")))
class_standing = (int(input("Class Standing: ")))

q_avg = q1 + q2 + q3/3
p_avg = p1 + p2 + p3/3

final_grade = 0.3 * q_avg + 0.2 * p_avg + 0.3 * final_exam + 0.1 * assignment + 0.1 * class_standing
print(final_grade) 