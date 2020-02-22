
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = collections.deque([(root, 0)])
        res = 1

        while queue:
            level = collections.deque([])
            for i in range(len(queue)):
                node = queue.popleft()
                if node[0].left:
                    level.append((node[0].left, node[1] * 2))
                if node[0].right:
                    level.append((node[0].right, node[1] * 2 + 1))

            if level:
                res = max(res, level[-1][1] - level[0][1] + 1)

            queue = level
        return res


class Solution2:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        left = {}
        self.dfs(root, left, 0, 0)
        return self.res

    def dfs(self, node, left, depth, pos):
        if node:
            # left.setdefault(depth, pos)
            if depth not in left:
                left[depth] = pos
            self.res = max(self.res, pos - left[depth] + 1)
            self.dfs(node.left, left, depth + 1, pos * 2)
            self.dfs(node.right, left, depth + 1, pos * 2 + 1)









