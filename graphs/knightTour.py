#!/usr/bin/env python

from graph import Graph, Vertex



def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    done = False
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done




def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, col, board_size):
    return row * board_size + col


def legalCoord(x, bdsize):
    return x >= 0 and x < bdsize


def genLegalMoves(x, y, bdsize):

    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, 2), (1, -2), (2, -1), (2, 1)]

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdsize) and legalCoord(newY, bdsize):
            newMoves.append((newX, newY))

    return newMoves


def main():
    path = []
    ktGraph = knightGraph(6)
    knightTour(0, path, ktGraph.getVertex(0), 63)
    print path

if __name__ == '__main__':
    main()