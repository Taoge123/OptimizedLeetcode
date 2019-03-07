

"""
   1
 / | \
2  3  4

to:

 1
/
2
 \
  3
   \
    4

The left child of a binary node is the subtree encoding all the children of the corresponding n-ary node.
The right child of a binary node is a chain of the binary root nodes encoding each sibling of the n-ary node.
Hence the root node has no right binary child, because the root has no sibilings.

Here is the logic:
We start reading the N-ary nodes from the root.
Put all the first root's children at the RIGHT side of the Binary Tree,
the next root is the child node of the current node (parent).
What we do here for this node is exactly same
except we put all of this node's children to the LEFT side of the Binary Tree
(left side of this node in binary tree). For their childs we do the reverse,
which is putting their children in RIGHT side of the Binary Tree again, and so on.
We keep continuing puting children of the current nodes at RIGHT,
and LEFT sides till we reach to the end.
For decoding, we just read as we create it. Right, then Left, Right, then Left, and so on.
The picture illustrates the process:

"""

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




