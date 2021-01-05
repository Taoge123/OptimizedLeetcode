
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



