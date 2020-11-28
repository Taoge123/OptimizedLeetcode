
import heapq

class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A, -heapq.heappop(A))
        return sum(A)



class SolutionLee:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2


