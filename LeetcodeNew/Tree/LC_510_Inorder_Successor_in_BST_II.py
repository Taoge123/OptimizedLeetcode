
"""
if node.right, find the most left node in the right subtree of the node;
otherwise, find a parent upward that contains the node in its left subtree
(and thus the node is the most right one in the subtree).

"""

class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node:
            return None

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            while node.parent and node.parent.val < node.val:
                node = node.parent

        return node.parent






