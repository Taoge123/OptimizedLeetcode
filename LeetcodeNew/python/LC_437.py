
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def helper(self, root, target):
        if not root:
            return 0
        left = self.helper(root.left, target - root.val)
        right = self.helper(root.right, target - root.val)
        return left + right + int(root.val == target)


class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        self.helper(root, cache, 0, sum)
        return self.result

    def helper(self, root, cache, curSum, sum):

        if not root:
            return

        curSum += root.val
        oldSum = curSum - sum
        self.result += cache[oldSum]
        cache[curSum] += 1
        self.helper(root.left, cache, curSum, sum)
        self.helper(root.right, cache, curSum, sum)
        cache[curSum] -= 1








