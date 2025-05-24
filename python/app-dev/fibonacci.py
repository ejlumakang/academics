# Create a Python program that generates Fibonacci number sequence and find their square in the given sequence based on the user input.
# Condition:
# - Fibonacci sequence should be in list format.
# - User input should be only positive input.

empty_list = []
n1, n2 = 0, 1
count = 0
temp = 0

# Takes user input
user_input = int(input("Enter the number of Fibonacci number: "))

# Input only accepts positive value
if user_input <= 0:
    print("\nNumber of Fibonacci numbers should be a positive integer.")

else:
    for i in range(user_input): # For loop that iterates user input
        empty_list.append(n1) # Appends current n1 value to list
        temp = n2 # Stores value of n2 to temp variable
        n2 = n1 + n2 # Update value of n2 by adding n1 to previous value n2
        n1 = temp # Update value of n1 by adding to previous value of n2 
        
    print(f"\nFibonacci sequence of {user_input} numbers:")
    print(empty_list)
    print()

for i in range(user_input): # For loop that iterates user input
    square = empty_list[i] ** 2 # Squares the current index of the list
    print(f"Fibonacci number ({i + 1}): {empty_list[i]}, Square: {square}")