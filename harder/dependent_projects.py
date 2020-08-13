"""
Build Order.

You are given a list of projects and a list of dependencies (which is list of pairs of projects, where the second project 
dependent on the first project). All of a projects dependencies must be built before the project is.

Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

Eg:
    Input: 
      projects: ['a','b','c','d,','e','f']
      dependencies [(a,d),(f,b),(b,d),(f,a),(d,c)]

    Output:
      f, e, a, b, d, c


"""

class node(object):
    def __init__(self,key):
        self.key = key
        self.edges = []
        self.incoming = []

    def addEdge(self,node):
        self.edges.append(node)
        node.incoming.append(self)
    
    def delEdge(self,node):
        self.edges = self.edges.remove(node)
        node.incoming.remove(self)
    


a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')

a.addEdge(d)
f.addEdge(b)
b.addEdge(d)
f.addEdge(a)
d.addEdge(c)

proj = [a,b,c,d,e,f]

def findBuildOrder(arr):
    output = []
    #tobeprocessed = []

    def recurse(node):
    
        for i in range(len(node)):
            if node[i].edges == []:
                if node[i].key not in output:
                    output.append(node[i].key)
                #processed.add(0, node[i])
                return node
            else: 
                for j in range(len(node[i].edges)):
                    if node[i].edges[j].key not in output:
                        recurse(node[i].edges[j].edges)
                        output.append(node[i].edges[j].key)
                    else: 
                        output.append(node[i].key)
                    #if node.edges[i] not in tobeprocessed:
                        #tobeprocessed.append(node.edges[j])
                        #recurse(j)
                        
        

    recurse(arr)

    return output

print(findBuildOrder(proj))