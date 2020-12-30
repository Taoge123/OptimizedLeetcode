import functools

class Solution:
    def ways(self, pizza, k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        mod = pow(10, 9) + 7
        summ = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                summ[i][j] = summ[i][j + 1] + summ[i + 1][j] - summ[i + 1][j + 1] + (pizza[i][j] == 'A')


        @functools.lru_cache(None)
        def dfs(row, col, cuts):
            if cuts == 0 and summ[row][col] > 0:
                return 1

            if cuts == 0 or summ[row][col] == 0:
                return 0

            res = 0

            for i in range(row, m):
                if summ[row][col] > summ[i][col]:
                    res += dfs(i, col, cuts - 1)

            for j in range(col, n):
                if summ[row][col] > summ[row][j]:
                    res += dfs(row, j, cuts - 1)

            return res % mod

        return dfs(0, 0, k - 1)



