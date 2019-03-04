
# (reverse preorder traversal)
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


class Solution22:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)
        tempRight = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tempRight
        return
"""
An inorder python solution
         *
       /
      n
   /     \
 left   right
  \ 
   *
    *
     \
      p

The idea is very simple. Suppose n is the current visiting node, 
and p is the previous node of preorder traversal to n.right.

We just need to do the inorder replacement:

n.left -> NULL

n.right - > n.left

p->right -> n.right

"""
class Solution2:
    # @param root, a tree node
    # @return nothing, do it in place
    prev = None
    def flatten(self, root):
        if not root:
            return
        self.prev = root
        self.flatten(root.left)

        #temp is right, right point to left, left point to None, prev.right = right
        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        self.flatten(temp)


class Solution3:
    def flatten(self, root):
        while root:
            if root.left:
                self.flatten(root.left)
                tail = root.left
                while tail.right:
                    tail = tail.right
                tail.right = root.right
                root.right = root.left
                root.left = None
            root = root.right









