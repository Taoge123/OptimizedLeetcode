"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k)
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

"""


class Solution:
    def numberOfBoomerangs(self, points) -> int:

        res = 0
        for p1 in points:
            table = {}
            for p2 in points:
                x = p1[0] - p2[0]
                y = p1[1] - p2[1]
                dist = x * x + y * y
                table[dist] = 1 + table.get(dist, 0)

            for val in table.values():
                res += val * (val - 1)

        return res


points = [[0,0],[1,0],[2,0]]
a = Solution()
print(a.numberOfBoomerangs(points))




