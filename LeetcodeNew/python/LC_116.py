"""
116. Populating Next Right Pointers in Each Node
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root



class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        stack = [root]

        while stack:
            node = stack.pop()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left

                stack.append(node.left)
                stack.append(node.right)

        return root





