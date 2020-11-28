
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return [0, 0.0]

        count1, sum1 = self.helper(root.left)
        count2, sum2 = self.helper(root.right)

        count = count1 + count2 + 1
        summ = sum1 + sum2 + root.val
        self.res = max(self.res, summ / count)
        return [count, summ]



