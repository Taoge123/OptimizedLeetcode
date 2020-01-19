"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        res = []
        if start > end:
            res.append(None)

        for rootVal in range(start, end + 1):
            for left in self.dfs(start, rootVal - 1):
                for right in self.dfs(rootVal + 1, end):
                    root = TreeNode(rootVal)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res




class Solution1:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        res = []
        if start > end:
            res.append(None)

        for rootVal in range(start, end + 1):
            left = self.dfs(start, rootVal - 1)
            right = self.dfs(rootVal + 1, end)
            for i in left:
                for j in right:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res


a = Solution()
print(a.generateTrees(6))








