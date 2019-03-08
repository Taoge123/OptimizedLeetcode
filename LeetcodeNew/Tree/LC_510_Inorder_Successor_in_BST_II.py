
"""
if node.right, find the most left node in the right subtree of the node;
otherwise, find a parent upward that contains the node in its left subtree
(and thus the node is the most right one in the subtree).

"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.val < node.val:
            node = node.parent
        return node.parent



class Solution2:
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        val = node.val
        # If node has right subtree, just look for extreme left node in it
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            # Else go up till root, look for val greater than given node val
            while node and (node.val <= val):
                node = node.parent
        return node








