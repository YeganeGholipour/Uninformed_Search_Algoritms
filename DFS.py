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