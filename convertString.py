#!/usr/local/bin/env python


def convertString(num, base):
    conv = "0123456789ABCDEF"
    if(num < base):
        return conv[num]
    return convertString(num // base, base) + conv[num % base]


def main():
    print convertString(34562, 16)
    print convertString(1234, 8)
    print convertString(345, 6)
    print convertString(345, 2)
    print convertString(565, 16)
    print convertString(345, 16)
    print convertString(12, 2)



if __name__ == '__main__':
    main()
