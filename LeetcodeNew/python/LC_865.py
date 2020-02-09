"""
 The question is unclear. For example, if we did not have nodes 7 and 4, the answer would
 be TreeNode(3). If we did not have node 4, the answer would be TreeNode(7) and not
 TreeNode(2). Similarly, if we did not have 7, the answer would be TreeNode(4) and not
 TreeNode(2).

 Intuitively, we should be traversing from the children to the parent and calculate the
 height from bottom. So the null nodes would have height 0. The leaf nodes would have the
 height 1 and the root would have the max height.

 At each node, we keep a pair<height_of_node_from_bottom, node>. At a given node,
 if we realize that the leftHeight == rightHeight, it means we have found the deepest subtree
 rooted at node.

 If leftHeight > rightHeight, it means the deepest subtree must be rooted
 at left child.

 If rightHeight > leftHeight, it means the deepest subtree must be rooted
 at right child.

 * Which traversal allows us to traverse from bottom-up? Postorder! So we use it in the code.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return 0, None
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left[0] > right[0]:
            return left[0] + 1, left[1]
        elif left[0] < right[0]:
            return right[0] + 1, right[1]
        else:
            return left[0] + 1, root




