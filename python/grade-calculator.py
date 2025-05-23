print("Name: Eloiza Joy B. Lumakang")
print("Course/Year/Section: BSCS", "\n")

at = int(input("Attendance: "))
cp = int(input("Class Participation: "))
atcp = int(((at + cp)/30)*0.2*100)
print("20% of Attendance/Class Participation: ", str(atcp), "\n")

sq1 = int(input("Short Quiz 1: "))
sq2 = int(input("Short Quiz 2: "))
sq3 = int(input("Short Quiz 3: "))
le = int(input("Long Exam: "))

ea = int(((sq1+sq2+sq3+le)/60)*.5*100)
print("50% of Enabling Assessment: ", str(ea), "\n")

se = int(input("Summative Exam: "))
se2 = int((se/50)*.3*100)
print("30% of Summative Exam: ", str(se2), "\n")

to = int(atcp+cp+ea+se)
if to >= 60:
    print("You Passed!")
else:
    print("You failed!")