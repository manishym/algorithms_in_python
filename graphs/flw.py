#!/usr/bin/env python2
from graph import Graph


def buildGraph(wordfile):
    d = {}
    g = Graph()
    wfile = open(wordfile, "r")
    for line in wfile:
        w = line[:-1]
        for i in range(len(w)):
            if bucket in d:
                