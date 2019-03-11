"""

Given the root of a binary tree with N nodes, each node in the tree has node.val coins,
and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
(The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree,
we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root,
we move two coins to the root [taking two moves].
Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4


Note:

1<= N <= 100
0 <= node.val <= N

Solution 1
Quite similar problem as this one 968.Binary Tree Cameras.
So I put this as the first solution.
Write a dfs helper, return the number of coins given to the parent.

"""

class SolutionLee1:
    res = 0
    def distributeCoins(self, root):
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left) + abs(right)
            return root.val + left + right - 1

        dfs(root)
        return self.res



class Solution:
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans

# Give the parent node so we can move the coins to the parent directly.
class SolutionLee3:
    def distributeCoins(self, root, pre=None):
        if not root: return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre: pre.val += root.val - 1
        return res + abs(root.val - 1)









