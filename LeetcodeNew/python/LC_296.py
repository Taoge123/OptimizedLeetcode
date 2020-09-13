"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.


本题的笨方法，就是存下所有persons的位置，然后遍历每个点，计算该点到所有person的曼哈顿距离之后。时间复杂度是o(MNK).

比较聪明的办法就是利用数学的性质。对于任意的序列x1,x2,x3,...,xn,我们要找到其中的一个k，使得

min_{k} |xi-k| for i=1,2,..,n

利用求导（非连续函数的特殊求导定义）的方法，可以得到如下的结论，最优的k是这个数列的中位数，注意不是平均数。如果序列里面有偶数个，那么中位数就是中间两个数的平均值。

在本题里，最优点坐标的X可以直接判定是所有persons横坐标的中位数，Y就是所有persons纵坐标的中位数。知道了（X，Y）就可以直接计算所有人到该点的曼哈顿距离。


"""

class Solution:
    def minTotalDistance(self, grid):

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        pos = []
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pos.append([i, j])

        pos = sorted(pos, key=lambda point: point[0])
        x = pos[len(pos) // 2][0]
        for point in pos:
            res += abs(point[0] - x)

        pos = sorted(pos, key=lambda point: point[1])
        y = pos[len(pos) // 2][1]
        for point in pos:
            res += abs(point[1] - y)

        return res







