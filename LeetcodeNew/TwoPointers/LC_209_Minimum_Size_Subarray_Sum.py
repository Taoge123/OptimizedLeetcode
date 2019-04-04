
"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""
import math

"""
No special trick, just use this two pointer minimum window template, can apply to many problems.
ref: https://leetcode.com/problems/minimum-window-substring/
"""

class Solution111:
    def minSubArrayLen(self, s, nums):
        _sum = 0
        slow, fast = 0, 0
        min_len = len(nums) + 1
        while fast < len(nums):
            while (fast < len(nums) and _sum < s):  # Get possible candidate
                _sum += nums[fast]
                fast += 1

            while (slow < len(nums) and _sum >= s):  # Refine candiate
                min_len = min(min_len, fast - slow)
                _sum -= nums[slow]
                slow += 1
        return 0 if min_len == len(nums) + 1 else min_len



class Solution222:
    def minSubArrayLen(self, s, nums):

        left, total, res = 0, 0, float('inf')
        for right in range(len(nums)):
            total += nums[right]
            ''' sliding window problem, move left pointer to right until sum is smaller than target'''
            while total >= s:
                ''' decrease total when moving one step of left pointer'''
                total -= nums[left]
                res = min(res, right - left + 1)
                left += 1
        ''' corner case: sum of the list is less than target '''
        if res == float('inf'):
            return 0
        return res


class Solution333:
    def minSubArrayLen(self, s, nums):

        if not nums or len(nums) == 0: return 0

        i = j = 0
        total = nums[0]
        solution = math.inf
        while j < len(nums):
            if total < s:
                j += 1
                if j < len(nums): total += nums[j]
            else:
                solution = min(solution, j - i + 1)
                total -= nums[i]
                i += 1
        return 0 if solution == math.inf else solution

class Solution1:
    def minSubArrayLen(self, s, nums):
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0




class Solution2:

    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left



class Solution3:
    def minSubArrayLen(self, k, nums):
        count, i, j, n, res = 0, 0, 0, len(nums), float('inf')
        for j in range(len(nums)):
            count += nums[j]
            while i <= j and count >= k:
                res, = min(res, j - i + 1)
                count = count - nums[i]
                i += 1
        return res if res < float('inf') else 0


class Solution4:
    def minSubArrayLen(self, s, nums):

        i = j = curSum = 0
        mini = math.inf

        while j < len(nums):
            if curSum + nums[j] < s:
                curSum = curSum + nums[j]
                j += 1
            else:
                mini = min(j - i + 1, mini)
                curSum = curSum - nums[i]
                i += 1

        return mini if mini != math.inf else 0



