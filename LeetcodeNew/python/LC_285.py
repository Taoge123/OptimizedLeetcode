"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.



Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.


Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        return res

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.dfs(root, p)
        return self.res

    def dfs(self, root, p):
        if not root:
            return
        if p.val < root.val:
            self.res = root
            self.dfs(root.left, p)
        else:
            self.dfs(root.right, p)









