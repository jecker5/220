"""
Name: Joseph Decker
hw10.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def fibonacci(n):
    if n < 1:
        return None
    elif n == 1:
        return 1
    else:
        num1 = 0
        num2 = 1
        acc = 0
        while acc != n:
            acc = acc + 1
            num3 = num1 + num2
            num1 = num2
            num2 = num3
    return num1


def double_investment(principle, rate):
    new_rate = rate + 1
    double_principle = principle * 2
    acc = 0
    while principle < double_principle:
        principle = principle * new_rate
        acc = acc + 1
    return acc


def syracuse(n):
    n_list = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            n_list.append(n)
        elif n % 2 == 1:
            n = (n*3) + 1
            n_list.append(n)
    return n_list


def goldbach(n):
    n_list = []
    if n % 2 == 0:
        n1 = n / 2
        n_list.append(int(n1))
        n_list.append(int(n1))
    else:
        return None
    return n_list
