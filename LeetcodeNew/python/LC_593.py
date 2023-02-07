
"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True


Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.

"""

import itertools

"""
[0,0]
[1,1]
[1,0]
[0,1]

"""


class SolutionTony:
    def validSquare(self, p1, p2, p3, p4) -> bool:

        def dist(p1, p2):
            i, j = p1
            x, y = p2
            return (x - i) ** 2 + (y - j) ** 2

        distances = set()
        for i, a1 in enumerate([p1, p2, p3, p4]):
            for j, b1 in enumerate([p1, p2, p3, p4]):
                if i == j:
                    continue
                # if points are repeated, unable to form a square
                if a1 == b1:
                    return False
                distances.add(dist(a1, b1))
        return len(distances) == 2


class SolutionTony:
    def validSquare(self, p1, p2, p3, p4):
        def dist(p1, p2):
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

        test = set()
        s1, s2, s3, s4 = tuple(p1), tuple(p2), tuple(p3), tuple(p4)
        test.add(s1)
        test.add(s2)
        test.add(s3)
        test.add(s4)
        if len(test) != 4:
            return False
        d1 = dist(p1, p2)
        d2 = dist(p1, p3)
        d3 = dist(p1, p4)
        d4 = dist(p2, p3)
        d5 = dist(p2, p4)
        d6 = dist(p3, p4)
        # print(d1, d2, d3, d4, d5, d6)
        res = set()
        res.add(d1)
        res.add(d2)
        res.add(d3)
        res.add(d4)
        res.add(d5)
        res.add(d6)

        # print(res)
        return len(res) == 2


class SolutionRika:
    def validSquare(self, p1, p2, p3, p4):
        # 给4个点 看能否组成正方形 --> 算出每两个点之间的距离，最后只有两种可能，边长和斜边 + 要确保4个点是不重复的
        points = set()
        seen = set()

        total = [p1] + [p2] + [p3] + [p4]

        for i, (a, b) in enumerate(total):
            points.add((a, b))
            for j, (x, y) in enumerate(total):
                if i == j:
                    continue
                seen.add(abs(a - x) ** 2 + abs(b - y) ** 2)

        return len(seen) == 2 and len(points) == 4



class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        visited = set()

        for a, b in itertools.combinations((p1, p2, p3, p4), 2):
            visited.add(self.distance(a, b))

        return 0 not in visited and len(visited) == 2

    def distance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


class Solution2:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        edges = set()
        for p1, p2 in itertools.combinations([p1, p2, p3, p4], 2):
            print(self.dist(p1, p2))
            edges.add(self.dist(p1, p2))

        return len(edges) == 2

    def dist(self, p1, p2):
        return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2



p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
a = Solution2()
print(a.validSquare(p1, p2, p3, p4))