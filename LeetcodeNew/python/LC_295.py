"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

import heapq

class MedianFinder:

    def __init__(self):
        # maxHeap for small values and minHeap for big values
        self.small = []
        self.large = []


    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            replace = -heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, replace)
        else:
            replace = -heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, replace)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return self.large[0]


class MedianFinder2:
    def __init__(self):
        self.med, self.odd, self.heaps = 0, 0, [[], []]

    def addNum(self, x):
        big, small = self.heaps
        if self.odd:
            heapq.heappush(big, max(x, self.med))
            heapq.heappush(small, -min(x, self.med))
            self.med = (big[0] - small[0]) / 2.0
        else:
            if x > self.med:
                self.med = heapq.heappushpop(big, x)
            else:
                self.med = -heapq.heappushpop(small, -x)
        self.odd ^= 1

    def findMedian(self):
        return self.med


nums = [1,2,3,4,5]
a = MedianFinder2()
for i in nums:
    print(a.addNum(i))
    print(a.findMedian())
