"""
Use recursion. Pass down two parameters:
lessThan (which means that all nodes in the the current subtree must be smaller
than this value) and largerThan (all must be larger than it).
Compare root of the current subtree with these two values.
Then, recursively check the left and right subtree of the current one.
Take care of the values passed down.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))


class SolutionInorder:
    # @param root, a tree node
    # @return a boolean
    # 7:38
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)




