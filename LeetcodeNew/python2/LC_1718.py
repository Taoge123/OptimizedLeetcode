"""
https://github.com/wisdompeak/LeetCode/tree/master/DFS/1718.Construct-the-Lexicographically-Largest-Valid-Sequence

"""


class Solution:
    def constructDistancedSequence(self, n):

        res = [0 for i in range(2 * n - 1)]
        visited = [0 for i in range(n + 1)]

        def dfs(i):
            if i == 2 * n - 1:
                return True
            if res[i] > 0:
                return dfs(i + 1)

            for j in range(n, 0, -1):
                if visited[j] == 1:
                    continue
                if j > 1 and (i + j >= 2 * n - 1 or res[i + j] > 0):
                    continue
                visited[j] = 1
                res[i] = j

                if j > 1:
                    res[i + j] = j

                if dfs(i + 1):
                    return True

                visited[j] = 0
                res[i] = 0

                if j > 1:
                    res[i + j] = 0
            return False

        dfs(0)
        return res







