# Create a 5-user input list that accept either string or number then select an item randomly from a list and remove the selected item randomly in the list.

import random

empty_list = []

for i in range(5):
    empty_list.append(input(f"Enter a string or number: "))

choice = random.choice(empty_list)

print(f"Randomly selected item: {choice}")

for i in empty_list:
    if i == choice:
        empty_list.remove(i)
        break

print(empty_list)