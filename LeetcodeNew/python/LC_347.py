
"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums, k):

        table = {}
        heap = []
        for num in nums:
            table[num] = table.get(num, 0) + 1

        for i in table.keys():
            heappush(heap, (table[i], i))

        while len(heap) > k:
            heappop(heap)

        res = []
        while heap:
            res.append(heappop(heap)[1])

        return res





