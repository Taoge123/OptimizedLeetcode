"""
https://leetcode.com/problems/get-equal-substrings-within-budget/discuss/392901/Standard-Python-moving-window-(similar-problems-listed)
1208. Get Equal Substrings Within Budget
3. Longest Substring Without Repeating Characters
76. Minimum Window Substring
159. Longest Substring with At Most Two Distinct Characters
209. Minimum Size Subarray Sum
340. Longest Substring with At Most K Distinct Characters
424. Longest Repeating Character Replacement
992. Subarrays with K Different Integers
713. Subarray Product Less Than K

"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        n = len(s)
        cost = 0
        left = 0
        res = 0
        for right in range(n):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            res = max(res, right - left + 1)

        return res




class SolutionLee:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        n = len(s)
        nums = [0] * n

        for i in range(n):
            nums[i] = abs(ord(s[i]) - ord(t[i]))

        left = 0
        for right in range(n):
            maxCost -= nums[right]
            if maxCost < 0:
                maxCost += nums[left]
                left += 1

        return right - left + 1



