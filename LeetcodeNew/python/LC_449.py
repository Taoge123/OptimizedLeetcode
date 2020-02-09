
"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

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

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))




