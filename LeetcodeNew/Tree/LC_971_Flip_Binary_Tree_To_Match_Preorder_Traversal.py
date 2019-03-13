
"""
https://blog.csdn.net/qq_17550379/article/details/85987595

https://blog.csdn.net/fuxuemingzhu/article/details/85939252


Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.
Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value,
then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes
in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.
You may return the answer in any order.

If we cannot do so, then return the list [-1].

Example 1:

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []

"""
"""
Explanation:
Global integer i indicates next index in voyage v.
If current node == null, it's fine, we return true
If current node.val != v[i], doesn't match wanted value, return false
If left child exist but don't have wanted value, flip it with right child.

1 若当前节点root与voyage中当前元素不相等，返回False;
2 否则，若root的左节点存在且节点值与voyage中当前元素相等，则分别递归遍历左右节点；
3 否则，若root的右节点存在且节点值与voyage中当前元素相等，
  此时如果左节点也存在则发生反转，则把反转节点记录到结果中，然后分别递归遍历右左节点（逻辑上翻转）；
4 最后，若root的左右节点都不存在，返回True
--------------------- 
作者：ClementCJ 
来源：CSDN 
原文：https://blog.csdn.net/jianyingyao7658/article/details/86140125 
版权声明：本文为博主原创文章，转载请附上博文链接！

"""

class SolutionLee:
    def flipMatchVoyage(self, root, voyage):
        res = []
        self.i = 0

        def dfs(root):
            if not root:
                return True
            if root.val != voyage[self.i]:
                return False

            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left, root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)

        return res if dfs(root) else [-1]


class SolutionLee2:
    def flipMatchVoyage(self, root, voyage):
        res = []
        self.i = 0
        def dfs(root):
            if not root: return True
            if root.val != voyage[self.i]: return False
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left,root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)
        return res if dfs(root) else [-1]




















