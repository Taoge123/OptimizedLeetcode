
"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



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


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:

        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])  # sort on start time
        currEnd = intervals[0][1]
        res = 0
        for x in intervals[1:]:
            if x[0] < currEnd:  # find overlapping interval
                res += 1
                currEnd = min(currEnd, x[1])  # erase the one with larger end time
            else:
                currEnd = x[1]   # update end time
        return res


intervals = [[1,2],[2,3],[3,4],[1,3]]

a = Solution()
print(a.eraseOverlapIntervals(intervals))
