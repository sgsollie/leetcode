"""

Write code to remove duplicates from an unsorted linked list

1. Iterate over each variable and add it to a cache.
2. Each time we come to a new variable, check if it is in the cache.
3. If it is in the cache already, it is a duplicate:
    3a. Set the previous item's nextnode to be the current item's next node - removing this duplicate from the chain.
4 continue until we get to the tail.


"""

class node(object):
    def __init__(self,key):
        self.key = key
        self.next = None


a = node("a")
b = node("b")
c = node("c")
d = node("d")
e = node("a")
f = node("a")

a.next = e
e.next = b
b.next = f
f.next = c
c.next = d


def remove_dups(node):
    
    currentnode = node
    cache = {}
    prev = None

    while currentnode:
        print(cache)
        if currentnode.key in cache:
            prev.next = currentnode.next
        else:
            cache[currentnode.key] = 1
            prev = currentnode
        currentnode = currentnode.next


print("Key: ",a.key,"Next: ",a.next.key) 
print("Key: ",b.key,"Next: ",b.next.key)
print("Key: ",c.key,"Next: ",c.next.key)
remove_dups(a)
print("Order after removed Dups below")
print("Key: ",a.key,"Next: ",a.next.key) 
print("Key: ",b.key,"Next: ",b.next.key)
