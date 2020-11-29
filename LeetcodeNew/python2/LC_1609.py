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





