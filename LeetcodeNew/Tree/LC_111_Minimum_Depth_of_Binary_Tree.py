
"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/158303/Python-or-DFS-tm

这里思路很简单，分制以后再返回的时候增加层级。
唯一要注意的是一定要有个Edge情况，如果左右孩子一边为空，例如地下白板的例子，
就不能返回min(left, right)，因为空的一边为0，所以会返回错误的数。
这种edge我们则返回: left + right + 1

"""
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionGood:
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        return min(left, right) + 1


class SolutionTony:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
