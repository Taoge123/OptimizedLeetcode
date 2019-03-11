
"""

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


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



