
"""
Median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle value.

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
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            replace = -heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, replace)
        else:
            replace = -heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, replace)

        print(self.small)
        print(self.large)

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])




# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(7)
obj.addNum(26)
obj.addNum(1)
obj.addNum(9)
obj.addNum(211)
obj.addNum(232)

print(obj.findMedian())








