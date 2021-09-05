"""
https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/discuss/489882/O(n)-Solution-with-explanation

Explanation
total calculate the total sum of |A[i] - A[j]|.
res record the value the we can improve.

Assume the current pair is (a,b) = (A[i], A[i+1]).

If we reverse all element from A[0] to A[i],
we will improve abs(A[0] - b) - abs(a - b)

If we reverse all element from A[i+1] to A[n-1],
we will improve abs(A[n - 1] - a) - abs(a - b)

As we iterate the whole array,
We also record the maximum pair and the minimum pair.
We can break these two pair and reverse all element in the middle.
This will improve (max2 - min2) * 2


Complexity
Time O(N)
Space O(1)

"""


class Solution:
    def maxValueAfterReverse(self, nums):
        res, n = 0, len(nums)
        for i in range(1, n):
            res += abs(nums[i] - nums[i - 1])

        diff = 0
        for i in range(n):

            if i + 1 < n:
                diff = max(diff, abs(nums[i + 1] - nums[0]) - abs(nums[i + 1] - nums[i]))

            if i > 0:
                diff = max(diff, abs(nums[i - 1] - nums[n - 1]) - abs(nums[i - 1] - nums[i]))

        low, high = float("inf"), float("-inf")

        for i in range(n - 1):
            low = min(low, max(nums[i], nums[i + 1]))
            high = max(high, min(nums[i], nums[i + 1]))

            diff = max(diff, 2 * (high - low))

        return res + diff



class Solution2:
    def maxValueAfterReverse(self, nums):
        total, res = 0, 0
        mini, maxi = float('inf'), -float('inf')
        for a, b in zip(nums, nums[1:]):
            total += abs(a - b)
            res = max(res, abs(nums[0] - b) - abs(a - b))
            res = max(res, abs(nums[-1] - a) - abs(a - b))
            mini = min(mini, max(a, b))
            maxi = max(maxi, min(a, b))
        return total + max(res, (maxi - mini) * 2)



names = ('time', 'dsds', 'dcfef', 'vfv', 'rgb')
grades = (1, 2, 3, 4, 5)

res = []
for name, grade in zip(names, grades):
    res.append((name, grade))

print(res)

