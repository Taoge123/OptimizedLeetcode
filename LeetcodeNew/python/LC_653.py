"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

"""

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        if not root:
            return False
        bfs, visited = collections.deque([root]), set()
        while bfs:
            node = bfs.popleft()
            if k - node.val in visited:
                return True
            visited.add(node.val)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return False



class Solution2:
    def findTarget(self, root, k):
        if not root:
            return False

        return self.dfs(root, set(), k)

    def dfs(self, root, visited, k):
        if not root:
            return False

        complement = k - root.val
        if complement in visited:
            return True

        visited.add(root.val)
        return self.dfs(root.left, visited, k) or self.dfs(root.right, visited, k)







