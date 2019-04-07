
"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

class Solution1:
    def arrangeCoins(self, n):

        start = 1
        end = n
        while end >= start:
            mid = (start+end)//2
            total = mid*(mid+1)//2
            if total == n:
                return mid
            elif total<n:
                start = mid + 1
            else:
                end = mid - 1
        return end

class Solution2:
    def arrangeCoins(self, n):

        row = 0
        while (n >= 0):
            row += 1
            n -= row
        return row-1


class Solution3:
    def arrangeCoins(self, n):

        left = 0
        right = n

        while left <= right:

            mid = left + (right - left) // 2

            # sum of n natural numbers equation
            total = mid * (mid + 1) / 2

            if n >= total:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1

        return ans





