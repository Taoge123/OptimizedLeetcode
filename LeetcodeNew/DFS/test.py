import functools

class Solution:
    def minCost(self, basket1, basket2) -> int:
        m, n = len(basket1), len(basket2)


        def dfs(i, j, sum1, sum2):
            print(i, j, sum1, sum2)
            if i >= m and j >= n:
                if sum1 == sum2:
                    return 0
                else:
                    return 10 ** 10

            if i >= m:
                if sum1 == (sum2 + sum(basket2[j:])):
                    return 0
                else:
                    return 10 ** 10
            elif j >= n:
                if sum2 == (sum1 + sum(basket1[i:])):
                    return 0
                else:
                    return 10 ** 10

            a1 = dfs(i + 1, j, sum1 + basket1[i], sum2)
            a2 = dfs(i, j + 1, sum1, sum2 + basket2[j])
            a3 = dfs(i + 1, j + 1, sum1 + basket2[j], sum2 + basket1[i]) + min(basket1[i], basket2[j])
            return min(a1, a2, a3)

        res = dfs(0, 0, 0, 0)
        if res == 10000000000:
            return -1
        else:
            return res

basket1 = [4,4,4,4,3]
basket2 = [5,5,5,5,3]

a = Solution()
print(a.minCost(basket1, basket2))