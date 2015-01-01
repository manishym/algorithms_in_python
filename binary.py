#!/usr/local/bin/env python
from stack import Stack


def binary_convert(s, base):
    p = Stack()
    while(s > 0):
        p.push(s % base)
        s = s / base

    s = ""
    while not p.isEmpty():
        s += str(p.pop())
    return s


def main():
    s = 1204
    s1 = 5
    s3 = 14
    print binary_convert(s, 2)
    print binary_convert(s1, 2)
    print binary_convert(s3, 2)
    print binary_convert(s, 3)
    print binary_convert(s1, 3)
    print binary_convert(s3, 3)

if __name__ == '__main__':
    main()
