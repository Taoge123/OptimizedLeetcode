
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

class Solution:
    def findLHS(self, nums) -> int:

        count = collections.Counter(nums)
        res = 0
        for num in count.keys():
            if num + 1 in count.keys():
                res = max(res, count[num] + count[num + 1])

        return res




