#!/usr/bin/python3
lwc_letters = range(97, 123)
for lwc_letter in lwc_letters:
    if chr(lwc_letter) == 'q' or chr(lwc_letter) == 'e':
        continue
    print("{}".format(chr(lwc_letter)), end="")
