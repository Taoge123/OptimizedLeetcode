
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root):

        self.res = 0
        def dfs(node)  :  # return min,max,sum starting from this cur node
            if not node:
                return [float('inf'), -float('inf'), 0]
            leftMin, leftMax, leftSum = dfs(node.left)
            rightMin, rightMax, rightSum = dfs(node.right)
            # larger than leftMax and smaller than rightMin
            if node.val > leftMax and node.val < rightMin:
                self.res = max(self.res, node.val + leftSum + rightSum)
                # update min,max,sum
                return [min(leftMin, node.val), max(rightMax, node.val), node.val + leftSum + rightSum]
                # for other cases, we fail.
            return [-float('inf') ,float('inf') ,0]

        dfs(root)
        return self.res

