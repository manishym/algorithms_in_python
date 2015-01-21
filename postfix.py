#!/usr/local/bin/env python
from stack import Stack


def postfix(s):
    ops = Stack()
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    exp = []
    inp = s.split()
    # print inp

    for char in inp:
        if(char in operands):
            exp.append(char)
        elif(char == '('):
            ops.push(char)

        elif(char == ')'):
            top = ops.pop()
            while top != '(':
                exp.append(top)
                top = ops.pop()
        else:
            ops.push(char)

    while (not ops.isEmpty()):
        exp.append(ops.pop())
    return " ".join(exp)


def main():
    print (postfix("A + B * C"))
    print (postfix("A + B * C + D"))
    print (postfix("( A + B ) * ( C + D )"))

#pooja gupta prestige


if __name__ == '__main__':
    main()
