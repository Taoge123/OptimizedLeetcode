
"""
Create a pq - keep it only having the k-largest elements by popping off small elements.
With only k elements, the smallest item (self.pool[0]) will always be the kth largest.

If a new value is bigger than the smallest, it should be added into your heap.
If it's bigger than the smallest (that are already the kth largest), it will certainly be within the kth largest of the stream.
"""

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)


    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
