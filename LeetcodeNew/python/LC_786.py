
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        n = len(A)
        heap = []
        for i in range(1, n):
            heapq.heappush(heap, (float(A[0]) / A[i], 0, i))

        for _ in range(K):
            node, nu, de = heapq.heappop(heap)
            if nu + 1 < de:
                heapq.heappush(heap, (float(A[nu + 1]) / A[de], nu + 1, de))
        return [A[nu], A[de]]

