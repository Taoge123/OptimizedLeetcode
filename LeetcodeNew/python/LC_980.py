"""
934 - similar

"""
"""
思路分析：
这和旅行商问题有异曲同工之妙，对旅行商问题有兴趣的可以参考这道题

关键点就是在于如何表示已经行走过的路径，这道题提示中说总格子数不超过20，那么用一个20空间大小的bool数组来表示可以吗？
未必不行，但没有必要。希望大家对这种题目敏感一点，用01代表状态的时候，要能反映过来可以用位。20位整数一个int型变量就可以保存，每一位上1代表已经走过，0代表还没走过。

然后判断处终点情况的位表示情况，例如对于示例2中的网格，终点情况应该是011111111111，因为最后一个数是-1，所以不能到达，故位表示的首位是0。依次类推，将起点的位表示计算出来，然后dfs遍历。

当然，如果你做了旅行商那道题的话，你应该知道其实这里面是包含重复计算的，我们应该使用记忆化的思想去递归。想知道为何有重复计算可以参考这篇博客。

懒得看也没关系，看下面的代码也ok。


"""



class Solution:
    def uniquePathsIII(self, grid) -> int:
        self.res = 0
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        self.dfs(grid, x, y, empty, end)
        return self.res

    def dfs(self, grid, x, y, empty, end):
        m, n = len(grid), len(grid[0])
        # grid[x][y] < 0 走过的地方都调成负数, 保证只走一次
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0:
            return

        if (x, y) == end:
            self.res += empty == 0
            return
        grid[x][y] = -2
        self.dfs(grid, x + 1, y, empty - 1, end)
        self.dfs(grid, x - 1, y, empty - 1, end)
        self.dfs(grid, x, y + 1, empty - 1, end)
        self.dfs(grid, x, y - 1, empty - 1, end)
        grid[x][y] = 0


class SolutionBitMask:
    def uniquePathsIII(self, grid):
        n, m = len(grid), len(grid[0])
        start = 0
        final = 0
        fi = fj = 0
        # 先获得起始位置和终点位置，以及起始和终点的位表示
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    final += 1 << (i * m + j)
                if grid[i][j] == 1:
                    start += 1 << (i * m + j)
                    si, sj = i, j
                if grid[i][j] == 2:
                    fi, fj = i, j

        # 使用记忆化思想，存储已经走过的情况
        cache = {(start, si, sj): 1}
        return self.dfs(grid, final, fi, fj, cache)

    def dfs(self, grid, status, i, j, cache):
        n, m = len(grid), len(grid[0])
        if (status, i, j) in cache:
            return cache[status, i, j]
        res = 0
        now_status = 1 << (i * m + j)
        # 每次向四个临近结点移动，但要保证临近结点能走
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < n and 0 <= y < m and grid[x][y] != -1:
                # 保证每个空白位置只走一遍
                mask = 1 << (x * m + y)
                if status & mask:
                    res += self.dfs(grid, status ^ now_status, x, y, cache)
        cache[status, i, j] = res
        return res

