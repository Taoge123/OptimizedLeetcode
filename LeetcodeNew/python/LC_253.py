"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


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




