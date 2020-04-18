"""
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct.
"""
"""
Approach #4: Binary Search [Accepted]
Intuition

Let's ask possible(D): with K (or less) gas stations, can we make every adjacent distance between gas stations at most D? 
This function is monotone, so we can apply a binary search to find:
"""


class Solution:
    def minmaxGasDist(self, nums, K):
        left, right = 1e-6, nums[-1] - nums[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0

            for a, b in zip(nums, nums[1:]):
                count += int((b - a) / mid)

            if count > K:
                left = mid
            else:
                right = mid
        return right




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
        return sum(int((nums[i +1] - nums[i]) / mid) for i in range(len(nums) - 1)) <= K




