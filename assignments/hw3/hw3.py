"""
Name: Joseph Decker
hw3.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def average():
    acc = 0
    total = 0
    inputs = (eval(input("How many grades will you enter?")))
    for _ in range(inputs):
        grade = eval(input("Enter grade: "))
        total = grade + total
        acc = acc + 1
    final_grade = total / acc
    print(final_grade)


def tip_jar():
    total = 0
    for i in range(5):
        donation = eval(input("How much would you like to donate?"))
        total = total + donation
    print(total)


def newton():
    number_1 = eval(input("What number would you like to square root?"))
    number_2 = eval(input("How many times should we improve the approximation?"))
    approx = number_1
    for _ in range(number_2):
        approx = (approx + (number_1/approx)) / 2
    print(approx)


def sequence():
    number = eval(input("Enter amount of numbers"))
    for x in range(0, number):
        y = 1 + (x // 2 * 2)
        print(y)


def pi():
    terms = eval(input("How many terms in the series?"))
    acc = 1
    for y in range(terms):
        num = 2 + (y // 2*2)
        denom = 1 + ((y + 1) // 2*2)
        acc = acc * (num / denom)
    print(acc * 2)


if __name__ == '__main__':
    pass
