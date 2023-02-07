"""
253. Meeting Rooms II
2406. Divide Intervals Into Minimum Number of Groups
2402. Meeting Rooms III
731. My Calendar II
732. My Calendar III
1094. Car Pooling
1109. Corporate Flight Bookings
218. The Skyline Problem

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

class SolutionTony:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        # stores the end time of intervals
        heap = []
        for i, j in intervals:
            # if current time is > the previous smallest end time, then this meeting can take over an ended metting, no additional meeting need
            if heap and i >= heap[0]:
                # heapq.heapreplace(heap, i[1])
                heapq.heappop(heap)
                heapq.heappush(heap, j)
            else:
                # store the end time
                heapq.heappush(heap, j)
        return len(heap)



class SolutionRika:
    def minMeetingRooms(self, intervals):

        meetings = []
        for i, j in intervals:
            meetings.append([i, 1])
            meetings.append([j, -1])

        # if start time == end time, -1 goes first
        meetings = sorted(meetings,key=lambda x : (x[0], x[1]))

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





