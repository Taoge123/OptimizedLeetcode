
# O(nlgn) time, the same as Merge Intervals
# https://leetcode.com/problems/merge-intervals/
def insert1(self, intervals, newInterval):
    intervals.append(newInterval)
    res = []
    for i in sorted(intervals, key=lambda x :x.start):
        if res and res[-1].end >= i.start:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)
    return res

# O(n) time, not in-place, make use of the
# property that the intervals were initially sorted
# according to their start times
def insert(self, intervals, newInterval):
    res, n = [], newInterval
    for index, i in enumerate(intervals):
        if i.end < n.start:
            res.append(i)
        elif n.end < i.start:
            res.append(n)
            return res +intervals[index:]  # can return earlier
        else:  # overlap case
            n.start = min(n.start, i.start)
            n.end = max(n.end, i.end)
    res.append(n)
    return res
