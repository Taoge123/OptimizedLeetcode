"""
Serialization is the process of converting a data structure
or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

"""

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        if not root:
            return ""
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

            res.append(str(node.val) if node else '#')
        print(",".join(res))
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(nodes[0])
        i = 1
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if nodes[i] != '#':
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if nodes[i] != '#':
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
"""
   1
  2 5
 3  6 7
"""

a = Codec()
print(a.serialize(root))

