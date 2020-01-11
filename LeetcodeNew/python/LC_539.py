

"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""


class Solution:
    def findMinDifference(self, timePoints) -> int:
        minutes = [self.convert(time) for time in timePoints]
        minutes = sorted(minutes)
        minutes.append(minutes[0] + 1440)

        return min(b - a for a, b in zip(minutes, minutes[1:]))

    def convert(self, time):
        return int(time[:2]) * 60 + int(time[3:])


timePoints = ["23:59","00:00"]
a = Solution()
print(a.findMinDifference(timePoints))



