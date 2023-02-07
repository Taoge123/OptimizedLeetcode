
"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].


Note: The length of the input array will not exceed 20,000.
"""

import collections
import functools

class Solution:
    def findLHS(self, nums) -> int:
        count = collections.Counter(nums)
        res = 0
        for num in count.keys():
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])

        return res


class SolutionToBeFixed:
    def findLHS(self, nums) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, mini, maxi):
            if i >= n:
                return 0
            pick = 0
            if nums[i] >= mini and nums[i] <= maxi and maxi - mini <= 1:
                pick = dfs(i + 1, mini, maxi) + 1
            mini = min(nums[i], mini)
            maxi = max(maxi, nums[i])
            no_pick = dfs(i + 1, mini, maxi)
            return max(pick, no_pick)

        return dfs(0, 0, 0)



nums = [1,2,3,4]
a = Solution2()
print(a.findLHS(nums))

