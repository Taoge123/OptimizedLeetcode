
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        table = self.hashset(root1, target)
        return self.check(root2, table)

    def hashset(self, node, target):
        if not node:
            return set()
        return self.hashset(node.left, target) | self.hashset(node.right, target) | {target - node.val}


    def check(self, node, table):
        if not node:
            return False
        return self.check(node.left, table) or self.check(node.right, table) or (node.val in table)



