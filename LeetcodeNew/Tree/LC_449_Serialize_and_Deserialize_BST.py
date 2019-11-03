
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):

        preorder = []
        self.helper(root, preorder)
        print(preorder)
        return ' '.join(map(str, preorder))

    def helper(self, root, preorder):
        if not root:
            return
        preorder.append(root.val)
        self.helper(root.left, preorder)
        self.helper(root.right, preorder)

    def deserialize(self, data):

        if not data:
            return None
        data = collections.deque(int(val) for val in data.split())
        return self.build(data, float('-inf'), float('inf'))

    def build(self, preorder, min, max):
        if not preorder:
            return None

        if preorder and preorder[0] > min and preorder[0] < max:
            val = preorder.popleft()
            root = TreeNode(val)
            root.left = self.build(preorder, min, root.val)
            root.right = self.build(preorder, root.val, max)
            return root



