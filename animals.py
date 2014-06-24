from Sheep import *
from Cow import *

def display_menu():
    print()
    print("Which animal would you like to create?")
    print()
    print("1.Cow")
    print("2.Sheep")
    print()
    print("Please select an option from the menu above")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            print()
            if choice in (1,2):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Cow()
    elif choice == 2:
        new_animal = Sheep()
    return new_animal

def main():
    new_animal = create_animal()
    manage_animal(new_animal)

if __name__ == "__main__":
    main()
