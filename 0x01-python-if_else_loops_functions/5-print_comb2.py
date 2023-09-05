#!/usr/bin/python3

# program that prints numbers from 0 to 99

output = ""
for number in range(100):
    output += "{:02d}".format(number)
    if number != 99:
        output += ", "
print(output)
