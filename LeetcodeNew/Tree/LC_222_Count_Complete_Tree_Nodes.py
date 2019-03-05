

"""
Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

compare the depth between left sub tree and right sub tree.
A, If it is equal, it means the left sub tree is a full binary tree
B, It it is not , it means the right sub tree is a full binary tree
Nice solution, add a word, comparing the depth between left sub tree and right sub tree,
If it is equal, it means the left sub tree is a perfect binary tree, not only a full binary tree.
If it is not , it means the right sub tree is a perfect binary tree.


class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
O(log(n) ^ 2):
The idea is compare the left subtree depth with the right subtree depth.
If they are equal, we have a full tree, thus we return 2^height - 1.
If they aren't equal, we do recursive call for the root.left subtree and the root.right subtree.
Note that everytime we do recursive call for the root.left subtree or the root.right subtree,
one of them must be a full tree due to the condition of the problem.

"""

class Solution2:
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


class Solution:
    # @param {TreeNode} root
    # @return {integer}
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

class SolutionCaikehe:
    def countNodes(self, root):
        if not root:
            return 0
        h1 = self.height(root.left)
        h2 = self.height(root.right)
        if h1 > h2:  # right child is full
            return self.countNodes(root.left) + 2 ** h2
        else:  # left child is full
            return self.countNodes(root.right) + 2 ** h1

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









