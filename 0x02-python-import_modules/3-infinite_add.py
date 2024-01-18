#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0
    lent = len(sys.argv)
    for i in range(1, lent):
        sum += int(sys.argv[i])
    print("{}".format(sum))
