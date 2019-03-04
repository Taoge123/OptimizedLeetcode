
"""
这题很巧妙的运用了Binary Search的一些性质，然后配合Binary Search Tree的特征。
每次找寻中间点，然后左右分配。
优化部分解决了每次Slicing多付出的时间复杂度。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums: return None
        l, r = 0, len(nums) - 1
        mid = (l + (r - l)) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node


class SolutionBetter:
    def sortedArrayToBST(self, nums):
        self.nums = nums
        return self.dfs(0, len(nums) - 1)

    def dfs(self, l, r):
        if l > r: return None
        mid = (l + r) // 2
        node = TreeNode(self.nums[mid])
        node.left = self.dfs(l, mid - 1)
        node.right = self.dfs(mid + 1, r)
        return node







