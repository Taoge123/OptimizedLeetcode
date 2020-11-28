"""
Time O(N * min(L,H))
Space O(H)
where N = tree size, H = tree height, L = list length.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return root.val == head.val and (self.dfs(head.next, root.left) or self.dfs(head.next, root.right))



"""
Solution 2: DP
Iterate the whole link, find the maximum matched length of prefix.
Iterate the whole tree, find the maximum matched length of prefix.
About this dp, @fukuzawa_yumi gave a link of reference:
https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm

Time O(N)
Space O(L + H)
where N = tree size, H = tree height, L = list length.
"""




