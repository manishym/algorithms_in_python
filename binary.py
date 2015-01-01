#!/usr/local/bin/env python
from stack import Stack


def binary_convert(s):
    p = Stack()
    while(s > 0):
        p.push(s % 2)
        s = s / 2

    s = ""
    while not p.isEmpty():
        s += str(p.pop())
    return s


def main():
    s = 1204
    s1 = 5
    s3 = 14
    print binary_convert(s)
    print binary_convert(s1)
    print binary_convert(s3)


if __name__ == '__main__':
    main()
