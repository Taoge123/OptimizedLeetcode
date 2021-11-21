"""

0    |   |   |    10

mid = 3


x.  x.        x.                x            x



1 2 7 9 15  -> 3

dist - 3


left = 0
right = stations[-1] - stations[0]

mid - big   -  less
      small -  more

if count(mid) >= k:
    left = mid + 1
else:
    right = mid
return left

x                x
1                100

2. count(mid)


0 | | | 10
ceil()



3. equal

"""

import math

class Solution:
    def minmaxGasDist(self, stations, k: int) -> float:
        left, right = 1e-9, stations[-1] - stations[0]
        while right - left > 1e-6:
            mid = (right - left) / 2 + left
            if self.count(stations, mid) > k:
                left = mid
            else:
                right = mid

        return left

    def count(self, nums, mid):

        count = 0

        for a, b in zip(nums, nums[1:]):
            count += math.ceil((b - a) / mid) - 1
        return count


class Solution2:
    def minmaxGasDist(self, stations, K):
        lo, hi = 0, max(stations)
        while hi - lo > 1e-6:
            mid = (lo + hi) / 2
            if self.possible(stations, mid, K):
                hi = mid
            else:
                lo = mid
        return lo

    def possible(self, nums, mid, K):
        return sum(int((nums[i+1] - nums[i]) / mid) for i in range(len(nums)-1)) <= K




