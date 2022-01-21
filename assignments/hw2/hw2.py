"""
Name: Joseph Decker
hw2.py

Problem: calculate multiple things such as sum of threes, triangle area, etc.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    acc = 0
    total = 0
    upper = eval(input("what is the upper bound?"))
    for _ in range(upper):
        if acc+3 <= upper:
            acc = acc + 3
            total = acc + total
    print(total)


def multiplication_table():
    for length in range(1, 11):
        for width in range(1, 11):
            print(length*width, end="\t")
        print()


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    perimeter = (side_a + side_b + side_c) / 2
    area = math.sqrt(perimeter*(perimeter-side_a)*(perimeter-side_b)*(perimeter-side_c))
    print(area)


def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    total = 0
    for _n_ in range(lower, upper + 1):
        total = (_n_ ** 2) + total
    print(total)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    total = base ** exponent
    print(base, "^", exponent, " = ", total)


if __name__ == '__main__':
    pass
