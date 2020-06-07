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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root


class SolutionWisdom:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        if not root.left:
            self.flatten(root.right)
            return

        left = root.left
        right = root.right
        self.flatten(root.left)
        self.flatten(root.right)

        root.right = left
        root.left = None

        # 右边的链子搭到左边的底端
        while left.right:
            left = left.right
        left.right = right



