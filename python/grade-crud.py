columns = ["Student No", "Name", "Quiz 1", "Quiz 2", "Quiz 3", "CP", "Final Exam", "Grade", "Remarks"]
student_values = []


def calculateGrade(student):
    quiz_scores = [int(student[2]), int(student[3]), int(student[4])]  # Get specific indices and store in a variable                         
    quiz_average = sum(quiz_scores) / 3
    class_participation = int(student[5])
    final_exam = int(student[6])
    total_grade = (quiz_average * 0.4) + (class_participation * 0.1) + (final_exam * 0.5)
    remarks = "PASSED" if total_grade >= 75 else "FAILED"

    student[7] = f"{total_grade:.2f}"     # Set index 7 to total_grade
    student[8] = remarks                  # Set index 8 to remarks


def create():
    student_values.clear()  #Clears data everytime user picks option 1
    print("STUDENT NO - NAME - Q1 - Q2 - Q3 - CP - FINAL EXAM")
    for i in range(5):
        values = input(f"Enter the values for Student {i + 1} (separated with spaces): ").split()
        if len(values) != 7: # If user input is not equal to 7
            print("\nInvalid input.\n")
            break
        else:
            student = values
            student.extend(["", ""])  # Add two empty strings for index 7 and 8 to avoid error
            calculateGrade(student)   # Manually computes index 7 and 8
            student_values.append(student)


def read():
    print("|".join(f"{col.center(12)}" for col in columns))
    for student in student_values:
        print("|".join(f"{value.center(12)}" for value in student))
    print()


def update():
    student_num = int(input("Enter the student number to update (1-5): ")) - 1
    if 0 <= student_num < len(student_values):
        new_values = input(f"Enter the updated values for Student {student_num + 1}: ").split()
        if len(new_values) == 7:
            student_values[student_num][:7] = new_values  # Updates the indices 0-6, 7-8 are manually computed
            calculateGrade(student_values[student_num])
            print("\nStudent data updated successfully.\n")
        else:
            print("\nInvalid input.\n")
    else:
        print("\nInvalid student number.\n")


def delete():
    student_num = int(input("Enter the student number to delete (1-5): ")) - 1
    if 0 <= student_num < len(student_values):
        student_values[student_num] = [""] * 9  # Creates a list of 9 empty strings
        print(f"\nStudent {student_num + 1} data deleted.\n")
    else:
        print("\nInvalid student number.\n")


while True:
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("\nInvalid choice. Please select a valid option.\n")