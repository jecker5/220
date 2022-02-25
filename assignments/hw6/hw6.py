"""
Name: Joseph Decker
hw6.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import unicodedata
import math


def cash_converter():
    integer = eval(input("enter an integer: "))
    value = "${:.2f}".format(integer)
    print("That is", value)


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    acc = ""
    for i in message:
        c = ord(i)
        i = chr(key+c)
        acc += i
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = 4/3 * math.pi * (radius ** 3)
    return volume


def sum_n(number):
    acc = 1
    total = 0
    for _ in range(number):
        total = acc + total
        acc += 1
    return total


def sum_n_cubes(number):
    acc = 1
    total = 0
    for _ in range(number):
        total += acc ** 3
        acc += 1
    return total


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    acc = ""





if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
