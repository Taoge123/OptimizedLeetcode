"""
We can simplify the problem:

subarry is continuous, so we can transfer the problem to: For each index i n nums , what is the max length of subarray (ending with index i) With positive product. Then we can iterate every answer for all indexes to get the result for original question.
We know that: positive_number * positive_number is positive, positive_number * negative_number is negative, negative_number * negative_number is positive.
Let's define:
dp[i][0] : max length of subarray ending with index i With positive product
dp[i][1] : max length of subarray ending with index i With negative product

In order to get the answer for current index, we need dp[i - 1][0] and dp[i - 1][1] to form a new subarray.

Implementation:

define a 2D array with length n

Base case would be: when index is 0, only one number can be used

Loop through the array, for the new number we have:

if current number is positive, we know we can definitely form a positive subarry, the length is at least 1:
[previous positive subarray] + [current number positive]
if current number is positive, we know we can form a negative subarray if for previous index, negative subarray exists. Otherwise we can't form a negetive subarray ending with current number
[previous negative subarray] + [current number positive]
if current number is negative, we know we can definitely form a negative subarry, the length is at least 1:
[previous positive subarray] + [current number negative]
if current number is negative, we know we can form a positive subarray if for previous index, negative subarray exists. Otherwise we can't form a positive subarray ending with current number
[previous negative subarray] + [current number negative]
"""

"""
...0 [X X X j] 0 ...

if [i:j] negative count % 2 == 0 -> [i:j]
else: [k+1:j]

"""


class SolutionDP:
    def getMaxLen(self, nums):
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        # dp[i][0] : max length of subarray ending with index i With positive product
        # dp[i][1] : max length of subarray ending with index i With negative product

        # Base case: when index is 0, only one number can be used
        if nums[0] > 0:
            dp[0][0] = 1

        if nums[0] < 0:
            dp[0][1] = 1

        res = dp[0][0]
        for i in range(1, n):
            if nums[i] > 0:
                dp[i][0] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0:  # if previous negative subarray exists
                    dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)

            if nums[i] < 0:
                dp[i][1] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0:  # if previous negative subarray exists
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)

            res = max(res, dp[i][0])

        return res



"""
...0 [X X X j] 0 ...

if [i:j] negative count % 2 == 0 -> [i:j]
else: [k+1:j]

"""

class Solution:
    def getMaxLen(self, nums):
        res = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
                continue
            j = i
            count = 0
            firstNeg = -1
            while j < len(nums) and nums[j] != 0:
                count += (nums[j] < 0)
                if count % 2 == 0:
                    res = max(res, j-i+1)
                elif firstNeg != -1:
                    res = max(res, j-firstNeg)
                if firstNeg == -1 and nums[j] < 0:
                    firstNeg = j
                j += 1
            i = j
        return res




nums = [0,1,-2,-3,-4]
a = SolutionGreedy()
print(a.getMaxLen(nums))

