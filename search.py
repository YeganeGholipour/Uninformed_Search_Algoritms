# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:09:21 2023

@author: user
"""


import queue
from queue import PriorityQueue



def backtrace(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def BFS(graph, start, goal):
    frontier = []
    explored = set()
    parent = {}
    frontier.put(start)
    result = 'Fail'
    while not frontier.empty():
        current_node = frontier.pop[0]
        explored.add(current_node)
        for child in graph[current_node]:
            if (child not in frontier) or (child not in explored):
                if child == goal:
                    return backtrace(parent, start, goal)
                parent[child] = current_node
                frontier.put(child)
    return  result




def backtrace(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def DFS(graph, start, goal):
    frontier = []
    parent = {}
    frontier.append(start)
    result = 'Fail'
    while frontier:
        current_node = frontier.pop()
        if current_node == goal:
            return backtrace(parent, start, goal)
        for child in graph[current_node]:
            if (child not in frontier) and child != None:
                parent[child] = current_node
                frontier.append(child)
    return result
                
graph = {'s': ['a','b','c'],
         'a': ['d', 'e'],
         'b': ['f', 'g'],
         'c': ['h'],
         'd': [None],
         'e': [None],
         'f': [None],
         'g': [None],
         'h': ['i', 'j'],
         'i': ['k', 'L', 'm'],
         'j': [None],
         'k': [None],
         'l': [None],
         'm': [None]}                
                
                


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

















graph = {'s': ['a','b','c'],
         'a': ['s', 'd', 'e'],
         'b': ['s', 'f', 'g'],
         'c': ['s', 'h'],
         'd': ['a'],
         'e': ['a'],
         'f': ['b'],
         'g': ['b'],
         'h': ['c', 'i', 'j'],
         'i': ['h', 'k', 'L', 'm'],
         'j': ['h'],
         'k': ['i'],
         'l': ['i'],
         'm': ['i']}
            
                
                
                
                
                
