#/usr/local/bin/env python

from dqueue import Deque


def palchecker(s):
    dq = Deque()
    for c in s:
        dq.addRear(c)
    palindrome = True
    while palindrome == True and dq.size() > 1:
        if(dq.removeFront() != dq.removeRear()):
            palindrome = False
    return palindrome


def main():
    st = ["radar", "madam", "adam", "malayalam", "foobar"]
    for s in st:
        res = palchecker(s)
        if res:
            pal = "is palindrome"
        else:
            pal = "is not palindrome"
        print "%s %s" % (s, pal)

if __name__ == '__main__':
    main()
