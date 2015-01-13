#!/usr/bin/env python

from fractions import gcd
import random


class Monty:
    def __init__(self, choice):
        self.choices = ["Car", "Goat1", "Goat2"]
        random.shuffle(self.choices)
        self.you_won=self.choices[choice]
        self.choice = choice

    def what_you_won(self):
        return self.you_won

    def reveal(self):
        if(self.you_won == "Goat1"):
            return self.choices.index("Goat2")
        elif self.you_won == "Goat2":
            return self.choices.index("Goat1")
        return self.choices.index("Goat%d"%random.randrange(1,3))

    def switch(self):
        if(self.you_won == "Car"):
            return 0
        return 1

    def result(self):
        if self.you_won == "Car": 
            return 1
        return 0



def main():
    res = 0
    sw = 0
    for i in range(10000):
        m = Monty(random.randrange(3))
        m.reveal()
        res += m.result()
        sw += m.switch()
    print "Switch won %d times. \nRes won %d times" %(sw, res)




if __name__ == '__main__':
    main()