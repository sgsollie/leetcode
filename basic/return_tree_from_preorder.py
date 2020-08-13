class node(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
inputtree = [8,5,1,7,10,12]

def bstFromPreOrder(input):
    for i in range(1,len(input)):
        currlen = len(input[:i])//2
        
        if input[currlen] < input[i]:
            input[currlen].left = input[i]
        else:
            input[currlen].right = input[i]
            
        return input[0] # ?


