"""
https://leetcode.com/problems/count-univalue-subtrees/solution/


"""

class Solution1:
    def countUnivalSubtrees(self, root):
        self.ans = 0
        def recurse(node, parent):
            if not node:
                return True
            left = recurse(node.left, node.val)
            right = recurse(node.right, node.val)
            if left and right:
                self.ans += 1
            return left and right and node.val == parent
        recurse(root, None)
        return self.ans


class Solution2:

    def countUnivalSubtrees(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right) + (1 if self.same(root, root.val) else 0)

    def same(self, root, val):
        if not root: return True
        if root.val != val: return False
        return self.same(root.left, val) and self.same(root.right, val)


class Solution3:
    def countUnivalSubtrees(self, root):
        if root is None: return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):

        # base case - if the node has no children this is a univalue subtree
        if node.left is None and node.right is None:
            # found a univalue subtree - increment
            self.count += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtrees and if they have the same value
        # also recursively call is_uni for children
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        # increment self.res and return whether a univalue tree exists here
        self.count += is_uni
        return is_uni


class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def is_valid_part(self, node, val):

        # considered a valid subtree
        if node is None: return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val




