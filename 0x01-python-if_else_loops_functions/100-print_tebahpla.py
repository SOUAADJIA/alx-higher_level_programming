#!/usr/bin/python3
output = ""
for i in range(122, 96, -1):
    if i % 2 == 0:
        output += "{:c}".format(i)
    else:
        output += "{:c}".format(i - 32)

print(output, end='')
