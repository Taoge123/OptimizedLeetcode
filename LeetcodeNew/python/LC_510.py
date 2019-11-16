

"""
510. Inorder Successor in BST II

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node.

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




