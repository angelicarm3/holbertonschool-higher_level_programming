#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = ord(i)
        if char > 96 and char < 123:
            char -= 32
        print("{}".format(chr(char)), end="")
    print(end="\n")
