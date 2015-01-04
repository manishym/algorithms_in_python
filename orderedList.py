#!/usr/local/bin/env python

from list import Node


class OrderedList():
    """An ordered linked list implementation in python"""
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, obj):
        temp = Node(obj)
        current = self.head
        previous = None
        if (current == None):
            self.head = temp
            return
        stop = False
        while current != None and not stop:
            if(obj > current.getData()):
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp.setNext(current)
        if(previous == None):
            self.head = temp
        else:
            previous.setNext(temp)
        return

    def size(self):
        count = 0
        curr = self.head
        while curr != None:
            count = count + 1
            curr = curr.getNext()
        return count

    def search(self, obj):
        current = self.head
        while current != None:
            if current.getData() == obj:
                return current
            if (current.getData() > obj):
                return False
            current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if(current.getData() == item):
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            return False
        if previous == None:
            self.head = self.head.getNext()
        previous.setNext(current.getNext())
        if current == self.tail:
            self.tail = previous
        return current

    def __repr__(self):
        s = "["
        current = self.head
        while current != None:
            s += str(current.getData())
            current = current.getNext()
            if(current):
                s += ", "
        s += "]"
        return s

    # def append(self, obj):
    #     current = self.head
    #     if(current == None):
    #         self.add(obj)
    #         return
    #     temp = Node(obj)
    #     self.tail.setNext(temp)
    #     self.tail = self.tail.getNext()


def main():
    l = OrderedList()
    l.add("foo")
    print l
    l.add("dog")
    print l
    l.add("Goobe")
    print l
    l.add("Nari")
    # print l
    print l
    # l.remove("haavu")
    # print l
    l.add("cat")
    print l
    l.add("haavu")
    print l
    l.add(1)
    print l
    l.add(2)
    print l
    l.add(3)
    print l
    l.add(4)
    print l
    l.add(10)
    print l
    l.add(5)
    print l
    l.add(11)
    print l

if __name__ == '__main__':
    main()
