class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution0:
    def constructMaximumBinaryTree(self, nums):
        return self.dfs(nums, 0, len(nums))

    def dfs(self, nums, i, j):
        if i == j:
            return None

        maxi = max(nums[i:j])
        k = nums.index(maxi)

        root = TreeNode(nums[k])
        root.left = self.dfs(nums, i, k)
        root.right = self.dfs(nums, k + 1, j)
        return root





class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return None

        mid = nums.index(max(nums))
        node = TreeNode(nums[mid])

        node.left = self.constructMaximumBinaryTree(nums[:mid])
        node.right = self.constructMaximumBinaryTree(nums[mid + 1:])
        return node




class SolutionTony1:
    def constructMaximumBinaryTree(self, nums):
        return self.dfs(nums)

    def dfs(self, nums):
        if not nums:
            return

        maxi = max(nums)
        i = nums.index(maxi)

        root = TreeNode(nums[i])
        root.left = self.dfs(nums[:i])
        root.right = self.dfs(nums[i + 1:])
        return root

