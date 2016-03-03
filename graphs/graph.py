#!/usr/bin/env python
import sys


def _addMethod(fldName, clsName, verb, methodMaker, dict):
    """Make a get or set method and add it to dict."""
    compiledName = _getCompiledName(fldName, clsName)
    methodName = _getMethodName(fldName, verb)
    dict[methodName] = methodMaker(compiledName)


def _getCompiledName(fldName, clsName):
    """Return mangled fldName if necessary, else no change."""
    # If fldName starts with 2 underscores and does *not* end with 2 underscores...
    if fldName[:2] == '__' and fldName[-2:] != '__':
        return "_%s%s" % (clsName, fldName)
    else:
        return fldName


def _getMethodName(fldName, verb):
    """'_salary', 'get'  => 'getSalary'"""
    s = fldName.lstrip('_') # Remove leading underscores
    return verb + s.capitalize()


def _makeGetter(compiledName):
    """Return a method that gets compiledName's value."""
    return lambda self: self.__dict__[compiledName]


def _makeSetter(compiledName):
    """Return a method that sets compiledName's value."""    
    return lambda self, value: setattr(self, compiledName, value)


class Accessors(type):

    """Adds accessor methods to a class."""
    def __new__(cls, clsName, bases, dict):
        for fldName in dict.get('_READ', []) + dict.get('_READ_WRITE', []):
            _addMethod(fldName, clsName, 'get', _makeGetter, dict)
        for fldName in dict.get('_WRITE', []) + dict.get('_READ_WRITE', []):
            _addMethod(fldName, clsName, 'set', _makeSetter, dict)
        return type.__new__(cls, clsName, bases, dict)


class Vertex(object):

    """a vertex in a graph."""
    __metaclass__ = Accessors
    _READ_WRITE = ['color', 'distance', 'pred', 'disc', 'fin', 'id']
    def __init__(self, key):
        super(Vertex, self).__init__()
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.id) + ' color: ' + self.getColor() + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]




class Graph(object):

    """a graph class."""

    def __init__(self):
        super(Graph, self).__init__()
        self.verticies = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)

        self.verticies[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.verticies:
            return self.verticies[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verticies

    def addEdge(self, f, t, cost=0):
        if f not in self.verticies:
            nv = self.addVertex(f)
        if t not in self.verticies:
            nv = self.addVertex(t)
        self.verticies[f].addNeighbor(self.verticies[t], cost)

    def getVertices(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())
