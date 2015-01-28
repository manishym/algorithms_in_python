from pythonds.graphs import Graph, Vertex

def posToNodeId(row, col, bdSize):
	return row *bdSize + col

def legalCoord(x, bdSize):
	return x >= 0 and x < bdSize

def genLegalMoves(x, y, bdSize):
	newMoves = []
	moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2 ,1),
					(1, -2), (1, 2), (2, -1), (2, 1)]
	for i in moveOffsets:
		newX = x + i[0]
		newY = y + i[1]
		if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
			newMoves.append((newX, newY))
	return newMoves

def knightTour(n, path, u, limit):
	u.setColor('gray')
	path.append(u)
	if n < limit:
		nbrlist = list(u.getConnections())
		i = 0;
		done = False
		while i < len(nbrlist) and not done:
			if nbrlist[i].getColor() == 'white':
				done = knightTour(n+1, path, nbrlist[i], limit)
			i = i + 1
		if not done:
			path.pop()
			u.setColor('white')
			# print "Back tracking from %s" % u.getId()
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

def orderByAvail(n):
	resList = []
	for v in n.getConnections():
		if v.getColor() == 'white':
			c = 0
			for w in v.getConnections():
				if w.getColor() == 'white':
					c += 1
			resList.append((c, v))
	resList.sort(key = lambda x: x[0])
	return [y[1] for y in resList]
	
def knightTourFast(n, path, u, limit):
	u.setColor('gray')
	path.append(u)
	if(n < limit):
		nbrlist = orderByAvail(u)
		i = 0;
		done = False
		while i < len(nbrlist) and not done:
			if(nbrlist[i].getColor() == 'white'):
				done = knightTourFast(n+1, path, nbrlist[i], limit)
				i += 1
		if not done:
			path.pop()
			u.setColor('white')
	else:
		done = True
	return done

def bmain():
	g = knightGraph(8)
	path = []
	start = g.getVertex(4)
	done = knightTourFast(0, path, start, 63)
	print done
	for v in path:
		print v.getId()



def main():
	bmain()


if __name__ == '__main__':
	main()