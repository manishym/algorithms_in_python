#!/usr/local/bin/env python
from queue import Queue


def hotpotato(names, number):
    q = Queue()
    for name in names:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(number):
            q.enqueue(q.dequeue())
        print q.dequeue() + " is out"
    return q.dequeue()


def main():
    print hotpotato(["Manish", "Dashi", "Guru", "1t", "Mayura", "Raj", "Sapna"], 5) + " Wins"

if __name__ == '__main__':
    main()
