"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

-------
    -------
      --------
             ------
                     -----------

i   i i      i       i
       j   j  j   j            j
"""

import heapq


class SolutionRika:
    def minMeetingRooms(self, intervals):

        meetings = []
        for i, j in intervals:
            meetings.append([i, 1])
            meetings.append([j, -1])

        meetings.sort()

        count = 0
        res = 0
        for time, status in meetings:
            count += status
            res = max(res, count)
        return res



class Solution:
    def minMeetingRooms(self, intervals) -> int:
        right = res = 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)

        for i in range(len(start)):
            if start[i] < end[right]:
                res += 1
            else:
                right += 1
        return res


"""
-------
    -------
      --------
             ------
                     -----------
"""

class Solution2:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)


