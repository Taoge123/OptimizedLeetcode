
class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1 ]= max(1, 1 - dungeon[-1][-1])
        for j in range( n -2, -1, -1):
            dp[-1][j] = max(dp[-1][ j +1] - dungeon[-1][j], 1)
        for i in range( m -2, -1, -1):
            dp[i][-1] = max(dp[ i +1][-1] - dungeon[i][-1], 1)
        for i in range( m -2, -1, -1):
            for j in range( n -2, -1, -1):
                dp[i][j] = max(min(dp[ i +1][j], dp[i][ j +1]) - dungeon[i][j], 1)
        return dp[0][0]


#     def calculateMinimumHP(self, dungeon):
#         if not dungeon:
#             return
#         r, c = len(dungeon), len(dungeon[0])
#         dp = [[0 for _ in range(c)] for _ in range(r)]
#         dp[-1][-1] = max(1, 1-dungeon[-1][-1])
#         for i in range(c-2, -1, -1):
#             dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])
#         for i in range(r-2, -1, -1):
#             dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
#         for i in range(r-2, -1, -1):
#             for j in range(c-2, -1, -1):
#                 dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])

#         for i in dungeon:
#             print(i)
#         for i in dp:
#             print(i)

#         return dp[0][0]






