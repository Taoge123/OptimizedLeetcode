
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        res = []
        queue = collections.deque([(root, 1)])

        while queue:
            node, pos = queue.popleft()
            res.append(pos)
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))

        return len(res) == res[-1]



class Solution2:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        total, right_most = self.dfs(root, 1)
        return total == right_most

    # number of nodes, right_most_coords
    def dfs(self, root, coord):
        if not root:
            return 0, 0
        left = self.dfs(root.left, 2 * coord)
        right = self.dfs(root.right, 2 * coord + 1)

        total = left[0] + right[0] + 1
        right_most = max(coord, left[1], right[1])

        return total, right_most



"""
Use BFS to do a level order traversal,
add childrens to the bfs queue,
until we met the first empty node.

For a complete binary tree,
there should not be any node after we met an empty one.
"""


class Solution3:
    def isCompleteTree(self, root: TreeNode) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])







