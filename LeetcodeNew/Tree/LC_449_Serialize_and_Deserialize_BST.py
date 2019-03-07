
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))


class Codec2:

    def serialize(self, root):
        res, stk = [], []
        while stk or root:
            if root:
                res.append(str(root.val))
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                root = root.right
        return ' '.join(res)

    def deserialize(self, data):
        if not data:
            return None
        data = map(int, data.split(' '))
        stk = []
        root = node = TreeNode(data[0])
        for n in data[1:]:
            if n < node.val:
                node.left = TreeNode(n)
                stk.append(node)
                node = node.left
            else:
                while stk and stk[-1].val < n:
                    node = stk.pop()
                node.right = TreeNode(n)
                node = node.right
        return root


from collections import deque


class Codec:
    # recursive function to serialize BST
    # using a pre-order traversal
    # simply stores node values to a list
    def serialize_bst(self, root, preorder):
        if root is None:
            return
        preorder.append(str(root.val))
        self.serialize_bst(root.left, preorder)
        self.serialize_bst(root.right, preorder)

    # serialize BST to pre-order traversal
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        self.serialize_bst(root, preorder)
        return ','.join(preorder)

    # recursive function to deserialize BST from preorder queue
    def deserialize_bst(self, queue, maximum):
        # base case: empty queue
        if len(queue) == 0:
            return None

        # if the head of the queue is too big
        # then this node is not meant to be placed here
        if int(queue[0]) > maximum:
            return None

        # create root node
        root = TreeNode(int(queue.popleft()))

        # create left and right subtrees
        root.left = self.deserialize_bst(queue, root.val)
        root.right = self.deserialize_bst(queue, maximum)

        # return root node
        return root

    # deserialize BST pre-order traversal
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # sanity check: empty input be ignored, don't creat queue
        if len(data) == 0:
            return None
        queue = deque(data.split(','))
        # the maximum value is infinity
        root = self.deserialize_bst(queue, float('inf'))
        return root    




