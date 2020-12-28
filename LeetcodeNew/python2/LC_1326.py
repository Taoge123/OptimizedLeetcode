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

1326.Minimum-Number-of-Taps-to-Open-to-Water-a-Garden
此题的本质就是寻找数目最少的、互相重叠区间，使得最终能够覆盖[0,n]。这和1024.Video-Stitching非常类似。

我们将所有的区间按照左端点排列，如果左端点并列，那么优先选择范围大的区间。假设我们当前处理区间i，记作[a,b]，那么我们会查看i后面的、与i有交叠的区间，如果有多个，我们一定会从里面挑选右端点最远的那一个（记作区间j），因为j既能与i重叠、又能覆盖最远的地方，可以减少最终所选区间的数目。然后我们再考察区间j，重复之前的操作。

注意无解的情况有三种：1. 最右端的位置还没有推进到n，但是区间i之后已经没有任何其他区间能与之重叠；2. 如果考察完所有的区间，最右端的位置仍然无法推进到n，3. 第一个区间的左端点在0后面。

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







