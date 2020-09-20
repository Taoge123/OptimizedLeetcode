
import heapq

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m* n
        while left < right:
            mid = (right - left) // 2 + left
            if not self.enough(mid, m, n, k):
                left = mid + 1
            else:
                right = mid
        return left

    def enough(self, mid, m, n, k):
        count = 0
        for i in range(1, m + 1):
            count += min(mid // i, n)
        return count >= k





class Solution1:
    def findKthNumber(self, m, n, k):
        heap = [(i, i) for i in range(1, m+1)]
        heapq.heapify(heap)

        for _ in range(k):
            val, root = heapq.heappop(heap)
            nxt = val + root
            if nxt <= root * n:
                heapq.heappush(heap, (nxt, root))

        return val

