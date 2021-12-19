
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDistance(self, root: [TreeNode], p: int, q: int):
        # print(root.val, root.left.val, root.right.val)
        lca = self.dfs(root, p, q)
        h1 = self.bfs(lca, p)
        h2 = self.bfs(lca, q)
        return h1 + h2

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if root.val == p or root.val == q:
            return root

        if left and right:
            return root
        if left or right:
            return left or right
        if not left and not right:
            return None


    def bfs(self, root, target):
        if not root:
            return 0

        queue = collections.deque()
        size = 0
        queue.append(root)
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.val == target:
                    return step
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            step += 1


