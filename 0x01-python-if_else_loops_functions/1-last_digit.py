#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if lastdigit > 5:
    print('Last digit of', number, 'is', lastdigit, 'and is greater 5')
elif lastdigit < 6 and lastdigit != 0:
    print('Last digit of', number, 'is', lastdigit, 'and is less than 6 and not 0')
else:
    print('Last digit of', number, 'is', lastdigit, 'and is 0')