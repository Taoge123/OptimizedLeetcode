"""
Given a binary tree and a sum,
find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


https://leetcode.com/problems/path-sum-ii/discuss/158342/Python-DFS-tm
大致思路就是每层递归用一个临时数组保存当前的路径，
最后将sum(temp) == target 来判断此路径是否满足条件，满足则放入Global数组。
这个思路还可以被优化：因为要好几次sum的调用，可以每一层递归的时候把target - root.val传下去。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res = []
        self.helper(root, sum, [], res)
        return res

    def helper(self, root, sum, path, res):

        if not root:
            return []

        if not root.left and not root.right and root.val == sum:
            res.append(path + [root.val])

        self.helper(root.left, sum - root.val, path + [root.val], res)
        self.helper(root.right, sum - root.val, path + [root.val], res)
