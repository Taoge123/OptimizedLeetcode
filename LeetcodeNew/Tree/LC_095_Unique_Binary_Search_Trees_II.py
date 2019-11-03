"""

Given an integer n, generate all structurally unique BST's
(binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


1) Initialize list of BSTs as empty.
2) For every number i where i varies from 1 to N, do following
......a)  Create a new node with key as 'i', let this node be 'node'
......b)  Recursively construct list of all left subtrees.
......c)  Recursively construct list of all right subtrees.
3) Iterate for all left subtrees
   a) For current leftsubtree, iterate for all right subtrees
        Add current left and right subtrees to 'node' and add
        'node' to list.

Refer geekforgeeks
https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/
我们不妨将问题关于规模n进行抽象，即S(K)表示1~K构成的所有二叉搜索树组成的集合，而我们的答案就是S(n)。
那么如何求解S(K)呢？

我们不妨枚举根节点root的取值j，不难发现，root的左子树必然是一个1~(j-1)的二叉搜索树，
root的右子树必然是一个j+1~K的二叉搜索树。

特别的，如果我们把root的右子树中的所有取值都减去j，那么root的右子树必然是一个1~(K-j)的二叉搜索树。
也就是说，如果我们已经计算出了S(j-1)和S(K-j)，
我们就可以通过枚举S(j-1)中的一个元素和S(K-j)中的一个元素，来拼接成所有的S(K)，
即可以通过将S(K)转化为更小规模的问题来完成计算。

所以我们可以按照递推的方式，从K=1开始依次对S(K)进行计算，并且在最后计算S(n)
"""




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.gen_helper({}, 1, n)

    def gen_helper(self, memo, start, end):
        if start > end:
            return [None]
        if (start, end) in memo:
            return memo[(start, end)]
        memo[(start, end)] = []
        for root_val in range(start, end + 1):
            for left_child in self.gen_helper(memo, start, root_val - 1):
                for right_child in self.gen_helper(memo, root_val + 1, end):
                    root = TreeNode(root_val)
                    root.left, root.right = left_child, right_child
                    memo[(start, end)].append(root)
        return memo[(start, end)]



class SolutionTony:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        res = []
        if start > end:
            res.append(None)

        for rootVal in range(start, end + 1):
            for left in self.dfs(start, rootVal - 1):
                for right in self.dfs(rootVal + 1, end):
                    root = TreeNode(rootVal)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res





