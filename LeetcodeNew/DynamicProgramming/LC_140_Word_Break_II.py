
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

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


class Solution1:
    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})


    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res


class Solution2:
    def wordBreak(self, s, wordDict):
        res = []
        self.dfs(s, wordDict, '', res)
        return res

    def dfs(self, s, dic, path, res):
        # Before we do dfs, we check whether the remaining string
        # can be splitted by using the dictionary,
        # in this way we can decrease unnecessary computation greatly.
        if self.check(s, dic):  # prunning
            if not s:
                res.append(path[:-1])
                return  # backtracking
            for i in range(1, len(s) + 1):
                if s[:i] in dic:
                    # dic.remove(s[:i])
                    self.dfs(s[i:], dic, path + s[:i] + " ", res)

    # DP code to check whether a string can be splitted by using the
    # dic, this is the same as word break I.
    def check(self, s, dic):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]


"""
Word Break II https://leetcode.com/problems/word-break-ii/

Memoization

We parameterize the problem with a single variable k. helper(k, s, ....) returns all the solns to the problem for input string s[k:].
Given a s and k, we divide the string into left and right half by running a loop i from k to len(s). 
left = s[k:i+1]. If left is a valid word, we call the sub-problem helper(i+1, s...). 
The output of the sub-problem is combined with left to produce all results.
Corner case: left = s[k:len(s)]. The remainder for this problem is empty. 
So we return left as an answer given left is a valid word.
"""
class Solution3:
    def wordBreak(self, s, wordDict):
        return self.helper(0, s, set(wordDict), {})

    def helper(self, k, s, wordDict, cache):
        if k == len(s):
            return []
        elif k in cache:
            return cache[k]
        else:
            cache[k] = []
            for i in range(k, len(s)):
                left = s[k:i+1]
                if left in wordDict:
                    remainder = self.helper(i+1, s, wordDict, cache)
                    if remainder:
                        for x in remainder:
                            cache[k].append(left + " " + x)
                    elif (i == len(s)-1):
                        cache[k].append(left)
            return cache[k]




