"""

Flatten a binary tree to a linkedlist:

Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


##

(Below solution does this kinda opposite, using the left branch as the linked list.)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

previous = None

def flatten(node):
    if not node:
        return
        
    flatten(node.left)
    flatten(node.right)
    node.left = previous
    node.right = None
    previous = node

