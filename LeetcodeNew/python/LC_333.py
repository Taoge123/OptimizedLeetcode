
"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SubTree:
    def __init__(self, largest, size, min, max):
        self.largest = largest
        self.size = size
        self.min = min
        self.max = max


class SolutionTony:
    def largestBSTSubtree(self, root):

        count, mini, maxi = self.dfs(root)
        return count

    def dfs(self, root):
        if not root:
            return 0, float("inf"), float("-inf")

        lcount, lmin, lmax = self.dfs(root.left)
        rcount, rmin, rmax = self.dfs(root.right)

        if lmax < root.val < rmin:
            return lcount + rcount + 1, min(lmin, root.val), max(rmax, root.val)  # 看能否和root组合成一个大的

        return max(lcount, rcount), float("-inf"), float("inf")  # 只能选一边



class Solution2:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        if self.isBST(root, -sys.maxsize, sys.maxsize):
            return self.count(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def count(self, node):
        if not node:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

    def isBST(self, node, mini, maxi):
        if not node: return True
        if node.val < mini or node.val > maxi:
            return False

        return self.isBST(node.left, mini, node.val - 1) and self.isBST(node.right, node.val + 1, maxi)




class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res[0]

    def dfs(self, root):
        if not root:
            return [0, 0, float('inf'), float('-inf')]

        left, size1, mini1, maxi1 = self.dfs(root.left)
        right, size2, mini2, maxi2 = self.dfs(root.right)

        if root.val > maxi1 and root.val < mini2:
            size = size1 + size2 + 1
        else:
            size = float('-inf')

        largest = max(left, right, size)

        return [largest, size, min(root.val, mini1), max(root.val, maxi2)]












