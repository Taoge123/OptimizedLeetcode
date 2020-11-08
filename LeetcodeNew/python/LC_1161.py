import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 0
        res = 0
        maxi = float('-inf')
        queue = collections.deque()
        queue.append(root)
        while queue:
            level += 1
            summ = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                summ += node.val
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if maxi < summ:
                maxi = summ
                res = level

        return res


