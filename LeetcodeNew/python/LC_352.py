

"""
Given a data stream input of non-negative integers a1, a2, ..., an, ...,
summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]


Follow up:

What if there are lots of merges and the number of disjoint intervals
are small compared to the data stream's size?
"""

import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end



class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        heapq.heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        stack = []
        while self.intervals:
            idx, cur = heapq.heappop(self.intervals)
            if not stack:
                stack.append((idx, cur))
            else:
                _, prev = stack[-1]
                if prev.end + 1 >= cur.start:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((idx, cur))
        self.intervals = stack
        res = list(map(lambda x: x[1], stack))

        for i in res:
            print(i.start, i.end)

        return res





a = SummaryRanges()
print(a.addNum(1))
print(a.getIntervals())
print(a.addNum(3))
print(a.getIntervals())
print(a.addNum(7))
print(a.getIntervals())
print(a.addNum(2))
print(a.getIntervals())
print(a.addNum(6))
print(a.getIntervals())



