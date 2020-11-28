
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root):
        self.leaves = collections.deque()
        self.root = root
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.leaves.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v):
        node = self.leaves[0]
        self.leaves.append(TreeNode(v))
        if not node.left:
            node.left = self.leaves[-1]
        else:
            node.right = self.leaves[-1]
            self.leaves.popleft()
        return node.val

    def get_root(self):
        return self.root


