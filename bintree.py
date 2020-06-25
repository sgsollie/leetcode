

class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key  



# To traverse the tree with a recursive function:
def search(root, key):
    
    # base case of if the root node is the data we are looking for
    if root is None or root.val is key:
        return root

    if root.val < key:
        return search(root.right, key)
    
    return search(root.left, key)


def insert(root,node):
    
    #base case if the root node is none, insert here
    if root is None: 
        root = node
    
    if root.val < node.val:
        if root.right == None:
            root.right = node
        else: 
            insert(root.right, node)

    elif root.val > node.val:
        if root.left == None:
            root.left = node
        else:
            insert(root.left, node) 
            
    

def inorder(root):
    # function that takes a node object, traverses each node
    # and prints the value of each node.

    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

