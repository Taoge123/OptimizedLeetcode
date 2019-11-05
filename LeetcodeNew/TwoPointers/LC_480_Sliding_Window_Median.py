import heapq
import collections

class Solution:
    def medianSlidingWindow(self, nums, k):


        medians = []
        hashes = collections.defaultdict(int)
        bheap, theap = [], []

        i = 0

        while(i > 0):
            heapq.heappush(theap, -heapq.heappop(bheap))

            while bheap and hashes[bheap[0]]:
                hashes[heapq.heappop(bheap)]-=1
            while theap and hashes[theap[0]]:
                hashes[-heapq.heappop(theap)]-=1

        return medians












