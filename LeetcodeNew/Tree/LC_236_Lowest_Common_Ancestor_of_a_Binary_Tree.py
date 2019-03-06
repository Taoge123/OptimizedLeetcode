
"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

> 类型：DFS分制
> Time Complexity O(n)
> Space Complexity O(h)
这道Follow Up没有BST的特性，所以要对几种case一个一个进行测试。
Condition为两种：如果没找到，返回None，找到则返回当前的root(因为找到一个root就不需要继续深入)
比对方式：

1. 如果parent的左右孩子都有返回，说明parent就是LCA
2. 如果左边没有返回：则右边返回的就是LCA
3. 如果右边没有返回：则左边返回的就是LCA

"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left



