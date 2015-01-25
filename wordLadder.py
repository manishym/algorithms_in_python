#!/usr/local/bin/env python

from graphs import Graph, Vertex
from queue import Queue


def build_graph(wordfile):
    d = {}
    g = Graph()
    wfile = open(wordfile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currVertex = vertQueue.dequeue()
        for nbr in currVertex.getConnections():
            if(nbr.getColor() == "white"):
                nbr.setPred(currVertex)
                nbr.setColor("grey")
                vertQueue.enqueue(nbr)
                nbr.setDistance(currVertex.getDistance() + 1)
        currVertex.setColor("black")
        # print currVertex.getId()

def traverse(y):
    x = y
    while x:
        print(x.getId())
        x = x.getPred()
    # print x.getId()


def main():
    g = build_graph("wordfile.txt")
    bfs(g, g.getVertex("fool"))
    print g.getVertex("sage")
    traverse(g.getVertex("sage"))
    # for v in g:
        # print v


if __name__ == '__main__':
    main()
