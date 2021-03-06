import heapq

class Solution:
    def minimumDeviation(self, nums) -> int:

        minHeap = []
        maxHeap = []
        visited = set()

        for num in nums:
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, -num)

        visited.add(tuple([minHeap[0], maxHeap[0]]))

        res = -maxHeap[0] - minHeap[0]

        while (minHeap[0] % 2 == 1 or maxHeap[0] % 2 == 0) and tuple([minHeap[0], maxHeap[0]]) not in visited:
            print(minHeap)
            print(maxHeap)
            if minHeap[0] % 2 == 1:
                node = heapq.heappop(minHeap)
                maxHeap.remove(-node)
                heapq.heappush(minHeap, node * 2)
                heapq.heappush(maxHeap, -node * 2)

            elif maxHeap[0] % 2 == 0:
                node = heapq.heappop(maxHeap)
                minHeap.remove(-node)
                heapq.heappush(minHeap, -node // 2)
                heapq.heappush(maxHeap, node // 2)

            visited.add(tuple(minHeap + maxHeap))
            print(tuple([minHeap[0], maxHeap[0]]))
            res = min(res, -maxHeap[0] - minHeap[0])

        return res



nums = [1,2,3,4]
a = Solution()
print(a.minimumDeviation(nums))


