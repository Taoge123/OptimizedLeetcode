import heapq

class Solution:
    def maximumMinimumPath(self, A) -> int:
        m, n = len(A), len(A[0])
        heap = [[-A[0][0], 0, 0]]
        res = float('inf')
        visited = set()

        while True:
            score, i, j = heapq.heappop(heap)
            res = min(res, -score)
            if (i, j) == (m - 1, n - 1):
                return res

            for node in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x = node[0] + i
                y = node[1] + j
                if x >= 0 and y >= 0 and x < m and y < n and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(heap, [-A[x][y], x, y])
