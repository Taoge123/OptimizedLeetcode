

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        index = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:index +1], inorder[0:index])
        root.right = self.buildTree(preorder[index +1:], inorder[index + 1:])

        return root
















