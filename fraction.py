#!/usr/bin/env python

from fractions import gcd

class Fraction:
    def __init__(self, top, bottom):
        self.num = top/gcd(top, bottom)
        self.den = bottom/gcd(top, bottom)

    def __str__(self):
        if self.num != self.den:
            return str(self.num) + "/" + str(self.den) 
        return str(1)

    def __repr__(self):
        if self.num != self.den:
            return "Fraction" +": "+ str(self.num) + "/" + str(self.den) 
        return str(1)

    def __add__(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - self.den * other.num, self.den * other.den)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __div__(self, other):
        return Fraction(self.num * other.den, other.num * self.den) 

    def __mul__(self, other):
        return Fraction(self.num * other.num, other.den * self.den) 
    
    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num




def buildlist(range):
    a = []
    for i in range(range):
        a.append(i)
    return a


