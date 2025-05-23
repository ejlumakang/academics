class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display(self):
        print(f"Name: {self.name} Birthday: {self.birthday} Age:{self.age} food: {self.favorite_food} Goal: {self.goal}")

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        super().__init__(name, birthday, age, favorite_food, goal)
        self.position = position

    def display(self):
        super().display()
        print(f"Position: {self.position}")

cm = ClubMembers("Tom", "Jan 16", 14, "Ice cream", "To be happy")
co = ClubOfficers("Vera", "June 22", 16, "Beef Stroganoff", "To be the world's greatest chef", "Treasurer")

cm.display()
print()
co.display()




