
import heapq

class Solution:
    def minimumDeviation(self, nums) -> int:

        heap = []
        mini = float('inf')
        for num in nums:
            if num % 2 == 0:
                heap.append(-num)
                mini = min(mini, num)
            else:
                heap.append(-num * 2)
                mini = min(mini, num * 2)

        heapq.heapify(heap)
        res = float('inf')

        while heap:
            node = -heapq.heappop(heap)
            res = min(res, node - mini)
            if node % 2 == 0:
                mini = min(mini, node // 2)
                heapq.heappush(heap, -node // 2)
            else:
                # if the max is odd, break and return
                break
        return res


