
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        return self.helper(root, root.val)

    def helper(self, root, mini):
        if not root:
            return -1
        if root.val > mini:
            return root.val
        left = self.helper(root.left, mini)
        right = self.helper(root.right, mini)
        if left == -1 or right == -1:
            return max(left, right)
        else:
            return min(left, right)


class SolutionTony:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = []
        self.helper(root, res)
        res = list(set(res))
        if len(res) >= 2:
            res.sort()
            return res[1]
        return -1

    def helper(self, root, res):
        if not root:
            return

        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

