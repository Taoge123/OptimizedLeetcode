

"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree,
so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1

"""
"""

这题做法有些取巧，并不是真正意义上在内存里面删除不符合区间的Node，只是将Node的指向进行的更改，大致思路：

每一层的Condition有三种：

root.val小于区间的lower bound L，则返回root.right subtree传上来的root，这里就变相的'删除'掉了当前root和所有root.left的node
root.val大于区间的upper bound R，则返回root.left subtree传上来的root
满足区间，则继续递归
当递归走到叶子节点的时候，我们向上返回root，这里return root的定义是：
返回给parent一个区间调整完以后的subtree



"""

class Solution(object):
    def trimBST(self, root, L, R):
        # 每一层的Condition
        if not root: return root
        if root.val > R: return self.trimBST(root.left, L, R)
        if root.val < L: return self.trimBST(root.right, L, R)

        # 再区间内，正常的Recursion
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        # 返回给parent一个区间调整完以后的subtree
        return root


class Solution:
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)


class Solution2:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if L > root.val:
            return self.trimBST(root.right, L, R)
        elif R < root.val:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root






