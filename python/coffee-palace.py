class Customers:
    greeting = "Welcome to Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

    def info(self):
        return f"Name = {self.name} || Beverage = {self.beverage} || Food = {self.food} || Total = {self.total}"


c_1 = Customers("Nate   ", "Espresso              ", "Pastrami on rye   ", 220)
c_2 = Customers("Elaine ", "Strawberry frappuccino", "Tuna wrap         ", 270)
c_3 = Customers("Samirah", "Iced caffe latte      ", "Cinnamon roll     ", 225)
c_4 = Customers("Jerry  ", "Caramel macchiato     ", "Glazed doughnut   ", 230)
c_5 = Customers("Paz    ", "Iced tea              ", "Blueberry pancakes", 315)

print(Customers.greeting)
print("=========================\n")
print(c_1.info())
print(c_2.info())
print(c_3.info())
print(c_4.info())
print(c_5.info())