
"""
https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
A classic greedy case: interval scheduling problem.

The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

Therefore, we can sort interval by ending time and key track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.


Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
"""
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
