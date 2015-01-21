#/usr/local/bin/env python


class Deque():
    """A Python implementation of Deque"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def addFront(self, obj):
        self.items.append(obj)

    def removeRear(self):
        return self.items.pop(0)

    def addRear(self, obj):
        self.items.insert(0, obj)

    def removeFront(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        return "Deque: " + str(self.items)


def main():
    q = Deque()
    q.addRear("dog")
    q.addRear("Cat")
    q.addFront(100)
    print q
    print q.removeFront()
    print q.removeRear()
    print q


if __name__ == '__main__':
    main()
