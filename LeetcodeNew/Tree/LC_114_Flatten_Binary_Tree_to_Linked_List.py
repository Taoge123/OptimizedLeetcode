"""
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


"""
# (reverse preorder traversal)
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


class Solution22:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)
        tempRight = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tempRight
        return
"""
An inorder python solution
         *
       /
      n
   /     \
 left   right
  \ 
   *
    *
     \
      p

The idea is very simple. Suppose n is the current visiting node, 
and p is the previous node of preorder traversal to n.right.

We just need to do the inorder replacement:

n.left -> NULL

n.right - > n.left

p->right -> n.right

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root










