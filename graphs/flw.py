#!/usr/bin/env python2
from graph import Graph, Vertex
from pythonds.basic import Queue



def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    # print start

    vertQueue.enqueue(start)

    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()

        for nbr in currentVert.getConnections():
            # print nbr, vertQueue.size()
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while(x.getPred()):
        print(x.getId())
        x = x.getPred()
    print x.getId()


def buildGraph(wordfile):
    d = {}
    g = Graph()
    wfile = open(wordfile, "r")
    for line in wfile:
        w = line[:-1]
        for i in range(len(w)):
            bucket = w[:i] + '_' + w[i+1:]
            if bucket in d:
                d[bucket].append(w)
            else:
                d[bucket] = [w]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def main():
    wg = buildGraph("fourletterwords.txt")
    bfs(wg, wg.getVertex('SAGE'))
    traverse(wg.getVertex('TOOL'))


if __name__ == '__main__':
    main()
