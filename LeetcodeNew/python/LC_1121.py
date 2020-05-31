import collections

"""
Intuition
For example 2: A = [5,6,6,7,8]
we have two 6, so we have to split A into at least two subsequence.
We want K = 3 numbers in each subsequence, so we need at least K * 2 = 6 numbers.
But we have only A.length = 5 numbers.


Explanation
So the idea is that, find the maximum quantity of same numbers in nums.
As nums is sorted already, we can do this in one pass and O(1) space.
cur is the current length of same number until A[i].
If A[i - 1] < A[i], we reset cur = 1. Otherwise increment cur = cur + 1.

If n < K * groups, it's impossible to satisfy the condition, we return false.
Otherwise, we have enough numbers in hand and we can easily meet the requirement:


Prove
Provide a way to split here:

1. Find the number of groups as in the solution, assume it equals to M
2. Assign A[i] to groups[i % M].
3. Done.

Complexity
Time O(N) for one pass, and you can return false earlier.
Space O(1) for no extra space.
"""

class Solution:
    def canDivideIntoSubsequences(self, nums, K: int) -> bool:

        count = collections.Counter(nums)
        groups = max(count.values())
        return len(nums) >= K * groups


