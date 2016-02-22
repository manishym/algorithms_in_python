#!/usr/local/bin/env python

from pythonds.graphs import Graph


class DFSGraph(Graph):
	"""docstring for DFSGraph"""
	def __init__(self, arg):
		super(DFSGraph, self).__init__()
		self.time = 0

	def dfs(self):
		for aVertex in self:
			aVertex.setColor('white')
			aVertex.setPred(-1)
		for aVertex in self:
			if(aVertex.getColor == 'white'):
				self.depth_search(aVertex)

	def depth_search(self, v):
		v.setColor('grey')
		self.time += 1
		v.setDiscoveryTime(self.time)
		for nbr in v.getConnections():
			nbr.setPred(v)
			self.depth_search(nbr)

		v.setColor('black')
		self.time += 1
		v.setFinish(self.time)
		

def main():
	pass


if __name__ == '__main__':
	main()