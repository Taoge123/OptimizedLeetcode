"""
Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator1:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

class BSTIterator11:
    def __init__(self, root):
        self.last = root
        while self.last and self.last.right:
            self.last = self.last.right
        self.current = None
        self.g = self.iterate(root)


    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.current is not self.last


    # @return an integer, the next smallest number
    def next(self):
        return next(self.g)


    def iterate(self, node):
        if node is None:
            return
        for x in self.iterate(node.left):
            yield x
        self.current = node
        yield node.val
        for x in self.iterate(node.right):
            yield x

class BSTIterator2:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.q=[]
        self.allLeftIntoStack(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q:return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        cur = self.q.pop()
        self.allLeftIntoStack(cur.right)
        return cur.val

    def allLeftIntoStack(self,root):
        while root:
            self.q.append(root)
            root=root.left


class BSTIterator3:
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




