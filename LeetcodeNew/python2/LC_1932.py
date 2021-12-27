
"""
https://leetcode.com/problems/merge-bsts-to-create-single-bst/discuss/1330156/Python-clean-in-order-traversal-solution-O(N)-O(N)

"""


import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right







class SolutionTony:
    def canMerge(self, trees):

        nodes = {}
        indegree = collections.defaultdict(int)

        for node in trees:
            if node.val not in indegree:
                indegree[node.val] = 0
            if node.left:
                indegree[node.left.val] += 1
                if node.left.val not in nodes:
                    nodes[node.left.val] = node.left
            if node.right:
                indegree[node.right.val] += 1
                if node.right.val not in nodes:
                    nodes[node.right.val] = node.right
            nodes[node.val] = node

        sources = [k for k, v in indegree.items() if v == 0]
        if len(sources) != 1:
            return None

        self.cur = float('-inf')
        self.not_valid = False
        visited = set()

        def inorder(val):
            # check cycle
            if val in visited:
                self.not_valid = True
                return
            visited.add(val)
            node = nodes[val]
            if node.left:
                node.left = inorder(node.left.val)

            # check inorder increasing
            if val <= self.cur:
                self.not_valid = True
                return
            self.cur = val
            if node.right:
                node.right = inorder(node.right.val)

            return node

        root = inorder(sources[0])
        # print(len(visited), len(nodes), self.not_valid)
        # print(root.val)
        if len(visited) != len(nodes) or self.not_valid:
            return None
        return root



class SolutionRika:  # BEST
    def canMerge(self, trees):
        # 存储all leaf node.val 的set
        leaves = set()
        # 存储 each root --> hashmap {node.val : node}
        subtree = dict()
        for root in trees:
            if root.left:
                leaves.add(root.left.val)
            if root.right:
                leaves.add(root.right.val)
            subtree[root.val] = root

        for root in trees:
            if root.val not in leaves:  # get unique root --> root of merged tree
                subtree.pop(root.val)  # remove it from subtree hashmap
                if self.dfs(subtree, root, -float('-inf'), -float('inf')) and not subtree:  # if build BTS and all subtree are used
                    return root
                else:
                    return None

        return None

    def dfs(self, subtree, root, minn, maxx):
        if not root:
            return True

        if minn >= root.val or root.val >= maxx:
            return False

        # if leaf nodes has the same value as root in subtree ---> merge
        if not root.left and not root.right and root.val in subtree:
            root.left = subtree[root.val].left
            root.right = subtree[root.val].right
            subtree.pop(root.val)  # remove root in subtree --> to ensure all subtrees are merged at the end

        return self.dfs(subtree, root.left, minn, root.val) and self.dfs(subtree, root.right, root.val, maxx)

