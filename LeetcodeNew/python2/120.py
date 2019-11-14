
# class Solution:
#     def minimumTotal(self, triangle):

#         if not triangle:
#             return

#         res = [[0 for i in range(len(row))] for row in triangle]
#         res[0][0] = triangle[0][0]
#         for i in range(1, len(triangle)):
#             for j in range(len(triangle[i])):
#                 if j == 0:
#                     res[i][j] = res[i-1][j] + triangle[i][j]
#                 elif j == len(triangle[i]) - 1:
#                     res[i][j] = res[i-1][j-1] + triangle[i][j]
#                 else:
#                     res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
#         return min(res[-1])


class Solution:
    def minimumTotal(self, triangle):
        res = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                res[i] = row[i] + min(res[i], res[ i +1])
        return res[0]









