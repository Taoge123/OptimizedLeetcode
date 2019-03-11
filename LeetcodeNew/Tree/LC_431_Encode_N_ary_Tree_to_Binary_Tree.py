
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
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.

        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None

        res = TreeNode(root.val)

        if root.children:
            res.left = self.encode(root.children[0])

        cur = res.left

        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right

        return res

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        res = Node(data.val, [])
        cur = data.left

        while cur:
            res.children.append(self.decode(cur))
            cur = cur.right

        return res




