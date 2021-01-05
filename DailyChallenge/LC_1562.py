

class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        arr.insert(0, 0)
        res = -1

        day = {}
        for i in range(1, n + 1):
            day[arr[i]] = i

        queue = collections.deque()

        for i in range(1, n + 1):
            while queue and day[queue[-1]] < day[i]:
                queue.pop()
            while queue and i - queue[0] >= m:
                queue.popleft()
            queue.append(i)
            if i < m:
                continue
            maxi = day[queue[0]]

            left, right = float('inf'), float('inf')
            if i - m >= 1:
                left = day[i - m]
            if i + 1 <= n:
                right = day[i + 1]
            if maxi < left and maxi < right:
                res = max(res, min(left, right) - 1)
        return res
