"""
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

"""

import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        return self.dfs([i for i in range(1, n + 1)])

    def dfs(self, lst):
        if not lst: return [None]
        res = []
        for i in range(len(lst)):
            for left in self.dfs(lst[:i]):
                for right in self.dfs(lst[i + 1:]):
                    node, node.left, node.right = TreeNode(lst[i]), left, right
                    res += [node]
        return res

#With cache
class Solution2:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
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



#use yield
class Solution3:
    # @return a list of tree node
    # 2:30
    def generateTrees(self, n):
        nodes = map(TreeNode, range(1, n+1))
        return map(copy.deepcopy, self.buildTree(nodes))

    def buildTree(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return

        for i in range(n):
            root = nodes[i]
            for left in self.buildTree(nodes[:i]):
                for right in self.buildTree(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root








