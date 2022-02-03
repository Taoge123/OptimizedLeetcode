
"""
Similar with -> 803
https://leetcode.com/problems/bricks-falling-when-hit/



https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1507572/Python-Binary-Search-and-DFS
https://leetcode-cn.com/problems/last-day-where-you-can-still-cross/solution/ni-neng-chuan-guo-ju-zhen-de-zui-hou-yi-9j20y/
https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1403949/Python3.-Binary-search-%2B-dfs
https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1440354/Python-Binary-Search




https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1507572/Python-Binary-Search-and-DFS
https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1403907/C%2B%2BJavaPython-Binary-Search-and-BFS-Clean-and-Concise

"""


class Solution:
    def latestDayToCross(self, row: int, col: int, cells):

        res = 0
        n = len(cells)
        left, right = 0, n - 1

        def flood(matrix, pos):
            for i in range(pos + 1):
                matrix[cells[i][0] - 1][cells[i][1] - 1] = 1

        def check(matrix, row, col):
            for j in range(col):
                if not matrix[0][j] and dfs(matrix, 0, j):
                    return True
            return False

        def dfs(matrix, i, j):
            if i == row - 1:
                return True
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= row or y < 0 or y >= col or matrix[x][y]:
                    continue
                matrix[x][y] = '#'
                if dfs(matrix, x, y):
                    return True
            return False

        ## Binary searching the exact cell where you are  finally unable  to cross the land
        while left <= right:
            mid = (left + right) // 2
            matrix = [[0 for j in range(col)] for i in range(row)]
            flood(matrix, mid)
            if check(matrix, row, col):
                left = mid + 1
            else:
                right = mid - 1
        return left






