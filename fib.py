#/usr/local/bin/env python


def fib(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    for i in range(200):
        print "i: %3d, fib: %d" % (i, fib(i))

if __name__ == '__main__':
    main()
