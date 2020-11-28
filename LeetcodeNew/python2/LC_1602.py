import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:

        if not root:
            return []

        queue = collections.deque([])
        queue.append([root, 0])
        while queue:
            node, level = queue.popleft()
            if node == u:
                if queue and queue[0][1] == level:
                    return queue[0][0]
                else:
                    return None
            if node.left:
                queue.append([node.left, level + 1])

            if node.right:
                queue.append([node.right, level + 1])




class Solution2:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if not root:
            return []

        queue = collections.deque([root])
        while queue:
            next_queue = collections.deque()
            prev = None

            while queue:
                node = queue.popleft()
                if node == u:
                    return prev

                if node.right:
                    next_queue.append(node.right)
                if node.left:
                    next_queue.append(node.left)
                prev = node

            queue = next_queue
        return None

