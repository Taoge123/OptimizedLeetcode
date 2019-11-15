class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):


        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)

        res = [intervals[0]]

        for interval in intervals[1:]:
            last = res[-1]

            if interval.start <= last.end:
                last.end = max(interval.end, last.end)
            else:
                res.append(interval)
        return res

