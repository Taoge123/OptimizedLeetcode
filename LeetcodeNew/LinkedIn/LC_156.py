

# suppose the root.left part has been upsideDowned,
# then connect the root node (not root) to the right
# side of the right-most node of the already upsideDowned
# root.left part, root.right to the left side
def upsideDownBinaryTree(self, root):
    if not root or (not root.left and not root.right):
        return root
    node = self.upsideDownBinaryTree(root.left)
    tmp = node
    while tmp.right:
        tmp = tmp.right
    tmp.right = TreeNode(root.val)
    tmp.left = root.right
    return node
