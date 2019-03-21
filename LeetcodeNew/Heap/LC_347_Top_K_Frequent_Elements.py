
"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import collections
import heapq

class Solution1:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

"""
Klog(N) - Create a frequency map and then add every tuple (frequency, item) to a max heap. Then extract the top k elements.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = [(-1*v1, k1) for k1,v1 in collections.Counter(nums).items()]
        heapq.heapify(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


"""
Heap: Nlog(k)

- Create a frequency map.
- Add k tuples (frequency, item) to min-heap.
- Iterate from k+1st tuple to Nth tuple. If the tuple frequency is more than top of heap, pop from heap and add the tuple.
- Finally the heap will have k largest frequency numbers
"""


class Solution2:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter, result = collections.Counter(nums), []
        inverse = collections.defaultdict(list)

        for key, val in counter.items():
            inverse[val].append(key)

        for x in range(len(nums), 0, -1):
            if x in inverse:
                result.extend(inverse[x])
                if len(result) >= k:
                    break
        return result[:k]


class SolutionHeap:
    def topKFrequent(self, nums, k):
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        heap = []
        for key in dic.keys():
            heapq.heappush(heap, (dic[key], key))

        while len(heap) > k:  # pop out lease frequent elements
            heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

nums = [1,1,1,2,2,3]
k = 2

a = Solution()
print(a.topKFrequent(nums, K))



