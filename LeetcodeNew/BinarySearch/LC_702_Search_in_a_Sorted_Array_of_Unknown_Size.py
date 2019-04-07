
"""
Given an integer array sorted in ascending order,
\write a function to search target in nums.  If target exists, then return its index,
otherwise return -1. However, the array size is unknown to you.
You may only access the array using an ArrayReader interface,
where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000,
and if you access the array out of bounds, ArrayReader.get will return 2147483647.

Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
"""

class Solution1:
    def search(reader, target):
        hi = 1
        while reader.get(hi) < target:
            hi <<= 1
        lo = hi >> 1
        while lo <= hi:
            mid = lo + hi >> 1
            if reader.get(mid) < target:
                lo = mid + 1
            elif reader.get(mid) > target:
                hi = mid - 1
            else:
                return mid
        return -1


class Solution2:
    def search(self, reader, target):

        l = 1

        while reader.get(l - 1) < target:
            l *= 2

        if reader.get(l - 1) == target:
            return l - 1

        r = l - 1
        l = l // 2 - 1

        while l < r:
            mid = (l + r) // 2
            if reader.get(mid) > target:
                r = mid
            elif reader.get(mid) < target:
                l = mid + 1
            else:
                return mid

        return -1 if reader.get(l) != target else l


class Solution3:
    def search(self, reader, target):

        low, high = 0, 2147483647
        while low <= high:
            if reader.get(high) == 2147483647:
                high = high // 2
            elif reader.get(high) < target:
                low = high + 1
                high = low * 2
            else:
                mid = (low + high) // 2
                if reader.get(mid) == target:
                    return mid
                elif reader.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1






