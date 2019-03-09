
"""

https://leetcode.com/problems/add-one-row-to-tree/solution/


Example 1:
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:
Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root, v, d):
        if d < 2:
            node = TreeNode(v)
            node.left = root if d == 1 else None
            node.right = root if d == 0 else None
            return node
        elif root:
            root.left = self.addOneRow(root.left, v, d - 1 if d > 2 else 1)
            root.right = self.addOneRow(root.right, v, d - 1 if d > 2 else 0)
            return root


# Go row by row to the row at depth d-1, then insert the new nodes there.

class Solution2:
    def addOneRow(self, root, v, d):
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        for _ in range(d - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left


"""
Let's perform this recursively.

    1. When d is 1, depending on the direction we went previously (default is left), 
    we need to make a node with value v and put the rest of the tree as either the left or right child.

    2. Otherwise, we'll recursively perform our operation on the children of our node, 
    with the depth decremented by 1."""


class Solution:
    def addOneRow(self, root, v, d, direction='left'):
        if d == 1:
            ans = TreeNode(v)
            setattr(ans, direction, root)
            return ans
        elif root:
            root.left = self.addOneRow(root.left, v, d - 1, 'left')
            root.right = self.addOneRow(root.right, v, d - 1, 'right')
            return root


class Solution4:

    def addOneRow(self, root, v, d, direction = 'left'):
        if d == 1:
            ans = TreeNode(v)
            #setattr(ans, direction, root)
            #creat node with target value and set its left or right be the level great than level d
            if direction == 'left':
                ans.left = root
            else:
                ans.right = root
            return ans
        elif root:
            root.left = self.addOneRow(root.left, v, d-1, 'left')
            root.right = self.addOneRow(root.right, v, d-1, 'right')
            return root


