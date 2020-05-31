"""
https://www.youtube.com/watch?v=SEW3Vofoj_k
There are some explanations in order to help confused people.

1. if (is_root && !deleted) res.add(node)
    is_root: The node's parent is deleted. The node is the root node of the tree in the forest.
    !deleted: The node is not in the to_delete array.
2. We only need to add the root node of every tree.



"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def delNodes(self, root, to_delete):
        res = []
        self.target = set(to_delete)
        self.helper(root, True, res)
        return res

    def helper(self, root, is_root, res):
        if not root:
            return None

        need_delete = root.val in self.target

        # is_root - the node's parent is deleted. This node us the root node of the tree in the forest
        # not deleted means the node is not in to_delete
        #上游说是根节点 (上游被删了), 自己还不用被删
        if is_root and not need_delete:
            res.append(root)

        #if this root need to be deleted, left and right will be the root
        root.left = self.helper(root.left, need_delete, res)
        root.right = self.helper(root.right, need_delete, res)

        if need_delete:
            return None
        else:
            return root


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        res = []
        ds = set(to_delete)
        root = self.helper(root, ds, res)
        if root:
            res.append(root)
        return res

    def helper(self, root, ds, res):
        if not root:
            return None
        root.left = self.helper(root.left, ds, res)
        root.right = self.helper(root.right, ds, res)

        if root.val not in ds:
            return root

        if root.left:
            res.append(root.left)
        if root.right:
            res.append(root.right)
        return None


