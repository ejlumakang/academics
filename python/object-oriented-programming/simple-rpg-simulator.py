import random


class Humanoids:
    def __init__(self, height, weight, haircolor, eyecolor):
        self.height = height
        self.weight = weight
        self.hairColor = haircolor
        self.eyeColor = eyecolor
        self.height = height
        self.strength = random.randint(1, 18)
        self.dexterity = random.randint(1, 18)
        self.constitution = random.randint(1, 18)
        self.intelligence = random.randint(1, 18)
        self.wisdom = random.randint(1, 18)
        self.charisma = random.randint(1, 18)

    def displayattributes(self):
        print(f"\nThese are your random attributes: ")
        print(f"Strength:{self.strength}")
        print(f"Dexterity:{self.dexterity}")
        print(f"Constitution:{self.constitution}")
        print(f"Intelligence:{self.intelligence}")
        print(f"Wisdom:{self.wisdom}")
        print(f"Charisma:{self.charisma}")


class Humans(Humanoids):
    def __init__(self, height, weight, haircolor, eyecolor):
        super().__init__(height, weight, haircolor, eyecolor)

    def add_bonus(self):
        attribute = input(
            "\nWhich attribute would you like to add 2 points to: (Strength, Dexterity, Constitution, Intelligence, "
            "Wisdom, Charisma):\n")
        attribute = attribute.lower()

        if attribute == 'strength':
            self.strength += 2
        elif attribute == 'dexterity':
            self.dexterity += 2
        elif attribute == 'constitution':
            self.constitution += 2
        elif attribute == 'intelligence':
            self.intelligence += 2
        elif attribute == 'wisdom':
            self.wisdom += 2
        elif attribute == 'charisma':
            self.charisma += 2
        else:
            return


class Dwarves(Humanoids):
    def __init__(self, height, weight, haircolor, eyecolor):
        super().__init__(height, weight, haircolor, eyecolor)

    def add_bonus(self):
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2
        self.magic_resistance = 20


class Elves(Humanoids):
    def __init__(self, height, weight, haircolor, eyecolor):
        super().__init__(height, weight, haircolor, eyecolor)

    def add_bonus(self):
        self.dexterity += 2
        self.charisma += 2
        self.sleep_resistance = 100


def charactercreation():
    clan = input("\nChoose your clan (Elf, Human, Dwarf): ")
    clanoptions = ["human", "elf", "dwarf"]
    while clan.lower() not in clanoptions:
        clan = input("The clan you chose is not an option. \nPlease choose from Human, Elf, or Dwarf: ")

    height = int(input("Enter a height between 3ft and 7ft: "))
    while not (3 <= height <= 7):
        height = int(input("The height you chose is not an option.\nYou may only enter a height between 3ft and 7ft: "))

    weight = input("Enter a weight between 60lbs - 300lbs: ")
    while not (60 <= int(weight) <= 300):
        weight = int(
            input("The weight you chose is not an option.\nYou may only enter a weight between 60lbs and 300lbs: "))

    haircolor = input(
        "Choose a hair color (White, Silver, Gray, Black, Brown, Green, Blue, Yellow, Pink, Red, or Blonde): ")
    hairoptions = ["white", "silver", "gray", "black", "brown", "green", "blue", "yellow", "pink", "red", "blonde"]
    while haircolor.lower() not in hairoptions:
        haircolor = input(
            "The hair color you chose is not an option.\nPlease choose only one of the following hair colors: White, "
            "Silver, Gray, Black, Brown, Green, Blue, Yellow, Pink, Red, or Blonde: ")

    eyecolor = input("Choose an eye color (White, Black, Red, Green, Blue, Brown, Purple, Amber): ")
    eyeoptions = ["white", "black", "red", "green", "blue", "brown", "purple", "amber"]
    while eyecolor.lower() not in eyeoptions:
        eyecolor = input(
            "The eye color you chose is not an option.\nPlease choose only one of the following eye colors: White, "
            "Black, Red, Green, Blue, Brown, Purple, Amber: ")

    if clan.lower() == 'human':
        character = Humans(height, weight, haircolor, eyeoptions)
        character.displayattributes()
        character.add_bonus()

    elif clan.lower() == 'elf':
        character = Elves(height, weight, haircolor, eyeoptions)
        character.displayattributes()
        character.add_bonus()

    elif clan.lower() == 'dwarf':
        character = Dwarves(height, weight, haircolor, eyeoptions)
        character.displayattributes()
        character.add_bonus()

    else:
        return

    print(f"\nYou have chosen the {clan.capitalize()} clan, your character traits are: ")
    print(f"Hair Color: {haircolor.lower()}")
    print(f"Eye Color: {eyecolor.lower()}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Strength: {character.strength}")
    print(f"Dexterity: {character.dexterity}")
    print(f"Constitution: {character.constitution}")
    print(f"Intelligence: {character.intelligence}")
    print(f"Wisdom: {character.wisdom}")
    print(f"Charisma: {character.charisma}")

    if clan.lower() == 'elf':
        print(f"{character.sleep_resistance}% Resistance to Sleep")
    elif clan.lower() == 'dwarf':
        print(f"{character.magic_resistance}% Resistance to Magic")
    else:
        return


def main():
    print(
        "Welcome to the Falls of Eternity. This is a simple RPG simulator written in Python. You may choose from the "
        "following playable races: \n\t1. Human \n\t2. Elf \n\t3. Dwarf")
    charactercreation()


if __name__ == "__main__":
    main()