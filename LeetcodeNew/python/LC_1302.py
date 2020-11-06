import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            res = 0
            for i in range(len(queue)):
                node = queue.popleft()
                res += node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res




