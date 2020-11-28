"""
H-Index : the largest x, you have at least x publications that have x citatioins
                                  exact

a: there are a numbers which value >= a
b: there are b numbers which value >= b
a < b


"""

import collections

class Solution:
    def specialArray(self, nums) -> int:
        left = 1
        right = len(nums)

        while left < right:
            mid = right - (right - left) // 2
            count = 0
            for num in nums:
                if num >= mid:
                    count += 1
            if count >= mid:
                left = mid
            else:
                right = mid - 1

        count = 0
        for num in nums:
            if num >= left:
                count += 1
        if count == left:
            return left
        else:
            return -1


"""
H-Index : the largest x, you have at least x publications that have x citatioins
                                  exact

a: there are a numbers which value >= a
b: there are b numbers which value >= b
a < b


"""

class SolutionForOneSolutionOnly:
    def specialArray(self, nums) -> int:
        left = 1
        right = len(nums)

        while left <= right:
            mid = right - (right - left) // 2
            count = 0
            for num in nums:
                if num >= mid:
                    count += 1

            if count == mid:
                return mid

            if count >= mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1


"""

1 2 3 2       3
1 2 3 4 .... 100

"""


class Solution3:
    def specialArray(self, nums) -> int:
        n = len(nums)
        freq = collections.Counter()
        for num in nums:
            freq[min(num, n)] += 1

        count = 0
        for x in range(n, 0, -1):
            count += freq[x]
            if count == x:
                return x

        return -1

