"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019.
Please reset to default code definition to get new method signature.
"""


"""
字典+最大公约数
这个题是个Hard题，而且通过率非常低。其实做法一点都不难。

我们想想如何判断三个点是否在一个直线上？初中知识告诉我们，两点确定一个直线。如果已经确定一个点，
那么只需要计算另外两个点和当前点的斜率是否相等即可。当然如果另外两个点当中如果有和当前点重合的就不能直接求斜率了，
这种情况重合的两个点无论怎么样都会和第三个点共线的。

在计算斜率的时候需要用到技巧，因为如果两个点的横坐标重合了，那么斜率是无穷大；如果斜率是浮点数，
还会涉及到浮点数精度问题。所以使用了最大公约数这个技巧。我们不要直接计算斜率，而是相当于最简分式的形式，
使用pair或者Python中的tuple，保存已经化为最简分数的两个数值，然后使用字典来统计这个pair出现了多少次。

最后的结果是共线并且不重合的点的最大个数+重叠的点的个数。

时间复杂度是O(N^2)，空间复杂度是O(N)。
"""
import collections

class Solution:
    def maxPoints(self, points):
        n = len(points)
        res = 0
        for i in range(n):
            lines = collections.defaultdict(int)
            duplicates = 1
            for j in range(i + 1, n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicates += 1
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                delta = self.gcd(dx, dy)
                lines[(dx // delta, dy // delta)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicates)
        return res

    def gcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.gcd(y, x % y)





points = [[0,10],[0,11],[0,50]]
a = Solution()
print(a.maxPoints(points))

