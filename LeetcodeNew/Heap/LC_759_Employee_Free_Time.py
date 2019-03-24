"""
Similar to Leetcode 56
https://leetcode.com/problems/employee-free-time/discuss/170551/Simple-Python-9-liner-beats-97-(with-explanation)
https://leetcode.com/problems/merge-intervals/description/

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common,
positive-length free time for all employees, also in sorted order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals,
not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
"""
"""
Key points:

1. recognize that this is very similar to merging intervals 
(https://leetcode.com/problems/merge-intervals/description/)
2. it doesn't matter which employee an interval belongs to, so just flatten
3. can build result array while merging, don't have to do afterward (and don't need full merged arr)
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution1:
    def employeeFreeTime(self, schedule):
        sche = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, pre = [], sche[0]

        for i in sche[1:]:

            if i.start <= pre.end and i.end > pre.end:
                pre.end = i.end
            elif i.start > pre.end:
                res.append(Interval(pre.end, i.start))
                pre = i

        return res

class Solution2:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        free = []
        work = sorted([[i.start, i.end] for employee in schedule for i in employee])
        latest = work[0][0]
        for start, end in work:
            if start > latest:
                free.append(Interval(latest, start))
            latest = max(latest, end)
        return free


"""
Approach #1: Events (Line Sweep) [Accepted]

If some interval overlaps any interval (for any employee), 
then it won't be included in the answer. So we could reduce our problem to the following: 
given a set of intervals, find all places where there are no intervals.

To do this, we can use an "events" approach present in other interval problems. 
For each interval [s, e], we can think of this as two events: balance++ when time = s, 
and balance-- when time = e. We want to know the regions where balance == 0.

For each interval, create two events as described above, and sort the events. 
Now for each event occuring at time t, if the balance is 0, 
then the preceding segment [prev, t] did not have any intervals present, 
where prev is the previous value of t.
"""


class SolutionL1:
    def employeeFreeTime(self, avails):
        OPEN, CLOSE = 0, 1

        events = []
        for emp in avails:
            for iv in emp:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))

        events.sort()
        ans = []
        prev = None
        bal = 0
        for t, cmd in events:
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, t))

            bal += 1 if cmd is OPEN else -1
            prev = t

        return ans








