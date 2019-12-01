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











