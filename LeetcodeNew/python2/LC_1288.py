
"""
https://leetcode.com/problems/remove-covered-intervals/discuss/451277/JavaC%2B%2BPython-Sort-Solution


Intuition
Imagine that, after removing all covered intervals,
all intervals must have different bounds,
After sorting, their left and right bound are increasing at the same time.


Test Case
Here are some useful small test cases for debugging.
[[1,2],[1,3]]
[[1,3],[1,8],[5,8]]
[[1,6],[4,6],[4,8]]


Solution 1, sort
Sort the array, and note the previous left and right bound.
For evert interval v,
if v[0] > left && v[1] > right,
It's a new uncovered interval,
so we increment ++res.

Complexity: time O(NlogN), space O(1

if start equal, then we only care about the end

------
----------

"""

"""

---------------
  -----------
     -------------     
        ----            
                       -------


-------------              ok
  ---------                no
    -----                  no
      -------------        ok
       --                  no   
        ---                no
         ------            no

1. ----                ok
2. ---------           no

we need to sorted by decreasing order -> we need to include 2 and not include 1 since 1 is covered by 2



"""


class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 0

        prev_end = 0
        for start, end in intervals:

            if end > prev_end:
                res += 1
                prev_end = end

        return res





