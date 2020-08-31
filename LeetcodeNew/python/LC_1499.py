
"""
x is in increasing order
max(yi + yj - xi + xj)
-> xj + yj + max(-xi + yi) for |xi - xj| <= k

sliding window maximum -> deque O(N)

X X X X X j j‘

[5 3 1] 8

Because xi < xj, yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

So we only need to find out the maximum yi - xi.
To find out the maximum element in a sliding window,
we can use priority queue or stack.

"""

import collections
import heapq

class SolutionWisdom:
    def findMaxValueOfEquation(self, points, k: int) -> int:
        queue = collections.deque()
        res = -float('inf')
        for i, (x, y) in enumerate(points):
            # check xi and xj to make sure its not far away -> lazy deletion
            while queue and x - points[queue[0]][0] > k:
                queue.popleft()
            if queue:
                res = max(res, -points[queue[0]][0] + points[queue[0]][1] + x + y)
            while queue and -points[queue[-1]][0] + points[queue[-1]][1] < -x + y:
                queue.pop()
            queue.append(i)
        return res



class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:
        queue = collections.deque()
        res = -float('inf')
        for x, y in points:
            while queue and x - queue[0][1] > k:
                queue.popleft()
            if queue:
                res = max(res, queue[0][0] + y + x)
            while queue and queue[-1][0] <= y - x:
                queue.pop()
            queue.append([y - x, x])
        return res




class Solution2:
    def findMaxValueOfEquation(self, points, k):
        queue = []
        res = -float('inf')
        for x, y in points:
            while queue and queue[0][1] < x - k:
                heapq.heappop(queue)
            if queue:
                res = max(res, -queue[0][0] + y + x)
            heapq.heappush(queue, (x - y, x))
        return res
