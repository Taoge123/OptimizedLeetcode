"""
https://leetcode.com/problems/binary-tree-upside-down/discuss/49410/Explain-the-question-and-my-solution-Python
https://xlinux.nist.gov/dads/HTML/binaryTreeRepofTree.html

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1

The transform of the base three-node case is like below:

                         Root                   L
                         /  \                  /  \
                        L    R                R   Root
You can image you grab the L to the top, then the Root becomes it's right node,
and the R becomes its left node.

Knowing the base case, you can solve it recursively.

How? You keep finding the left most node, make it upside-down,
then make its parent to be its right most subtree recursively.

Here is a small point to be noticed, when you connect the root to the right subtree,
you need to make sure you are not copying the original root, otherwise it will become cyclic!
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root
        lRoot = self.upsideDownBinaryTree(root.left)
        rMost = lRoot
        while rMost.right:
            rMost = rMost.right

        root = lRoot
        rMost.left = root.right
        rMost.right = TreeNode(root.val)

        return root

"""
1. root's right node becomes the left node of the left node of root
2. root becomes the right node of root's left node
3. above rules apply on the left edge and return left node along the path.

"""

class Solution2:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
        #1 - 2 - 4 = then do modification on 4
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return left

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

a = Solution()
print(a.upsideDownBinaryTree(tree))




