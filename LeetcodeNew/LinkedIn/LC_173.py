
# @param root, a binary search tree's root node
def __init__(self, root):
    self.stack = []
    self.helper(root)

def helper(self, root):
    while root:
        self.stack.append(root)
        root = root.left

# @return a boolean, whether we have a next smallest number
def hasNext(self):
    return self.stack  # or self.stack != []

# @return an integer, the next smallest number
def next(self):
    node = self.stack.pop()
    self.helper(node.right)
    return node.val

