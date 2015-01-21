#!/usr/local/bin/env python
from queue import Queue
import random


class Task():
    """Simulate a task for a printer"""
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def  getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, time):
        return time - self.timestamp


class Printer():
    """A class to simulate printer"""
    def __init__(self, ppm):
        self.ppm = ppm
        self.current_task = None
        self.timeRemaining = 0

    def tick(self):
        if(self.current_task != None):
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining < 0:
                self.current_task = None  # schedule

    def busy(self):
        return self.current_task != None

    def startNext(self, new):
        self.current_task = new
        self.timeRemaining = new.getPages() * 60 / self.ppm


def newPrintTask():
    num = random.randrange(1, 181)
    return num == 180


def simulation(numSeconds, ppm):
    p = Printer(ppm)
    q = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if(newPrintTask()):
            task = Task(currentSecond)
            q.enqueue(task)

        if ((not p.busy()) and (not q.isEmpty())):
            nextTask = q.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            p.startNext(nextTask)
        p.tick()

    avg = sum(waitingTimes) / len(waitingTimes)
    print "Average wait time of %6.2f Seconds. Tasks in queue %3d" % (avg, q.size())



def main():
    for i in range(10):
        simulation(3600, 5)


if __name__ == '__main__':
    main()
