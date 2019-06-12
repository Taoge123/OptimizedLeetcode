
"""
Given n points in the plane that are all pairwise distinct,
a "boomerang" is a tuple of points (i, j, k) such that the distance
between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500
and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

"""
for each point, create a hashmap and count all points with same distance. 
If for a point p, there are k points with distance d, 
number of boomerangs corresponding to that are k*(k-1). 
Keep adding these to get the final result.
"""
"""
题目大意：
给定平面上的n个两两不同的点，一个“回飞镖”是指一组点(i, j, k)满足i到j的距离=i到k的距离（考虑顺序）

计算回飞镖的个数。你可以假设n最多是500，并且点坐标范围在 [-10000, 10000] 之内。

解题思路：
枚举点i(x1, y1)，计算点i到各点j(x2, y2)的距离，并分类计数

利用排列组合知识，从每一类距离中挑选2个点的排列数 A(n, 2) = n * (n - 1)

将上述结果累加即为最终答案
"""
import collections

class Solution0:
    def numberOfBoomerangs(self, points):
 
        ans = 0
        for x1, y1 in points:
            dmap = collections.defaultdict(int)
            for x2, y2 in points:
                dmap[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1
            for d in dmap:
                ans += dmap[d] * (dmap[d] - 1)
        return ans


class Solution1:
    def numberOfBoomerangs(self, points):
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0] - q[0]
                s = p[1] - q[1]
                cmap[f * f + s * s] = 1 + cmap.get(f * f + s * s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] - 1)
        return res


class Solution2:
    def numberOfBoomrangs(self, points):
        nums = 0
        for x1, y1 in points:
            distance = collections.defaultdict(int)
            for x2, y2 in points:
                dx = abs(x2 - x1)
                dy = abs(y2 - y1)
                d = dx * dx + dy * dy
                distance[d] += 1

            nums += sum(n * (n - 1) for n in distance.values())
        return nums



"""
遍历所有的点，每个当前点对应一个dictionary，key: 与该点的距离，value: 与该点相距此距离的剩余点的个数。
Because the order matters, 所以最终取排列数。因为最终返回的是三元组，所以取排列组合数为2即可。
"""

class Solution3:
    def numberOfBoomerangs(self, points):
        res = 0
        for p0 in points:
            distmap = collections.defaultdict(int)
            for p1 in points:
                dist = (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2
                distmap[dist] += 1  # Number of points that are dist far away from current point p0
            for p in distmap:
                res += distmap[p] * (distmap[p] - 1)

        return res






