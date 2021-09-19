"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class SolutionTD:
    def wordBreak(self, s: str, wordDict) -> bool:
        memo = {}
        return self.dfs(s, set(wordDict), 0, memo)

    def dfs(self, s, words, i, memo):
        if i in memo:
            return memo[i]
        n = len(s)
        if i == n:
            return True

        for j in range(i + 1, n + 1):
            if s[i:j] in words and self.dfs(s, words, j, memo):
                memo[i] = True
                return True
        memo[i] = False
        return False


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]







