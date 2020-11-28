
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.right:
                if node.right.right in queue:
                    node.right = None
                    return root
                else:
                    queue.append(node.right)
            if node.left:
                if node.left.right in queue:
                    node.left = None
                    return root
                else:
                    queue.append(node.left)
        return root




