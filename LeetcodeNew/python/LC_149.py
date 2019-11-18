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



