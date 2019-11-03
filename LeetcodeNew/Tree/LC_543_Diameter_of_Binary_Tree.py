
"""
Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
"""
"""
Intuition
Any path can be written as two arrows (in different directions) from some node, 
where an arrow is a path that starts at some node and only travels down to child nodes.
If we knew the maximum length arrows L, R for each child, 
then the best path touches L + R + 1 nodes.
Algorithm
Let's calculate the depth of a node in the usual way: 
max(depth of node.left, depth of node.right) + 1. 
While we do, a path "through" this node uses 1 + (depth of node.left) + (depth of node.right) nodes. 
Let's search each node and remember the highest number of nodes used in some path. 
The desired length is 1 minus this number.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max = float('-inf')
        self.helper(root)
        return self.max - 1

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.max = max(self.max, left + right + 1)
        return max(left, right) + 1




