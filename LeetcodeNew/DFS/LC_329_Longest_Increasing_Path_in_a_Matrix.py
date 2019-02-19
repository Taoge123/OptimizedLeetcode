
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        self.directions = [(1 ,0) ,(-1 ,0) ,(0 ,1) ,(0 ,-1)]
        m = len(matrix)
        n = len(matrix[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                cur_len = self.dfs(i, j, matrix, cache, m, n)
                res = max(res, cur_len)
        return res

    def dfs(self, i, j, matrix, cache, m, n):
        if cache[i][j] != -1:
            return cache[i][j]
        res = 1
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(x, y, matrix, cache, m, n)
            res = max(length, res)
        cache[i][j] = res
        return res