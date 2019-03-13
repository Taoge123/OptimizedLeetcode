

"""
This is similar to binary cameras
Also similar to: https://leetcode.com/problems/sum-of-distances-in-tree/description/

https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/251221/Detailed-post-order-explanation-with-python.
https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/



Given the root of a binary tree with N nodes,
each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
(The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].
Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionOfficial:
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans


class SolutionLee:
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


"""
As somebody may not like global variable,
here is the recursive version without helper.

"""
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.total = 0
        self.Calculate(root)
        return self.total


    def Calculate(self,node):
        if node == None:
            return 0
        lc = self.Calculate(node.left)
        rc = self.Calculate(node.right)
        val = lc + rc + node.val - 1
        self.total += abs(val)
        return val


class Solution2:
    def distributeCoins(self, root):
        result = [0]
        def postorder(node):
            if not node:
                return 0
            left, right = postorder(node.left), postorder(node.right)
            result[0] += abs(left) + abs(right)
            return node.val + left + right - 1
        postorder(root)
        return result[0]




class Solution:
    def distributeCoins(self, root, pre=None):
        if not root: return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)

        if pre:
            pre.val += root.val - 1

        return res + abs(root.val - 1)



