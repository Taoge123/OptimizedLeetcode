
"""
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 8 2 7 3 6 4 5


"""


class Solution:
    def constructArray(self, n: int, k: int):
        res = [0] * n
        left = 1
        right = n
        for i in range(n):
            if k % 2 != 0:
                res[i] = left
                left += 1
            else:
                res[i] = right
                right -= 1
            if k > 1:
                k -= 1
        return res


n = 8
k = 4
a = Solution()
print(a.constructArray(n, k))



