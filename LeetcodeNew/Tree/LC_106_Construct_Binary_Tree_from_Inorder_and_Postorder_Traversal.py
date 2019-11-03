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
"""
That's because inorder traversal goes 'Left-Parent-Right'
and postorder traversal goes 'Left-Right-Parent'.
And, postorder.pop() keeps picking the right-most element of the list,
that means it should go 'Parent-(one of parents of) Right (subtree) - Left'.
So, switching the order doesn't work.

Optimized Solution
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why.


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:

        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index + 1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)

            return root




