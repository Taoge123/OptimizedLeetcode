
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class SolutionTony:
    def employeeFreeTime(self, schedule):
        intervals = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res = []
        end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start > end:
                res.append(Interval(end, interval.start))
            end = max(end, interval.end)
        return res



class Solution:
    def employeeFreeTime(self, schedule):
        res = []
        work = sorted([[time.start, time.end] for employee in schedule for time in employee])
        latest = work[0][0]
        for start, end in work:
            if start > latest:
                res.append(Interval(latest, start))
            latest = max(latest, end)
        return res



