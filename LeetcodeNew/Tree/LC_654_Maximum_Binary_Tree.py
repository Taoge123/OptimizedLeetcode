
"""
https://leetcode.com/problems/maximum-binary-tree/discuss/158872/Python-DFS-tm

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])

        pivot = max(nums)
        idx = nums.index(pivot)
        root = TreeNode(pivot)

        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])

        return root


"""
这道题和LC108基本一样。并且相对简单一点。

LC108. Convert Sorted Array to Binary Search Tree 代码
"""
class Solution108:
    def sortedArrayToBST(self, nums):
        if not nums: return None
        l, r = 0, len(nums) - 1
        mid = (l + (r - l)) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

"""
区别在于108用Binary Search每次定义mid节点的区间，这道题只需要用nums.index(max(nums))即可。

LC654.Maximum Binary Tree 代码
"""

class Solution2:
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        mid = nums.index(max(nums))
        node = TreeNode(nums[mid])
        node.left = self.constructMaximumBinaryTree(nums[:mid])
        node.right = self.constructMaximumBinaryTree(nums[mid+1:])
        return node



