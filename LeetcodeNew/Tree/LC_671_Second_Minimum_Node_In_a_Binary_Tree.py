
"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/discuss/233767/Python-iterative-and-recursive-preorder-solutions-beats-100


Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node.
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value
in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

"""
"""
Based on the special property of the tree, 
we can guarantee that the root node is the smallest node in the tree. 
We just have to recursively traverse the tree and find a node that is bigger than the root node 
but smaller than any existing node we have come across.
"""

class Solution0:
    def findSecondMinimumValue(self, root):
        res = [float('inf')]
        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return -1 if res[0] == float('inf') else res[0]


class Solution1:
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if node:
                uniques.add(node.val)
                dfs(node.left)
                dfs(node.right)

        uniques = set()
        dfs(root)

        min1, ans = root.val, float('inf')
        for v in uniques:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1


class Solution2:
    def findSecondMinimumValue(self, root):
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1


class SolutionBFS:
    def findSecondMinimumValue(self, root):
        if not root or not root.left: return -1
        s = [root]
        smallest = float('inf')
        while s:
            temp = []
            for i in s:
                if i.val > root.val:
                    smallest = min(smallest, i.val)
                elif i.left:
                    temp.append(i.left)
                    temp.append(i.right)
            s = temp
        return -1 if smallest == float('inf') else smallest

