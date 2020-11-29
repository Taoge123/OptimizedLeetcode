import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = collections.deque()
        queue.append(root)
        even = True

        while queue:
            size = len(queue)
            prev = float('-inf') if even else float('inf')
            for _ in range(size):
                node = queue.popleft()
                # invalid case on even level
                if even and (node.val % 2 == 0 or node.val <= prev):
                    return False
                # invalid case on odd level
                if not even and (node.val % 2 == 1 or node.val >= prev):
                    return False

                prev = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            even = not even

        return True




class SolutionDFS:
    def isEvenOddTree(self, root):
        self.table = {}
        return self.dfs(root, 0)

    def dfs(self, root, level):
        if not root:
            return True
        # Check node is even, and level is even
        if level % 2 == 0 and root.val % 2 == 0:
            return False
        # Check node is odd, and level is odd
        if level % 2 == 1 and root.val % 2 == 1:
            return False
        if not level in self.table:
            self.table[level] = [root.val]
        else:
            if level % 2 == 0:
                # Check sort for even level
                if root.val <= self.table[level][-1]:
                    return False
            else:
                # Check sort for odd level
                if root.val >= self.table[level][-1]:
                    return False
            self.table[level].append(root.val)

        return self.dfs(root.left, level + 1) and self.dfs(root.right, level + 1)



