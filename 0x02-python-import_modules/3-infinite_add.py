#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = 0
    argv_len = len(sys.argv)

    for i in range(1, argv_len):
        number += int(sys.argv[i])
    print(number)
