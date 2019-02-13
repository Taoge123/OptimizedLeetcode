
class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            #Critical step to cache the value
            if not dp[i][j]:
                val = matrix[i][j]
                #al > matrix[i - 1][j] is to search for max decreasing, change the sign will get increasing
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))



#Bottom up solution
class Solution2:
    def longestIncreasingPath(self, matrix):
        matrix = {i + j * 1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        length = {}
        for z in sorted(matrix, key=matrix.get):
            length[z] = 1 + max([length[Z]
                                 for Z in (z + 1, z - 1, z + 1j, z - 1j)
                                 if Z in matrix and matrix[z] > matrix[Z]]
                                or [0])
        return max(length.values() or [0])


#Top down solution
class Solution3:
    def longestIncreasingPath(self, matrix):
        def length(z):
            if z not in memo:
                memo[z] = 1 + max([length(Z)
                                   for Z in (z + 1, z - 1, z + 1j, z - 1j)
                                   if Z in matrix and matrix[z] > matrix[Z]]
                                  or [0])
            return memo[z]
        memo = {}
        matrix = {i + j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        return max(map(length, matrix) or [0])




#Standard approach

class Solution3:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        memory = [[None] * len(matrix[0]) for i in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.helper(i, j, matrix, memory))
        return res

    def helper(self, i, j, matrix, memory):
        if memory[i][j]: return memory[i][j]
        count = 0
        if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
            count = max(count, self.helper(i - 1, j, matrix, memory))
        if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
            count = max(count, self.helper(i, j - 1, matrix, memory))
        if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
            count = max(count, self.helper(i + 1, j, matrix, memory))
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
            count = max(count, self.helper(i, j + 1, matrix, memory))
        memory[i][j] = count + 1
        return count + 1

