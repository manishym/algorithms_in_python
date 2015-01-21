#/usr/local/bin/env python


class Queue():
    """A Python implementation of queue"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, obj):
        self.items.insert(0, obj)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        return "Queue: " + str(self.items)


def main():
    q = Queue()
    q.enqueue("dog")
    q.enqueue("Cat")
    q.enqueue(100)
    print q
    q.dequeue()
    q.dequeue()
    print q



if __name__ == '__main__':
    main()
