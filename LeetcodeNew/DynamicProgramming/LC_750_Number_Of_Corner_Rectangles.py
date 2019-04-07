
"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.



Example 1:

Input: grid =
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].


Example 2:

Input: grid =
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.


Example 3:

Input: grid =
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.


Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000
"""
import collections

class Solution1:
    def countCornerRectangles(self, grid):
        counts, res = collections.defaultdict(int), 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    for k in range(j):
                        if grid[i][k] == 1:
                            res += counts[(k, j)]
                            counts[(k, j)] += 1
        return res


class Solution2:
    def countCornerRectangles(self, grid):
        ends, res = collections.defaultdict(int), 0
        for row in grid:
            for i in range(len(row) - 1):
                for j in range(i + 1, len(row)):
                    if row[i] and row[j]:
                        res += ends[(i, j)]
                        ends[(i, j)] += 1
        return res


class SolutionLee:
    def countCornerRectangles(self, grid):
        n = len(grid[0])
        d = collections.Counter((i, j) for line in grid for i in range(n)
                                for j in range(i + 1, n) if line[i] and line[j])
        return sum(x * (x - 1) / 2 for x in d.values())


class SolutionLee2:
    def countCornerRectangles(self, grid):
        d = collections.Counter((i, j) for line in grid
                                for j in range(len(line)) if line[j]
                                for i in range(j) if line[i])
        return sum(x * (x - 1) / 2 for x in d.values())


"""
解题思路：
朴素解法是枚举左上角和右下角坐标，时间复杂度 O(m^2 * n^2)，会导致TLE

组合（Combination）时间复杂度 O(m^2 * n)

枚举起始行x，终止行y：

    遍历各列z，统计满足grid[x][z] == 1并且grid[y][z] == 1条件的列数，记为cnt

    根据组合公式，C(cnt, 2) = cnt * (cnt - 1) / 2，累加至答案。

"""

"""
这道题给了我们一个由0和1组成的二维数组，这里定义了一种边角矩形，其四个顶点均为1，让我们求这个二维数组中有多少个不同的边角矩形。
那么最简单直接的方法就是暴力破解啦，我们遍历所有的子矩形，并且检验其四个顶点是否为1即可。先确定左上顶点，
每个顶点都可以当作左上顶点，所以需要两个for循环，然后我们直接跳过非1的左上顶点，接下来就是要确定右上顶点和左下顶点了，
先用一个for循环确定左下顶点的位置，同理，如果左下顶点为0，直接跳过。再用一个for循环确定右上顶点的位置，
如果右上顶点位置也确定了，那么此时四个顶点中确定了三个，右下顶点的位置也就确定了，此时如果右上和右下顶点均为1，
则结果res自增1
"""
"""
我们来看一种优化了时间复杂度的方法，这种方法的原理是两行同时遍历，如果两行中相同列位置的值都为1，则计数器cnt自增1，
那么最后就相当于有了(cnt - 1)个相邻的格子，问题就转化为了求cnt-1个相邻的格子能组成多少个矩形，
就变成了初中数学问题了，共有cnt*(cnt-1)/2个
"""


