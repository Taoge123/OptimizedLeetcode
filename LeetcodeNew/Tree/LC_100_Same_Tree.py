
"""

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


> 类型：DFSF分制
> Time Complexity O(N)
> Space Complexity O(h)
在每一层先检查再递归，所以这是pre-order的思路。
比对相等的条件：

p.val == q.val
if not p or not q: return p == q
如有不等，直接返回False，就不用继续递归了。最后左右孩子返回给Root：return left and right
p.s. 上面的第二个相等条件，检查了2种情况：
1.if not p and not q: return True
2.if not p or not q: return False

"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p or not q:
            return p == q

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right






