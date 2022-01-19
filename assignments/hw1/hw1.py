"""
Name: Joseph Decker
hw1.py
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    pass


def calc_volume():
    length = eval(input("Enter the length"))
    width = eval(input("Enter the width"))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("Volume = ", volume)


def shooting_percentage():
    shots = eval(input("Enter the players total shots"))
    made = eval(input("Enter the amount of shots scored"))
    percent = (made / shots) * 100
    print("Shooting percentage = ", percent, "%")


def coffee():
    pounds = eval(input("How many pounds would you like?"))
    shipping = pounds * 0.86
    cost = pounds * 10.50
    total = shipping + cost + 1.50
    print("Your total is: ", total)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers / 1.61
    print("That's ", miles, "miles!")


if __name__ == '__main__':
    pass
