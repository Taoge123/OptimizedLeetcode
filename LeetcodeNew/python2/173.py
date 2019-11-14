
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        next = node.right
        while next:
            self.stack.append(next)
            next = next.left
        return node.val



    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

