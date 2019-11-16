
"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return None

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return node.val

# class Solution:
#     def findBottomLeftValue(self, root: TreeNode) -> int:
#         if not root:
#             return -1

#         self.res = 0
#         self.height = 0
#         self.helper(root, 1)
#         return self.res

#     def helper(self, root, depth):
#         if not root:
#             return

#         if self.height < depth:
#             self.height = depth
#             self.res = root.val

#         self.helper(root.left, depth + 1)
#         self.helper(root.right, depth + 1)







