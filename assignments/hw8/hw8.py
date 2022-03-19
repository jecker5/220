"""
Name: Joseph Decker
hw8.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import GraphWin
from graphics import Circle


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] += 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]
    return total


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    for i in nums:
        nums = i.split(", ")
        print(nums)
        to_numbers(nums)
        square_each(nums)


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    pass


if __name__ == '__main__':
    pass
