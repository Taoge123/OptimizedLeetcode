"""
883.Projection-Area-of-3D-Shapes
从题目给出的示意图就可以看出，从某一个方向看过去的投影高度，完全取决于这个方向上能看到的最高的那根柱子的高度。
比如对于x=i方向上，投影到y-z平面上的高度其实就是max{grid[i][j]} for j=0,1,2,...。所以对于y-z平面上的总投影面积，就是把所有的max{grid[i]}加起来就行。

对于x-z平面上的总投影也是如此处理。计算每个col[j]，表示第j列上的的最大值。再把所有col[j]相加。

对于x-y平面上的总投影，处理起来更为简单，就是计算grid[i][j]有多少个非零元素即可。
"""


class Solution:
    def projectionArea(self, grid) -> int:

        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res += 1
                row[i] = max(row[i], grid[i][j])
                col[j] = max(col[j], grid[i][j])

        for i in range(m):
            res += row[i]

        for j in range(n):
            res += col[j]

        return res






