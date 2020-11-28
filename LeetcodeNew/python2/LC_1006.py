

"""
F(n) = n * (n-1) // (n-2) + n - 3 - F(n-4) when n > 4


"""


class Solution:
    def clumsy(self, N: int) -> int:
        def helper(n):
            if n == 1:
                return -1
            if n == 2:
                return -2
            if n == 3:
                return -6
            if n == 4:
                return -5
            return helper(n - 4) - n * (n - 1) // (n - 2) + (n - 3)

        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        if N == 4:
            return 7
        return N * (N - 1) // (N - 2) + N - 3 + helper(N - 4)






