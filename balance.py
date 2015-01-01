#!/usr/local/bin/env python
from stack import Stack


def check_balance(s):
    p = Stack()
    op = "{[("
    cl = "}])"

    balance = True
    for char in s:
        if(char in op):
            p.push(char)
        elif char in cl:
            temp = p.pop()
            balance = (op.index(temp) == cl.index(char))
            if not balance:
                return False
    if p.isEmpty():
        return True

    return False


def main():
    s = "{{[[]]}}(())({})"
    s1 = "{{[]}(})"
    s3 = "{}"
    print check_balance(s)
    print check_balance(s1)
    print check_balance(s3)


if __name__ == '__main__':
    main()
