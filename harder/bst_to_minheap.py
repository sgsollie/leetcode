class tree(object):
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
	

	def insertLeft(self,newNode):
		if self.left == None:
		    self.left = newNode
		else:
			t = tree(newNode)
			t.left = self.left
			self.left = t

	def insertRight(self,newNode):
		if self.right == None:
			self.right = newNode
		else:
			t = tree(newNode)
			t.right = self.right
			self.right = t

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getRootVal(self):
		return self.key
	
	def setRootVal(self,key):
		self.key = key


def preOrderprint(tree):
    if tree:
        print(tree.getRootVal())
        preOrderprint(tree.getLeft())
        preOrderprint(tree.getRight())

def inOrder(tree,arr):
    if tree == None:
        return
    else:
        inOrder(tree.left,arr)
        arr.append(tree.key)
        inOrder(tree.right,arr)



# pre order traverse to populate from array

def populateHeap(tree,arr,i):
    if not tree:
        return
    i[0] += 1

    tree.setRootVal(arr[i[0]])
    populateHeap(tree.left, arr, i)
    populateHeap(tree.right, arr, i)

def convertHeap(tree):
	arr = []
	i = [-1]
	inOrder(tree,arr)
	populateHeap(tree,arr,i)



r = tree(5)                                     #Remember here to assign tree objects, not just assining ints
r.left = tree(3)
r.right = tree(6)
r.getLeft().insertLeft(tree(2))
r.getLeft().insertRight(tree(4))


convertHeap(r)
preOrderprint(r)