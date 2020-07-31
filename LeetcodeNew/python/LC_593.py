
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