"""
Use a tree example: [100, 50, 200, 25, 75, 99, 400]
Sorted Order: 25,50,75,100,150,200,400
You can have out of order 50 and 200: 25,200,75,100,150,50,400.
Notice in this case we have 2 out of order pairs: (200,75) and (150,50).
Simply swap 200 and 50.
What if 25/50 or 200/400 are swapped? In that case we will have just one out of order element.
3 and 4 give us our algorithm.

"""

import sys

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.order = []
        self.prev = None
        self.inorder(root)
        if len(self.order) == 2:
            self.swap(self.order[0][0], self.order[1][1])
        elif len(self.order) == 1:
            self.swap(self.order[0][0], self.order[0][1])
        return

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            self.order.append((self.prev, root))
        self.prev = root
        self.inorder(root.right)
        return

    def swap(self, r1, r2):
        r1.val, r2.val = r2.val, r1.val
        return



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # average O(lgn) space (worst case, O(n) space), recursively, one-pass
    def recoverTree2(self, root):
        self.prevNode = TreeNode(-sys.maxsize -1)
        self.first, self.second = None, None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.first and self.prevNode.val > root.val:
            self.first, self.second = self.prevNode, root
        if self.first and self.prevNode.val > root.val:
            self.second = root
        self.prevNode = root
        self.inorder(root.right)

    # average O(n+lgn) space, worst case O(2n) space, recursively, two-pass
    def recoverTree3(self, root):
        res = []
        self.helper(root, res)
        first, second = None, None
        for i in range(1, len(res)):
            if not first and res[ i -1].val > res[i].val:
                first, second = res[ i -1], res[i]
            if first and res[ i -1].val > res[i].val:
                second = res[i]
        first.val, second.val = second.val, first.val

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root)
            self.helper(root.right, res)


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        import collections
        queue, prev, current = collections.deque(), None, None
        queue.extend([root, None])
        while queue:
            prev = current
            current = queue.popleft()
            if prev:
                prev.next = current
                if not current:
                    queue.append(current)
            if current:
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)








