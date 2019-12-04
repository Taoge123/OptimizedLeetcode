class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def test(self, arr):
        n = len(arr)
        res = [None] * (n+1)
        for i in range(n // 2):
            curr = TreeNode(arr[i])
            left = 2 * i + 1
            right = 2 * i + 2
            if 2 * i + 1 < n:
                res[left] = TreeNode(arr[left])
                curr.left = res[left]
            if 2 * i + 2 < n:
                res[right] = TreeNode(arr[right])
                curr.right = res[right]
            res[i] = curr

arr = [1,2,3,4,5,6,7,8,9]
a = Solution()
print(a.test(arr))


#        1
#       / \
#     -10   3
#     / \   \
#    1   7 -10


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Test:
    def maxSumPath(self, node):

        if not node:
            return 0

        self.res = float('-inf')
        self.helper(node)
        return self.res

    def helper(self, node):

        if not node:
            return 0

        left = max(self.helper(node.left), 0)
        right = max(self.helper(node.right), 0)

        self.res = max(self.res, node.val + left + right)

        return node.val + max(left, right)


"""
self.res = 7
"""













