
"""
Given a positive integer n, return the number of all possible attendance records with length n,
which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
Note: The value of n won't exceed 100,000.
"""


# https://leetcode.com/problems/student-attendance-record-ii/discuss/101634/Python-DP-with-explanation

class Solution:
    def checkRecord(self, n):
        M = 1000000007
        if n == 0:
            return 0
        if n == 1:
            return 3
        nums = [1, 1, 2]
        for i in range(2, n):
            nums.append((nums[i] + nums[i - 1] + nums[i - 2]) % M)

        res = (nums[n] + nums[n - 1] + nums[n - 2]) % M
        for i in range(n):
            res += nums[i + 1] * nums[n - i] % M
            res %= M

        return res





