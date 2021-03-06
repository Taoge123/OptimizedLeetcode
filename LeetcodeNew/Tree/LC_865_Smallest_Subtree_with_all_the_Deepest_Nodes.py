
"""
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.



Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.

"""




"""
Write a sub function deep(TreeNode root).
Return a pair(int depth, TreeNode subtreeWithAllDeepest)

In sub function deep(TreeNode root):

if root == null, return pair(0, null)
left = deep(root.left)
right = deep(root.left)

if left depth == right depth,
deepest nodes both in the left and right subtree,
return pair (left.depth + 1, root)

if left depth > right depth,
deepest nodes only in the left subtree,
return pair (left.depth + 1, left subtree)

if left depth < right depth,
deepest nodes only in the right subtree,
return pair (right.depth + 1, right subtree)
"""

"""
题目大意
一棵二叉树有它的最大深度，找出一个节点，这个节点包含了所有最大深度的叶子。并且这个节点最接近叶子节点。

解题方法
这个题貌似很复杂，而且没有思路，这就说明没有建模好。

这个题的模型其实比较左右子树的高度，如果左右子树的高度相等，说明当前节点就是要求的。这个解释是这样的：必须包含所有的最大高度的叶子，左右叶子高度相等，所以必须包含当前节点。

当左子树高度>右子树高度的时候，要求的节点在左边；反之，在右边。

所以，递归思路 + 一个pair。这个pair的思路是，保存了当前节点的深度和当前节点的最深子树节点。

如果还不明白可以看下图的右边部分，每个节点旁边都写了（高度，当前符合要求的节点）。

"""
import collections


class Solution1:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.depth(root)[1]

    def depth(self, root):
        if not root: return 0, None
        l, r = self.depth(root.left), self.depth(root.right)
        if l[0] > r[0]:
            return l[0] + 1, l[1]
        elif l[0] < r[0]:
            return r[0] + 1, r[1]
        else:
            return l[0] + 1, root





class Solution2:
    def subtreeWithAllDeepest(self, root):
        # Tag each node with it's depth.
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        max_depth = max(depth.itervalues())

        def answer(node):
            # Return the answer for the subtree at node.
            if not node or depth.get(node, None) == max_depth:
                return node
            L = answer(node.left)
            R = answer(node.right)
            return node if L and R else L or R

        return answer(root)


"""
Algorithm

The Result (on some subtree) returned by our (depth-first search) 
recursion will have two parts:

Result.node: the largest depth node that is equal to or an ancestor of all the deepest nodes of this subtree.
Result.dist: the number of nodes in the path from the root of this subtree, to the deepest node in this subtree.
We can calculate these answers disjointly for dfs(node):

To calculate the Result.node of our answer:

If one childResult has deeper nodes, then childResult.node will be the answer.

If they both have the same depth nodes, then node will be the answer.

The Result.dist of our answer is always 1 more than the largest childResult.dist we have.

"""


class Solution:
    def subtreeWithAllDeepest(self, root):
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))
        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node



















