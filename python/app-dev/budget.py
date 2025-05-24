# Create a  budgeting program that accept monthly salary using the Chinkee Tan approach (50/30/20 rule).
# Using this method, you would divide your earnings as follows:
# - Needs = 50% (Food, shelter, utilities)
# - Wants = 30% (Shopping, hobbies, dine-out)
# - Savings = 20% (Emergency fund)

salary = int(input("Input Salary: "))

print("\nMY MONTHLY BUDGET")

needs = salary * .5
foods = needs * .5
shelter = needs * .3
utilities = needs * .2

print("\n=====NEEDs=====")
print(f"Needs: {needs}")
print(f"Foods: {foods}")
print(f"Shelter: {shelter}")
print(f"Utilities: {utilities}")

wants = salary * .3
shopping = wants * .4
hobbies = wants * .15
dineout = wants *.45

print("\n=====WANTs=====")
print(f"Wants: {wants}")
print(f"Shopping: {shopping}")
print(f"Hobbies: {hobbies}")
print(f"Dine-out: {dineout}")

savings = salary * .2
emergency_fund = savings * .7
jar = savings * .3

print("\n=====Saving=====")
print(f"Savings: {savings}")
print(f"Emergency: {emergency_fund}")
print(f"Jar: {jar}\n")

print("================")
print(f"Total: {salary}")