"""
Name: Joseph Decker
hw7.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from encryption import encode


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    acc = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(acc))
            acc += 1
            outfile.write(" ")
            outfile.write(word)
            outfile.write("\n")


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage = wage + 1.65
        wage = wage * int(parts[3])
        outfile.write(parts[0])
        outfile.write(" ")
        outfile.write(parts[1])
        outfile.write(" ")
        outfile.write("{:.2f}".format(wage))
        outfile.write("\n")


def calc_check_sum(isbn):
    acc = 0
    isbn = isbn.replace('-', '')
    for i in range(10):
        pos = 10 - i
        acc += (pos * int(isbn[i]))
    return acc


def send_message(file_name, friend_name):
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(line)


def send_safe_message(file_name, friend_name, key):
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))
        outfile.write("\n")


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
