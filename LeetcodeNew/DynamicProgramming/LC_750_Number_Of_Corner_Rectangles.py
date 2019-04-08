
"""
http://www.cnblogs.com/grandyang/p/8433813.html

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
import itertools


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

"""
容易想到的是n*(n-1)/2这个计算公式，先固定2行，求每列与这2行相交是不是都是1 ，计算这样的列数
枚举起始行x，终止行y：

    遍历各列z，统计满足grid[x][z] == 1并且grid[y][z] == 1条件的列数，记为cnt

    根据组合公式，C(cnt, 2) = cnt * (cnt - 1) / 2，累加至答案。

public int countCornerRectangles(int[][] grid) {
    int m = grid.length, n = grid[0].length;
    int ans = 0;
    for (int x = 0; x < m; x++) {
        for (int y = x + 1; y < m; y++) {
            int cnt = 0;
            for (int z = 0; z < n; z++) {
                if (grid[x][z] == 1 && grid[y][z] == 1) {
                    cnt++;
                }
            }
            ans += cnt * (cnt - 1) / 2;
        }
    }
    return ans;
}
"""

"""
Python还需要改变遍历方式做一点prune
counts[i][j] is used to keep track of the number of rows, found so far, in which column i and column j are 1.
Every time you find a new row that has i and j set to 1, 
counts will tell you how many rectangles you can form with this new row.
"""

class Solution3:
    def countCornerRectangles(self, grid):
        res = 0
        counts = [[0] * len(grid[rows]) for rows in range(len(grid))]
        for row in range(0, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[row][j] == 1:
                    for i in range(0, j):
                        if grid[row][i] == 1:
                            res += counts[i][j]
                            counts[i][j] += 1
        return int(res)


"""
Approach #1: Count Corners [Accepted]
Intuition

We ask the question: for each additional row, how many more rectangles are added?

For each pair of 1s in the new row (say at new_row[i] and new_row[j]), 
we could create more rectangles where that pair forms the base. 
The number of new rectangles is the number of times some previous row had row[i] = row[j] = 1.

Algorithm

Let's maintain a count count[i, j], the number of times we saw row[i] = row[j] = 1. 
When we process a new row, for every pair new_row[i] = new_row[j] = 1, 
we add count[i, j] to the answer, then we increment count[i, j].
"""

class Solution4:
    def countCornerRectangles(self, grid):
        count = collections.Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in range(c1+1, len(row)):
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
        return ans


"""
Approach #2: Heavy and Light Rows [Accepted]
Intuition and Algorithm

Can we improve on the ideas in Approach #1? When a row is filled with XX 1s, we do O(X^2)O(X 
2) work to enumerate every pair of 1s. This is okay when XX is small, but expensive when XX is big.
Say the entire top row is filled with 1s. When looking at the next row with say, f 1s that match the top row, 
the number of rectangles created is just the number of pairs of 1s, which is f * (f-1) / 2. 
We could find each f quickly using a Set and a simple linear scan of each row.

Let's call a row to be heavy if it has more than \sqrt N 
N points. The above algorithm changes the complexity of counting a heavy row from O(C^2)O(C 
2) to O(N)O(N), and there are at most \sqrt N 
N heavy rows.
"""

class Solution5:
    def countCornerRectangles(self, grid):
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)

        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1

        return ans



