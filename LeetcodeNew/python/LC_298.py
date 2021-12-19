"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node
to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionTony:
    def longestConsecutive(self, root):
        if not root:
            return 0
        self.res = 1
        self.dfs(root, -1, 0)
        return self.res

    def dfs(self, root, prev, count):
        if not root:
            return None

        if root.val == prev + 1:
            count += 1
            self.res = max(self.res, count)
        else:
            count = 1

        self.dfs(root.left, root.val, count)
        self.dfs(root.right, root.val, count)



class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.helper(root, 0, root.val)
        return self.res

    def helper(self, root, count, target):
        if not root:
            return 0

        if root.val == target:
            count += 1
        else:
            count = 1
        self.res = max(self.res, count)

        self.helper(root.left, count, root.val + 1)
        self.helper(root.right, count, root.val + 1)






