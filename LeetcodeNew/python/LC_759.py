
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


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



