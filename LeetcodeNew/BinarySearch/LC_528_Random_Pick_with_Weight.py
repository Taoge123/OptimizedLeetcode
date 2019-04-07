
"""
Given an array w of positive integers, where w[i] describes the weight of index i,
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
"""
import random
import itertools
import bisect

class Solution1:
    def __init__(self, w):
        self.w = list(itertools.accumulate(w))


    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))


class Solution2:

    def __init__(self, w):
        self.w = w
        self.n = len(w)
        self.s = sum(self.w)
        for i in range(1,self.n):
            w[i] += w[i-1]

    def pickIndex(self):

        seed = random.randint(1,self.s)
        l, r = 0, self.n-1
        while l < r:
            mid = (l+r)//2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l


class Solution3:
    def __init__(self, w):

        self.cumsum = [w[0]]
        for weight in w[1:]:
            self.cumsum.append(self.cumsum[-1] + weight)

    def pickIndex(self):

        rv = random.randint(1, self.cumsum[-1])
        return bisect.bisect_left(self.cumsum, rv)


"""
We should generate array of ranges for each weighted index like (sm, sm + weight] 
and then create random integer in range [1, totalSum] 
and binary search for the target index covering that integer.
"""

class Solution4:

    def __init__(self, w):
        self.ranges, sm = [], 0
        for weight in w:
            self.ranges.append([sm, sm + weight])
            sm += weight
        self.mn, self.mx = 1, sm

    def pickIndex(self):
        num, l, r = random.randint(self.mn, self.mx), 0, len(self.ranges) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.ranges[mid][1] < num:
                l = mid + 1
            elif num <= self.ranges[mid][0]:
                r = mid - 1
            else:
                return mid




