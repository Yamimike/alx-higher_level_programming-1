#!/usr/bin/python3
numbers = range(0, 100)
for number in numbers:
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
