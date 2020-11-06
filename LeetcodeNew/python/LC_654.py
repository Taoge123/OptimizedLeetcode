class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return None

        mid = nums.index(max(nums))
        node = TreeNode(nums[mid])

        node.left = self.constructMaximumBinaryTree(nums[:mid])
        node.right = self.constructMaximumBinaryTree(nums[mid + 1:])
        return node


