"""

Implement an algorithm to traverse a graph or tree using a breadth first search (BFS)

"""

class node(object):
    def __init__(self,key):
        self.key = key
        self.children = []          # For a graph this would be edges


visited = []
queue = []

def bfs(node):
    visited.append(node)
    queue.append(node)

    while queue:
        current = queue.pop(0)
        print(current)

        for i in current.children:
            if i not in visited:
                visited.append(i)
                queue.append(i)


