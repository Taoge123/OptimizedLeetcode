
"""

分制，然后每次上传当前节点inc和dec的值，最后进行比对。
具体操作参考Leetcode答案里面的幻灯片，走一遍就懂了: 链接

https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/solution/

"""
class Solution(object):
    def longestConsecutive(self, root):
        if not root: return 0
        self.res = 1
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return [0, 0]
        inc, dec = 1, 1
        left = self.dfs(root.left)
        right = self.dfs(root.right)

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




