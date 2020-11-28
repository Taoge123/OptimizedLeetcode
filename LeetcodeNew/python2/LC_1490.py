"""
"clone graph" (#133),

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        newRoot = Node(root.val)
        for child in root.children:
            newRoot.children.append(self.cloneTree(child))

        return newRoot


