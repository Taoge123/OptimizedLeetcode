"""
https://www.youtube.com/watch?v=FRllaNUffZM

ntuition
If root is leaf,
we compare the limit and root.val,
and return the result directly.

If root is leaf,
we recursively call the function on root's children with limit = limit - root.val.

Note that if a node become a new leaf,
it means it has no valid path leading to an original leaf,
we need to remove it.


Explanation
if root.left == root.right == null, root is leaf with no child {
    if root.val < limit, we return null;
    else we return root.
}
if root.left != null, root has left child {
    Recursively call sufficientSubset function on left child,
    with limit = limit - root.val
}
if root.right != null, root has right child {
    Recursively call sufficientSubset function on right child,
    with limit = limit - root.val
}
if root.left == root.right == null,
root has no more children, no valid path left,
we return null;
else we return root.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None

        if self.isLeaf(root):
            if root.val < limit:
                return None
            else:
                return root

        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)

        #check new leaves
        if self.isLeaf(root):
            return None
        else:
            return root


    def isLeaf(self, node):
        return not node.left and not node.right




