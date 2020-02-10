

"""
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

For example, you may encode the following 3-ary tree to a binary tree in this way:







Note that the above is just an example which might or might not work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Note:

N is in the range of [1, 1000]
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def encode(self, root):
        if not root:
            return None

        binary = TreeNode(root.val)  # create a binary root
        if not root.children:
            return binary

        binary.left = self.encode(root.children[0])  # left child of binary is the encoding of all n-ary children,
        node = binary.left  # starting with the first child.
        for child in root.children[1:]:  # other children of n-ary root are right child of previous child
            node.right = self.encode(child)
            node = node.right

        return binary

    def decode(self, data):
        if not data:
            return None

        nary = Node(data.val, [])  # create n-ary root
        node = data.left  # move to first child of n-ary root
        while node:  # while more children of n-ary root
            nary.children.append(self.decode(node))  # append to list
            node = node.right  # and move to next child

        return nary


class Codec2:
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None

        res = TreeNode(root.val)
        if len(root.children) > 0:
            res.left = self.encode(root.children[0])

        cur = res.left
        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right

        return res

    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None

        res =Node(data.val, [])
        cur = data.left

        while cur:
            res.children.append(self.decode(cur))
            cur = cur.right

        return res

