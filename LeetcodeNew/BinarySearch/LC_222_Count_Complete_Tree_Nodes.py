
"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

"""
compare the depth between left sub tree and right sub tree.
A, If it is equal, it means the left sub tree is a full binary tree
B, It it is not , it means the right sub tree is a full binary tree

"""


class Solution1:

    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)

#Iterative solution
class Solution2:
    def countNodes(self, root):

        # O(logn logn)
        h = self.height(root)
        nodes = 0
        while root:
            if self.height(root.right) == h - 1:
                nodes += 2 ** h  # left half (2 ** h - 1) and the root (1)
                root = root.right
            else:
                nodes += 2 ** (h - 1)
                root = root.left
            h -= 1
        return nodes

    def height(self, root):
        return -1 if not root else 1 + self.height(root.left)


class Solution3:
    def countNodes(self, root):
        leftdepth = self.getdepth(root, True)
        rightdepth = self.getdepth(root, False)

        if leftdepth == rightdepth:
            return 2 ** leftdepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getdepth(self, root, isLeft):
        if root is None:
            return 0
        if isLeft:
            return 1 + self.getdepth(root.left, isLeft)
        else:
            return 1 + self.getdepth(root.right, isLeft)



class SolutionCaikehe1:
    def countNodes(self, root):
        if not root:
            return 0
        h1, h2 = self.height(root.left), self.height(root.right)
        if h1 > h2:  # right child is full
            return self.countNodes(root.left) + 2 ** h2
        else:  # left child is full
            return 2 ** h1 + self.countNodes(root.right)

    # the height of the left-most leaf node
    def height1(self, root):
        h = 0
        while root:
            h += 1
            root = root.left
        return h

    def height(self, root):
        if not root:
            return 0
        return self.height(root.left) + 1



class Solution4:
    def countNodes(self, root):
        if not root:
            return 0
        l = self.depthLeft(root.left)
        r = self.depthRight(root.right)
        if l == r:
            return 2 ** (l + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def depthLeft(self, node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    def depthRight(self, node):
        d = 0
        while node:
            d += 1
            node = node.right
        return d


class Solution5:
    def countNodes(self, root):
        def f(root):
            if root == None:
                return 0
            return f(root.right) + f(root.left) + 1
        return f(root)

