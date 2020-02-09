
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode):

        queue = collections.deque([root])
        res = []
        while queue:
            summ = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                summ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(summ /size)

        return res








