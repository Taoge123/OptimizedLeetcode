"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

-----
  -----
            -------
               --------
                              -----
                                -----
option 1:

 ---------
      ----------
    -------

option 2:
   ------
      ------
 -------------
"""


class Solution2:
    def insert(self, intervals, newInterval):

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res



class Solution:
    def insert(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[1]
        left, right = [], []

        for interval in intervals:
            if interval[1] < s:
                # current interval is on the left-hand side of newInterval
                left += [interval]

            elif interval[0] > e:
                # current interval is on the right-hand side of newInterval
                right += [interval]

            else:
                # current interval has overlap with newInterval
                # merge and update boundary
                s = min(s, interval[0])
                e = max(e, interval[1])

        return left + [[s, e]] + right


