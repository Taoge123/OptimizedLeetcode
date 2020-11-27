class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class BSTIteratorTony:

    def __init__(self, root: TreeNode):
        self.arr = []
        self.inorder(root)
        print(self.arr)
        self.n = len(self.arr)
        self.pointer = -1

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.arr.append(node.val)
            self.inorder(node.right)

    def hasNext(self) -> bool:
        return self.pointer < self.n - 1

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]


class BSTIterator:
    def __init__(self, root: TreeNode):
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        self.arr = inorder(root)
        self.n = len(self.arr)
        self.pointer = -1

    def hasNext(self) -> bool:
        return self.pointer < self.n - 1

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]



class BSTIteratorIter:
    def __init__(self, root: TreeNode):
        self.last = root
        self.stack, self.arr = [], []
        self.pointer = -1

    def hasNext(self) -> bool:
        return self.stack or self.last or self.pointer < len(self.arr) - 1

    def next(self) -> int:
        self.pointer += 1

        # if the pointer is out of precomputed range
        if self.pointer == len(self.arr):
            # process all predecessors of the last node:
            # go left till you can and then one step right
            while self.last:
                self.stack.append(self.last)
                self.last = self.last.left
            curr = self.stack.pop()
            self.last = curr.right

            self.arr.append(curr.val)

        return self.arr[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]

