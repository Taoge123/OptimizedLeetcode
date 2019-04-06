
"""
Given a set of intervals, for each of the interval i,
check if there exists an interval j whose start point is bigger than
or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index,
which means that the interval j has the minimum start point to build the "right" relationship
for interval i. If the interval j doesn't exist, store -1 for the interval i.
Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
"""

"""
solution from contest with minimal cleanup. 
For each end point search for the first start point that is equal 
or higher in a previously constructed ordered list of start points. 
If there is one then return its index. If not return -1:"""

import bisect

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution1:
    def findRightInterval(self, intervals):
        l = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e.end,))
            res.append(l[r][1] if r < len(l) else -1)
        return res

"""
Like other solutions :

1. sort Sort By interval.start runtime cost = O(n log(n)) plus memory usage
2. binary search for each interval INT in intervals : binary search INT.end 
   among the intervals startng after INT.start , O(n log(n))
binary search details as such
for a given intervals[i]

all intervals that start after intervals[i].start

intervals[i+1]  intervals[i+2]   intervals[i+3] intervals[i+4]  ... intervals[j]
who is the first one to start after intervals[i].end? (if there is any)

intervals[i+1]  intervals[i+2]   intervals[i+3] intervals[i+4]  ... intervals[j]
False                    False            True          True          True
"""


class Solution2:
    def findRightInterval(self, intervals):
        r = [-1] * len(intervals)
        intervals = [(intervals[i], i) for i in range(len(intervals))]
        intervals.sort(key=lambda x: x[0].start)

        for i in range(len(intervals)):
            u = intervals[i][0]
            lo, hi = i + 1, len(intervals) - 1
            while (lo < hi):
                med = (lo + hi) >> 1
                if intervals[med][0].start >= u.end:
                    hi = med
                else:
                    lo = med + 1
            r[intervals[i][1]] = intervals[lo][1] if lo < len(intervals) and intervals[lo][0].start >= u.end else -1
        return r


"""
这道题给了我们一堆区间，让我们找每个区间的最近右区间，要保证右区间的start要大于等于当前区间的end，
由于区间的顺序不能变，所以我们不能给区间排序，我们需要建立区间的start和该区间位置之间的映射，
由于题目中限定了每个区间的start都不同，所以不用担心一对多的情况出现。
然后我们把所有的区间的start都放到一个数组中，并对这个数组进行降序排序，那么start值大的就在数组前面。
然后我们遍历区间集合，对于每个区间，我们在数组中找第一个小于当前区间的end值的位置，
如果数组中第一个数就小于当前区间的end，那么说明该区间不存在右区间，结果res中加入-1；
如果找到了第一个小于当前区间end的位置，那么往前推一个就是第一个大于等于当前区间end的start，
我们在哈希表中找到该区间的坐标加入结果res中即可
"""

"""
解题方法
这个题主要是要使用二叉搜索，我发现我对这个理解的不够深入。

做法还是很容易理解的，因为可以使用一个字典保存每个区间的索引，因为每个区间的起点都是不同的，
所以可以使用这个开始点当做区间的标记。

对起始点进行排序之后（为什么要排序？因为我们要使用二分查找），遍历每个区间，
找出比这个区间的结尾大的第一个区间的起点值，然后根据这个起点值再找到这个区间的索引。

这也就是lowwer_found和higher_fount。我要补一补这方面的内容了。
"""

class Solution:
    def findRightInterval(self, intervals):

        n = len(intervals)
        start_map = {interval.start : i for i, interval in enumerate(intervals)}
        start_list = [interval.start for interval in intervals]
        res = []
        start_list.sort()
        for interval in intervals:
            pos = self.higher_find(start_list, interval.end)
            res.append(start_map[start_list[pos]] if pos != -1 else -1)
        return res

    def higher_find(self, array, v):
        lo, hi = 0, len(array) - 1
        first = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if array[mid] >= v:
                hi = mid - 1
                first = mid
            else:
                lo = mid + 1
        return first


