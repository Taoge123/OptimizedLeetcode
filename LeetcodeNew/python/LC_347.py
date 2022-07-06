
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


class SolutionRika:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 返回前k个frequency的数字 --> 用hashmap先存frequency，然后 再 存对应的值

        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1

        values = []
        arr = []
        for val in freq.keys():
            values.append(val)
            arr.append(freq[val])
        # print(values, arr)

        return self.quickSelect(arr, values, 0, len(arr) - 1, k)

    def quickSelect(self, arr, values, left, right, k):
        pivot = self.partition(arr, values, left, right)
        if pivot == k - 1:
            return values[:pivot + 1]
        elif pivot < k - 1:
            return self.quickSelect(arr, values, pivot + 1, right, k)
        else:
            return self.quickSelect(arr, values, left, pivot - 1, k)

    def partition(self, arr, values, left, right):
        if len(arr) == 0:
            return 0
        pivot = random.randint(left, right)
        arr[pivot], arr[right] = arr[right], arr[pivot]
        values[pivot], values[right] = values[right], values[pivot]

        slow = left
        for fast in range(left, right):
            if arr[fast] > arr[right]:
                arr[fast], arr[slow] = arr[slow], arr[fast]
                values[fast], values[slow] = values[slow], values[fast]
                slow += 1

        arr[slow], arr[right] = arr[right], arr[slow]
        values[slow], values[right] = values[right], values[slow]

        return slow
