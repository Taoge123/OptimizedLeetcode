
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTony:
    def maxSumBST(self, root):
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return float('inf'), float('-inf'), 0

        l_mini, l_maxi, leftSum = self.dfs(node.left)
        r_mini, r_maxi, rightSum = self.dfs(node.right)

        if l_maxi < node.val < r_mini:
            summ = node.val + leftSum + rightSum
            self.res = max(self.res, summ)
            return min(l_mini, node.val), max(r_maxi, node.val), summ

        return float('-inf'), float('inf'), 0


class Solution4Param:
    def largestBSTSubtree(self, root):

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return True, 0, float("inf"), float("-inf")

        lBST, lcount, lmin, lmax = self.dfs(root.left)
        rBST, rcount, rmin, rmax = self.dfs(root.right)

        isBST = lBST and rBST and lmax < root.val < rmin
        maxx = max(root.val, rmax)
        minn = min(root.val, lmin)
        count = lcount + rcount + 1

        if isBST:
            self.res = max(self.res, count)
        return isBST, count, minn, maxx



class SolutionRika:
    def maxSumBST(self, root):
        self.res = 0
        self.dfs(root, float('inf'), float('-inf'))
        return self.res

    def dfs(self, root, minn, maxx):
        if not root:
            return float('inf'), float('-inf'), 0

        Lmin, Lmax, Lsumm = self.dfs(root.left, minn, root.val - 1)
        Rmin, Rmax, Rsumm = self.dfs(root.right, root.val + 1, maxx)

        if Lmax < root.val < Rmin:
            summ = Lsumm + Rsumm + root.val
            self.res = max(self.res, summ)
            return min(Lmin, root.val), max(Rmax, root.val), summ

        return float('-inf'), float('inf'), 0




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

