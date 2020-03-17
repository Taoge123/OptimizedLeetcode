"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])

            return root


class Solution2:
    def buildTree(self, preorder, inorder):
        return self.dfs(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def dfs(self, preorder, inorder, preStart, preEnd, inStart, inEnd):
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None

        rootVal = preorder[preStart]
        root = TreeNode(rootVal)
        inIndex = inorder.index(rootVal)

        root.left = self.dfs(preorder, inorder, preStart + 1, inIndex, inStart, inIndex - 1)
        root.right = self.dfs(preorder, inorder, preStart + inIndex + 1 - inStart, preEnd, inIndex + 1, inEnd)

        return root


class Solution3:
    def buildTree(self, preorder, inorder):
        preorder.reverse()
        inorder.reverse()
        return self.build(None, inorder, preorder)

    def build(self, stop, inorder, preorder):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = self.build(root.val, inorder, preorder)
            inorder.pop()
            root.right = self.build(stop, inorder, preorder)
            return root

