"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

class Solution:
    def wordBreak(self, s: str, wordDict):

        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                print(word)
                res.append(word)
            else:
                rest = self.helper(s[len(word):], wordDict, memo)
                for item in rest:
                    item = word + ' ' + item
                    print(item, '---')
                    res.append(item)
        memo[s] = res
        return res




class Solution2:
    def wordBreak(self, s: str, wordDict):
        memo = dict()
        return self.dfs(s, wordDict, memo)

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word:
                continue
            for item in self.dfs(s[len(word):], wordDict, memo):
                res.append(word + ("" if not item else " " + item))
        memo[s] = res
        return res


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

a = Solution()
print(a.wordBreak(s, wordDict))


