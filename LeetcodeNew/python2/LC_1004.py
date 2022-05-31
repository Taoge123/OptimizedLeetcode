"""
dp[i][k]: A[0:i], using k previligies, the length of the longest (contiguous) subarray that contains onlu 1s

A[i] == 1, dp[i][k] = dp[i-1][k] + 1
A[i] == 0, dp[i][k] = dp[i-1][k-1] + 1

X X X X X 1

X [i X X j] 0 X X

X 1 [X X j] 0 X X

X [i X X j] 0 X X

Translation:
Find the longest subarray with at most K zeros.


"""


class SolutionTonyHandsome:
    def longestOnes(self, nums, k: int) -> int:
        n = len(nums)
        left = 0
        res = 0
        for right in range(n):
            if nums[right] == 0:
                k -= 1
            if k >= 0:
                res = max(res, right - left + 1)
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return res


class SolutionRika:
    def longestOnes(self, nums, k: int) -> int:
        # longest subarry that includes k zeros
        zeroCount = 0
        count = 0
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                zeroCount += 1
            right += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            count = max(count, right - left)

        return count


class SolutionTony:
    def longestOnes(self, A, K: int) -> int:
        i = 0
        count = 0
        res = 0
        for j in range(len(A)):
            if A[j] == 1:
                res = max(res, j - i + 1)
            else:
                count += 1
                while count > K:
                    if A[i] == 0:
                        count -= 1
                    i += 1
                res = max(res, j - i + 1)

        return res



class Solution:
    def longestOnes(self, A, K):
        res = 0
        i = 0
        for j in range(len(A)):
            K -= A[j] == 0
            if K < 0:
                K += A[i] == 0
                i += 1
            res = j - i + 1
        return res


