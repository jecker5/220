"""
Name: Joseph Decker
hw4.py

Problem: Create functions using the graphics library

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for _ in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 20, p.getY() - 20), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)
    point1 = win.getMouse()
    point2 = win.getMouse()
    rect = Rectangle(point1, point2)
    rect.draw(win)
    length = abs(point2.getX() - point1.getX())
    width = abs(point2.getY() - point1.getY())
    area = length * width
    area_txt = Text(Point(200, 350), "The area = " + str(area))
    perimeter = 2 * (length + width)
    perimeter_txt = Text(Point(200, 360), "The perimeter = " + str(perimeter))
    area_txt.draw(win)
    perimeter_txt.draw(win)

    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)
    click_1 = win.getMouse()
    click_2 = win.getMouse()
    x_1 = click_1.getX()
    y_1 = click_1.getY()
    x_2 = click_2.getX()
    y_2 = click_2.getY()
    radius = ((x_2-x_1)**2 + (y_2-y_1)**2)**0.5
    c = Circle(click_1, radius)
    c.draw(win)
    radius_text = Text(Point(200, 340), "The radius is: " + str(radius))
    radius_text.draw(win)

    win.getMouse()
    win.close()


def pi2():
    terms = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range(terms):
        num = 4 * ((-1)**i)
        denom = 1 + (2 * i)
        acc += num/denom

    print("Pi approximation: " + str(acc))
    accuracy = math.pi - acc
    print("accuracy: " + str(accuracy))



def main():

    # squares()
    # rectangle()
    # circle()
    pi2()


main()


if __name__ == '__main__':
    pass
