

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


class SummaryRanges:
    def __init__(self):
        self.startWith = {}
        self.endWith = {}
        self.visited = set()

    def addNum(self, val: int) -> None:
        if val in self.visited:
            return

        self.visited.add(val)
        end = self.startWith.pop(val + 1, val)
        start = self.endWith.pop(val - 1, val)

        self.startWith[start] = end
        self.endWith[end] = start

    def getIntervals(self):
        return sorted(self.startWith.items())

"""
1 3 5 2 4

val = 4
end = 5
start = 1

start: [(1, 5)]
end:   [(5, 1)]

"""

class SummaryRanges1:
    def __init__(self):
        self.visited = set()
        self.start = dict()
        self.end = dict()

    def addNum(self, val: int) -> None:
        if val in self.visited:
            return

        self.visited.add(val)
        interval = [val, val]

        if val + 1 in self.start.keys():
            interval[1] = self.start[val + 1]
            self.start.pop(val + 1)

        if val - 1 in self.end.keys():
            interval[0] = self.end[val - 1]
            self.end.pop(val - 1)

        #start的value是end, end的value是start
        self.start[interval[0]] = interval[1]
        self.end[interval[1]] = interval[0]

    def getIntervals(self):
        return sorted(self.start.items())


"""
interval = [num, num]     --- [start1, end1]
start = [num + 1, end1] --- [end1, start1]
end = [num - 1, start1]     --- [start1, end1]

1, 3, 7, 2, 6
interval = [1, 3]
start = [1, 3] [3, 3] [7, 7] - [1, 3] [3, 3] [7, 7] 
end = [1, 1] [3, 1] [7, 7] - [3, 1] [7, 7]
visited = (1, 3, 7, 2)


"""


class SummaryRanges11:
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        low, high = 0, len(self.intervals)
        while low < high:
            mid = (low + high) // 2
            elem = self.intervals[mid]
            if elem[0] <= val <= elem[1]:
                return
            elif elem[0] > val:
                high = mid
            else:
                low = mid + 1

        # insert the interval
        pos = low
        self.intervals.insert(pos, [val, val])

        # merge with next interval
        if pos + 1 < len(self.intervals) and val == self.intervals[pos + 1][0] - 1:
            self.intervals[pos][1] = self.intervals[pos + 1][1]
            self.intervals[pos + 1:pos + 2] = []

        # merge with prev interval
        if pos - 1 >= 0 and val == self.intervals[pos - 1][1] + 1:
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            self.intervals[pos:pos + 1] = []
        print(self.intervals)

    def getIntervals(self):
        return self.intervals




class SummaryRanges2:
    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, val):
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])

    def getIntervals(self):
        stack = []

        while self.intervals:
            cur = heapq.heappop(self.intervals)
            if stack and cur[0] <= stack[-1][1] + 1:
                stack[-1][1] = max(stack[-1][1], cur[1])
            else:
                stack.append(cur)

        self.intervals = stack
        return self.intervals


class SummaryRanges3:
    def __init__(self):
        self.visited=set()

    def addNum(self, val: int) -> None:
        self.visited.add(val)

    def getIntervals(self):
        res = []
        for val in sorted(self.visited):
            if not res or val > res[-1][1] + 1:
                res.append([val,val])
            elif res and val == res[-1][1] + 1:
                res[-1][1] = val
        return res





a = SummaryRanges1()
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
