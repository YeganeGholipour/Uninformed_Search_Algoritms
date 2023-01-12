# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 23:06:22 2023

@author: user
"""

from queue import PriorityQueue

# class Graph:
#     def __init__(self):
#         self._graph = {}
#         self._vertexNo = 0
#     def add_vertex(self, v):
#         if v in self._graph:
#             print('The vertex Already Exsits!')
#         else:
#             self._graph[v] = []
#             self._vertexNo += 1
#     def add_edges(self, v1, v2, w):
#         if v1 not in self._graph:
#             print(f'{v1} does not exist in the graph!')
#         elif v2 not in self._graph:
#             print(f'{v2} does not exist in the graph!')
#         else:
#             self._graph[v1].append([v2, w])
#             self._graph[v2].append([v1, w])
#     def __len__(self):
#         return len(self._graph)
#     def __getitem__(self, v):
#         return self._graph[v]
#     def show_graph(self):
#         return(self._graph)
    
import GraphsTrees

graph = GraphsTrees.Graph()

graph.add_vertex('s')
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')
graph.add_vertex('e')
graph.add_vertex('f')
graph.add_vertex('g')
graph.add_vertex('h')
graph.add_vertex('i')
graph.add_vertex('j')
graph.add_vertex('k')
graph.add_vertex('l')
graph.add_vertex('m')

graph.add_edges('s', 'a', 3)
graph.add_edges('s', 'b', 6)
graph.add_edges('s', 'c', 5)
graph.add_edges('a', 'd', 9)
graph.add_edges('a', 'e', 8)
graph.add_edges('b', 'f', 12)
graph.add_edges('b', 'g', 14)
graph.add_edges('c', 'h', 7)
graph.add_edges('h', 'i', 5)
graph.add_edges('h', 'j', 6)
graph.add_edges('i', 'k', 1)
graph.add_edges('i', 'l', 10)
graph.add_edges('i', 'm', 2)




graph = {'s': [['a', 3], ['b', 6], ['c', 5]],
 'a': [['s', 3], ['d', 9], ['e', 8]],
 'b': [['s', 6], ['f', 12], ['g', 14]],
 'c': [['s', 5], ['h', 7]],
 'd': [['a', 9]],
 'e': [['a', 8]],
 'f': [['b', 12]],
 'g': [['b', 14]],
 'h': [['c', 7], ['i', 5], ['j', 6]],
 'i': [['h', 5], ['k', 1], ['l', 10], ['m', 2]],
 'j': [['h', 6]],
 'k': [['i', 1]],
 'l': [['i', 10]],
 'm': [['i', 2]]}

def UCS(graph, start, goal):
    explored = set()
    frontier = PriorityQueue()
    frontier.put((0, start))
    result = 'Fail'
    pathCost = {}
    pathCost['s'] = 0
    while not frontier.empty():
        node = frontier.get()
        if node[1] == goal:
            return explored # node[1] = 's'
        explored.add(node[1])
        for i in range(len(graph[node[1]])): # graph[node[1]] = [['a', 3], [b,6], ['c', 5]]
            neighbor = graph[node[1]][i] # ['a', 3], [b,6], ['c', 5] # a , b , c
            if (neighbor[0] not in explored) :
                pathCost[neighbor[0]] = pathCost[node[1]] + neighbor[1]
                frontier.put((pathCost[neighbor[0]],neighbor[0]))
    print(pathCost)
    print(explored)
    return(result)


                
                
                
                
                
                
                
                
                
