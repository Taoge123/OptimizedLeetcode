import functools

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        @functools.lru_cache(None)
        def dfs(n, k):
            if n == 1:
                return 0

            N = (1 << n) - 1
            if k <= N // 2:
                return dfs(n - 1, k)

            elif k == N // 2 + 1:
                return 1

            else:
                return 1 - dfs(n - 1, N - k + 1)

        return str(dfs(n, k))



class Solution2:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return '0'
        elif k == 2 ** (n - 1):
            return '1'
        elif k < 2 ** (n - 1):
            return self.findKthBit(n - 1, k)
        else:
            return self.reverse(self.findKthBit(n - 1, 2 ** n - k))

    def reverse(self, n):
        return '1' if n == '0' else '0'


