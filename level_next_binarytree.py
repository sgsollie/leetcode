"""
Given a perfect binary tree. 

	1
   /  \
  2    3
 / \  / \
4  5  6  7

	1 ---------> Null
   /  \
  2--->3 ------> Null
 / \  / \
4-->5->6-->7---> Null

Where each node object has an additional value named "next" - 
Populate each next pointer to its next right node. (In the above example, node2.next would be 3, node 4.next would be 5 etc)
If there is no next right node, the next pointer should be set to None.
Initially all next pointers are set to null.

Constraints:
	number of nodes in a given tree < 4096
	-1000 is <= node.val <= 1000

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
1. Construct tree with input nodes (need not do this programatically)

2. traverse tree
	2.a: set left most node pointer to leftest node so far & set rightmost node pointer to rightest node so far
    2.b: while there is a leftmost node, populate leftmostnode.next with the known rightmost node



"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
   

def traverse(node):                 # node = 1
    if node:
        leftNode = node.left			 # leftNode = 2
        rightNode = node.right		     # rightNode = 3
    while leftNode: 
        leftNode.next = rightNode        # 2.next = 3,     5.next = 6
        leftNode = leftNode.right        # leftNode = 5,   leftNode=no
        rightNode = rightNode.left	     # rightNode = 6,  none
			
    traverse(node.left)
    traverse(node.right)