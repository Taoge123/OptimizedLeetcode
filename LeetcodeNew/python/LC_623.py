
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot

        queue = collections.deque()
        queue.append(root)

        for i in range(d - 2):
            size = len(queue)
            for j in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        while queue:
            node = queue.popleft()
            left = node.left
            node.left = TreeNode(v)
            node.left.left = left

            right = node.right
            node.right = TreeNode(v)
            node.right.right = right

        return root


class SolutionDFS:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if d < 2:
            newRoot = TreeNode(v)
            if d == 0:
                newRoot.right = root
            else:
                newRoot.left = root
            return newRoot

        if not root:
            return None
        if d == 2:
            root.left = self.addOneRow(root.left, v, 1)
            root.right = self.addOneRow(root.right, v, 0)
        else:
            root.left = self.addOneRow(root.left, v, d - 1)
            root.right = self.addOneRow(root.right, v, d - 1)

        return root



