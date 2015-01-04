#!/usr/local/bin/env python

class Node():
    """A linked list node in python"""
    def __init__(self, item):
        self.item = item
        self.next = None

    def getData(self):
        return self.item

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node
        return node

    def setData(self, data):
        self.item = data
        return data

class UnorderedList():
    """A linked list implementation in python"""
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, obj):
        temp = Node(obj)
        temp.setNext(self.head)
        self.head = temp

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

    def append(self, obj):
        current = self.head
        if(current == None):
            self.add(obj)
            return
        temp = Node(obj)
        previous = None
        while(current != None):
            previous = current
            current = current.getNext()
        previous.setNext(temp)


def main():
    l = UnorderedList()
    l.add("foo")
    l.add(3)
    l.add("dog")
    l.remove(3)
    l.add("Goobe")
    l.append("Nari")
    print l


if __name__ == '__main__':
    main()

