"""
"clone graph" (#133),

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class SolutionTony:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.tree = {}
        self.dfs(root)
        # print(self.tree[root.val])
        return self.tree[root]

    def dfs(self, node):
        if not node:
            return node
        if node in self.tree:
            return self.tree[node]

        newNode = Node(node.val)
        self.tree[node] = newNode
        for nei in node.children:
            newNode.children.append(self.dfs(nei))

        return newNode


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        newRoot = Node(root.val)
        for child in root.children:
            newRoot.children.append(self.cloneTree(child))

        return newRoot


