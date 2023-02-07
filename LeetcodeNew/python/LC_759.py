
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


"""
    
----- e
   ----
        --------
         -----
        
        
"""


class SolutionTony:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res = []
        end = intervals[0].end
        for interval in intervals[1:]:
            i, j = interval.start, interval.end
            if i > end:
                res.append(Interval(end, i))
            end = max(end, j)
        return res


# schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# a = SolutionTony()
# print(a.employeeFreeTime(schedule))


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



