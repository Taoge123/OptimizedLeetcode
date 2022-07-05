
"""
https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling

1. 如果求的是maximum number of non-overlapping intervals，用sort by ending point的方法
2. 如果求的是minimum number of intervals to cover the whole range，用sort by starting point的方法

56 Merge Intervals <- very similar
435 Non-overlapping Intervals <- very similar
252 Meeting Rooms
253 Meeting Rooms II

A classic greedy case: interval scheduling problem.

The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals. 
(or minimal number to remove).
This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. 
If we choose another interval with end time y, then available time slot would be [y:]. 
Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

Therefore, we can sort interval by ending time and key track of current earliest end time.
Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.

-----------
   -----------
     -------------
                    ------
                            -----
                              --------

"""


class Solution:
    def eraseOverlapIntervals(self, intervals):
        end = float('-inf')
        intervals = sorted(intervals, key=lambda x: x[1])
        res = 0
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                res += 1
        return res



intervals = [[1,2],[2,3],[3,4],[1,3]]

a = Solution()
print(a.eraseOverlapIntervals(intervals))


"""

------|
  ----|--
 -----|---
      | ---------   
      

-------
  ------
    ------
            --------
            
"""


