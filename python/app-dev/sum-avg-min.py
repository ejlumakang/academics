# Create a 5-input based that accept numbers and find sum, average and the smallest number of list in python.
# Note: Use sum() in adding the list and use len() in finding the average.

empty_list = []

for i in range(5):
    empty_list.append(int(input(f"Enter {i + 1} number: ")))

add = sum(empty_list)
average = add / len(empty_list)

min = empty_list[0]
for i in empty_list:
    if i < min:
        min = i

print(f"The sum is {add}.")
print(f"The average is {average}.")
print(f"The smallest number is {min}.")