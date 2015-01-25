#!/usr/local/bin/env python
import random


class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.pred = None
        self.distance = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " Connected to: " + str([i for i in self.connectedTo])

    def __repr__(self):
        return "(Name: %s, Color: %s)" % (self.id, self.color)

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr].weight

    def setColor(self, color):
        self.color = color
        return self.color

    def setPred(self, pred):
        self.pred = pred
        return self.pred

    def getColor(self):
        return self.color

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d
        return self.distance



class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVerticies = 0

    def addVertex(self, key):
        self.numVerticies += 1
        nv = Vertex(key)
        self.vertList[key] = nv
        return nv

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def addEdge(self, v1, v2, weight=0):
        if v1 not in self.vertList:
            nv = self.addVertex(v1)
        if v2 not in self.vertList:
            self.addVertex(v2)
        self.vertList[v1].addNeighbor(self.vertList[v2], weight)

    def getVerticies(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def testGraph(num_nodes):
    g = Graph()
    for i in range(num_nodes):
        g.addVertex(i)

    for i in range(num_nodes):
        for j in range(num_nodes):
            edge = random.randrange(2)
            weight = random.randrange(1, num_nodes)
            if(edge == 1):
                g.addEdge(i, j, weight)


    for v in g:
        for w in v.getConnections():
            print "(%s, %s)" % (v.getId(), w.getId())

def main():
    testGraph(6)


if __name__ == "__main__":
    main()
