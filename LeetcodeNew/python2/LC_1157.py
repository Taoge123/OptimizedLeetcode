"""
https://leetcode.com/problems/online-majority-element-in-subarray/discuss/366995/Python3-Binary-Search-Without-Using-Probabilities

[1 ,2 ,3 ,4 ,4 ,4 ,5 ,6 ,6 ,6 ,6 ,7]
after sort
[6, 4, 1, 2, 3, 5, 7]

"""

import collections
import bisect


class MajorityChecker:
    def __init__(self, arr):
        self.table = collections.defaultdict(list)
        for i, num in enumerate(arr):
            self.table[num].append(i)
        self.nums = sorted(self.table.keys(), key = lambda n: len(self.table[n]), reverse=True)


    def query(self, left: int, right: int, threshold: int) -> int:
        for num in self.nums:
            if len(self.table[num]) < threshold:
                return -1
            # left and right are index, we search in index and check if the ranges are >= threshold.
            l = bisect.bisect_left(self.table[num], left)
            r = bisect.bisect_right(self.table[num], right)
            if r - l >= threshold:
                return num
        return -1



