class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        return self.dfs(root, leaf, None)

    def dfs(self, root, node, prev):
        # set and break pointers between node and prev
        parent = node.parent
        node.parent = prev
        if node.left == prev:
            node.left = None
        if node.right == prev:
            node.right = None

        # stopping condition
        if node == root:
            return node

        # set right child
        if node.left:
            node.right = node.left
        # set left child
        node.left = self.dfs(root, parent, node)
        return node


