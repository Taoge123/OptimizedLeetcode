
"""
https://leetcode.com/problems/range-module/discuss/169353/Ultra-concise-Python-(only-6-lines-of-actual-code)-(also-236ms-beats-100)
https://leetcode.com/problems/range-module/discuss/793321/Python-SortedList
https://leetcode.com/problems/range-module/discuss/835119/Python-SortedDict

We make use of the python bisect_left and bisect_right functions. bisect_left returns an insertion index in a sorted array to the left of the search value. bisect_right returns an insertion index in a sorted array to the right of the search value. See the python documentation. To keep track of the start and end values of the ranges being tracked, we use a tracking array of integers. This array consists of a number of sorted pairs of start and end values. So, it always has an even number of elements.

addRange first gets the leftmost insertion index of the left value and the rightmost insertion index of the right value. Then, we check if either of these indexes are even. If the index is even, it means that it is currently outside the range of start and end indexes being tracked. In this case, we include this index to be updated in the tracking array. We then use python array slicing to overwrite the tracking array with the left and right values placed in the correct index. Complexity is O(n).

removeRange first gets the leftmost insertion index of the left value and the rightmost insertion index of the right value. Then, we check if either of these indexes are odd. If the index is odd, it means that it is currently inside the range of start and end indexes being tracked. In this case, we include this index to be updated in the tracking array. We then use python array slicing to overwrite the tracking array with the left and right values placed in the correct index. Complexity is O(n).

queryRange gets the rightmost insertion index of the left value and the leftmost insertion index of the right value. If both these indexes are equal and these indexes are odd, it means the range queried is inside the range of values being tracked. In this case, we return True. Else, we return False. Complexity is O(log n).

"""

import bisect

from sortedcontainers import SortedList, SortedDict


class RangeModule:

    def __init__(self):
        self.nums = SortedList()

    def addRange(self, left: int, right: int) -> None:
        l = self.nums.bisect_left(left)
        r = self.nums.bisect_right(right)

        for _ in range(r - l):
            self.nums.pop(l)
        if l % 2 == 0:
            self.nums.add(left)
        if r % 2 == 0:
            self.nums.add(right)

    def queryRange(self, left: int, right: int) -> bool:
        l = self.nums.bisect_right(left)
        r = self.nums.bisect_left(right)
        return l == r and l % 2 != 0

    def removeRange(self, left: int, right: int) -> None:
        l = self.nums.bisect_left(left)
        r = self.nums.bisect_right(right)
        for _ in range(r - l):
            self.nums.pop(l)
        if l % 2 != 0:
            self.nums.add(left)
        if r % 2 != 0:
            self.nums.add(right)




class RangeModuleDict:

    def __init__(self):
        self.data = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        l = self.data.bisect(left)
        r = self.data.bisect(right)
        if l != 0:
            l -= 1
            if self.data.peekitem(l)[1] < left:
                l += 1
        if l != r:
            left = min(left, self.data.peekitem(l)[0])
            right = max(right, self.data.peekitem(r - 1)[1])
            for _ in range(l, r):
                self.data.popitem(l)
        self.data[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        l = self.data.bisect_right(left)
        r = self.data.bisect_right(right)
        if l == 0 or self.data.peekitem(l - 1)[1] < right:
            return False
        return True

    def removeRange(self, left: int, right: int) -> None:
        l = self.data.bisect_right(left)
        r = self.data.bisect_right(right)
        if l != 0:
            l -= 1
            if self.data.peekitem(l)[1] < left:
                l += 1
        if l != r:
            minLeft = min(left, self.data.peekitem(l)[0])
            maxRight = max(right, self.data.peekitem(r - 1)[1])
            for _ in range(l, r):
                self.data.popitem(l)
            if minLeft < left:
                self.data[minLeft] = left
            if right < maxRight:
                self.data[right] = maxRight


class RangeModuleN2:

    def __init__(self):
        self.interval = []

    def addRange(self, left, right):
        start = bisect.bisect_left(self.interval, left)
        end = bisect.bisect_right(self.interval, right)

        subInterval = []
        if start % 2 == 0:
            subInterval.append(left)
        if end % 2 == 0:
            subInterval.append(right)

        self.interval[start:end] = subInterval

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.interval, left)
        end = bisect.bisect_right(self.interval, right)

        subInterval = []
        if start % 2 == 1:
            subInterval.append(left)
        if end % 2 == 1:
            subInterval.append(right)

        self.interval[start:end] = subInterval

    def queryRange(self, left, right):
        start = bisect.bisect_right(self.interval, left)
        end = bisect.bisect_left(self.interval, right)

        return start == end and start % 2 == 1

