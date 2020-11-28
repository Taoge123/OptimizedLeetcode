import bisect

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionON2:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = bisect.bisect_right(preorder, preorder[0])
        root.left = self.bstFromPreorder(preorder[1:index])
        root.right = self.bstFromPreorder(preorder[index:])
        return root


class SolutionNLOGN:
    def bstFromPreorder(self, preorder) -> TreeNode:
        return self.helper(preorder, 0, len(preorder))

    def helper(self, preorder, i, j):
        if i == j:
            return None
        root = TreeNode(preorder[i])
        mid = bisect.bisect_right(preorder, preorder[i], i + 1, j)
        root.left = self.helper(preorder, i + 1, mid)
        root.right = self.helper(preorder, mid, j)
        return root


class SolutionON:
    def __init__(self):
        self.i = 0

    def bstFromPreorder(self, preorder, bound=float('inf')) -> TreeNode:
        if self.i == len(preorder) or preorder[self.i] > bound:
            return None

        root = TreeNode(preorder[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(preorder, root.val)
        root.right = self.bstFromPreorder(preorder, bound)

        return root


preorder = [8,5,1,7,10,12]
a = SolutionNLOGN()
print(a.bstFromPreorder(preorder))


