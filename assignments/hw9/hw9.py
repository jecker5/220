"""
Name: Joseph Decker
hw9.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint


def get_words(file_name):
    file = open(file_name, "r")
    words = list(file)
    return words


def get_random_word(words):
    acc = -1
    for _ in words:
        acc += 1
    random_number = randint(0, acc)
    secret = words[random_number]
    return secret[:-1]


def letter_in_secret_word(letter, secret_word):
    for char in secret_word:
        if char == letter:
            return True
    return False


def already_guessed(letter, guesses):
    for char in guesses:
        if char == letter:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    acc = []
    for letters in secret_word:
        if letters in guesses:
            acc.append(letters)
        else:
            acc.append("_")
    return " ".join(acc)


def won(guessed):
    for char in guessed:
        if char == "_":
            return False
    return True


def play_graphics():
    pass


def play_command_line(secret_word):
    guess_acc = 6
    guessed = []
    while guessed != secret_word:
        print("already guessed: " + str(guessed))
        print("Guesses remaining: " + str(guess_acc))
        print(make_hidden_secret(secret_word, guessed))
        current_g = input("Guess a letter: ")
        guessed.append(current_g)
        if not letter_in_secret_word(current_g, secret_word):
            guess_acc -= 1
            if guess_acc == 0:
                print(make_hidden_secret(secret_word, guessed))
                print("Sorry, you did not guess the word.")
                print("The secret word was: " + secret_word)
                return False
        if won(make_hidden_secret(secret_word, guessed)):
            print("winner!")
            print(secret_word)
            return True


if __name__ == '__main__':
    play_command_line(get_random_word(get_words("words.txt")))
    # play_graphics(secret_word)
