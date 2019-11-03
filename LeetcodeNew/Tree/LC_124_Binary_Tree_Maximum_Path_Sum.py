"""

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42



Similar to Problem 687

https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/171807/Python-or-DFS-tm


Algorithm

分制到底部，在返回的时候传入左右任意一遍最大值加上目前root.val:
cur = max(left, right) + root.val
这种情况处理了从Root到左右任意一边的最大值，也就是 root.val + left 和 root.val + right
还有一种情况就是当最大值 = root.val + left + right， 我们在放入global变量的时候何其比较。
对于最底部叶子节点传上来的值，我们将其设置成0: return cur if cur > 0 else 0


Now everything is ready to write down an algorithm.

1. Initiate max_sum as the smallest possible integer and call max_gain(node = root).
2. Implement max_gain(node) with a check to continue the old path/to start a new path:
        - Base case : if node is null, the max gain is 0.
        - Call max_gain recursively for the node children to compute max gain from the left and right subtrees : left_gain = max(max_gain(node.left), 0) and
            right_gain = max(max_gain(node.right), 0).
        - Now check to continue the old path or to start a new path. To start a new path would cost price_newpath = node.val + left_gain + right_gain. Update max_sum if it's better to start a new path.
        - For the recursion return the max gain the node and one/zero of its subtrees could add to the current path : node.val + max(left_gain, right_gain).


Bottom up divider and conquer
At each rode, it can form 3 tyes of path.
1st is node
2nd is left - node - right
3rd is left/right - node
Once we get the max after comparsion, we return 1st or 3rd path sum to the upper level.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return

        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        self.res = max(self.res, root.val + left + right)
        return max(left, right) + root.val





