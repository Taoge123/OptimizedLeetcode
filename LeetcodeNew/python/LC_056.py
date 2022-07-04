"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


-----------
   -----------
     -------------
                    ------
                            -----
                              --------
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SolutionTony:
    def merge(self, intervals):

        res = []
        intervals.sort()
        res.append(intervals[0])
        for i, j in intervals[1:]:
            # if last meeting ends, then we start a new meeting
            if res[-1][1] < i:
                res.append([i, j])
            # if last meeting is going on, then we merge it by pick the latest finished time
            else:
                res[-1][1] = max(res[-1][1], j)
        return res



class Solution:
    def merge(self, intervals):

        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda x: x.start)

        res = []
        res.append(intervals[0])

        for interval in intervals[1:]:

            #Basically if the new interval is less than last end, then we merge, else its a new interval
            if interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)

            else:
                res.append(interval)

        return res

