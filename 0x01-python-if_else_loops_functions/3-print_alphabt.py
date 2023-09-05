#!/usr/bin/python3
# program that prints the ASCII alphabet in lowercase,
# excluding the letters 'q' and 'e', not followed by a new line.

for letter in range(97, 123):
    if letter not in (113, 101):
        print("{}".format(chr(letter)), end="")
