"""
Identical to 1024. Video Stitching


sort by end
435.Non-overlapping-Intervals (M+)
452.Minimum-Number-of-Arrows-to-Burst-Balloons (H-)
757.Set-Intersection-Size-At-Least-Two (H)

sort by start
1024.Video-Stitching (M+)
1288.Remove-Covered-Intervals (M+)
1326.Minimum-Number-of-Taps-to-Open-to-Water-a-Garden (M+)


sort by start -> the minimum number of intervals to cover the whole range
sort by end -> the maximum number of non-overlapping intervals

"""


class Solution:
    def minTaps(self, n: int, ranges) -> int:

        intervals = []
        for i in range(n + 1):
            intervals.append([i - ranges[i], i + ranges[i]])

        intervals.sort(key=lambda x: (x[0], x[1]))
        if intervals[0][0] > 0:
            return -1

        # pretend we virtually start from 0
        end = 0
        i = 0
        count = 0
        while i < len(intervals):
            count += 1
            nxt = end
            while i < len(intervals) and intervals[i][0] <= end:
                nxt = max(nxt, intervals[i][1])
                i += 1

            # if we already reached n
            if nxt >= n:
                return count
            # if next end wasn't being updated, that means we will not be able to reach n
            elif nxt == end:
                return -1

            end = nxt

        return -1







