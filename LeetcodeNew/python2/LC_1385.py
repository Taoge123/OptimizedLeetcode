"""
A number from arr1 adds to the distance value if the range(number - d, number + d + 1) is not in arr2. So for each number in arr1, we just need to check whether that range overlaps with arr2.

Convert arr2 to a set, to speed up searching for the range within it.
Convert arr1 to a bag (a dictionary that counts occurrences of each number). This way if arr1 = [1,1,1,3,4] we only need to check 1 once, and if it is valid then add 3 to res, as opposed to checking 1 three times.

If the intersection between arr2 and range(number - d, number + d + 1) is empty, then that number adds to the distance value. Repeat for all numbers in arr1 and you're done.



"""

import collections
import bisect

class Solution1:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        res = 0
        arr2.sort()

        for num in arr1:
            left = bisect.bisect_left(arr2, num - d)
            right = bisect.bisect_right(arr2, num + d)

            if left == right:
                res += 1

        return res



class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        res = 0
        count1 = collections.Counter(arr1)
        set2 = set(arr2)

        for num in count1:
            target = [i for i in range(num-d, num+d+1)]
            target = set(target)
            if not set2 & target:
                res += count1[num]
        return res




