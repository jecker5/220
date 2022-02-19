"""
Name: Joseph Decker
hw5.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("enter a name (first last)")
    name_split = name.split(" ")
    first = name_split[0]
    last = name_split[1]
    print(str(last) + ", " + str(first))


def company_name():
    domain = input("Enter a domain: ")
    company = domain.split(".")
    company_n = company[1]
    print(str(company_n))


def initials():
    students = eval(input("how many students are in the class? "))
    acc = 1
    for _ in range(students):
        name = input("what is the name of student " + str(acc) + "?")
        name_split = name.split(" ")
        last = name_split[1].split()
        first = name_split[0].split()
        first_i = first[0][0]
        last_i = last[0][0]
        print(first_i + last_i)


def names():
    name_l = input("enter a list of names")
    name_l = name_l.split(", ")
    for name in name_l:
        ini = name.split()
        print(ini[0][0] + ini[1][0])


def thirds():
    acc = 1
    sent = ""
    sent_num = eval(input("enter the number of sentences: "))
    for _ in range(sent_num):
        sentence = input("enter sentence " + str(acc) + ": ")
        acc += 1
        sent = sent + sentence[0::3]
    print(sent)


def word_average():
    acc = 0
    letters = 0
    sent = input("enter a sentence: ")
    words = sent.split(" ")
    for _ in words:
        current_word = words[acc]
        acc += 1
        for _ in current_word:
            letters += 1
    average = letters / acc
    print(average)


def pig_latin():
    word_list = input("enter a sentence to convert to pig latin: ")
    word_list = word_list.split()
    acc = 0
    index = 0
    current_word = ""
    for _ in word_list:
        letter = word_list[acc][index]
        word = word_list[acc][1:]
        new_word = word + letter + "ay"
        current_word = current_word + new_word.lower() + " "
        acc = acc + 1
    length = len(current_word)
    current_word = current_word[:length-1]
    print(current_word)


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    names()
    # thirds()
    # word_average()
    # pig_latin()
