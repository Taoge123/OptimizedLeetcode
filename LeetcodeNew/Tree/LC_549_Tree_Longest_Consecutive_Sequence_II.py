
"""
Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].


Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

分制，然后每次上传当前节点inc和dec的值，最后进行比对。
具体操作参考Leetcode答案里面的幻灯片，走一遍就懂了: 链接

https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/solution/

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        inc, dec = 1, 1
        if root.left:
            if root.left.val - 1 == root.val:
                inc = max(inc, left[0] + 1)
            if root.left.val + 1 == root.val:
                dec = max(dec, left[1] + 1)
        if root.right:
            if root.right.val - 1 == root.val:
                inc = max(inc, right[0] + 1)
            if root.right.val + 1 == root.val:
                dec = max(dec, right[1] + 1)
        self.res = max(self.res, inc + dec - 1)
        return [inc, dec]





