"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        """
        inorder   = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        need to build the tree from right to left, because we are popping from the last element from the postorder array.
        """
        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index + 1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)

            return root


















