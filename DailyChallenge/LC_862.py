import collections

class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        queue = collections.deque([[0, 0]])
        res = float('inf')
        summ = 0
        for i, num in enumerate(A):
            summ += num

            while queue and summ - queue[0][1] >= K:
                res = min(res, i + 1 - queue.popleft()[0])

            while queue and summ <= queue[-1][1]:
                queue.pop()
            queue.append([i + 1, summ])
        return res if res < float('inf') else -1


