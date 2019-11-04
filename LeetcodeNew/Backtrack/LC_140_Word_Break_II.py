"""
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

#Important solution

def wordBreak(self, s, wordDict):
    res = []
    self.dfs(s, wordDict, '', res)
    return res

def dfs(self, s, dic, path, res):
# Before we do dfs, we check whether the remaining string
# can be splitted by using the dictionary,
# in this way we can decrease unnecessary computation greatly.
    if self.check(s, dic): # prunning
        if not s:
            res.append(path[:-1])
            return # backtracking
        for i in range(1, len(s)+1):
            if s[:i] in dic:
                # dic.remove(s[:i])
                self.dfs(s[i:], dic, path+s[:i]+" ", res)

# DP code to check whether a string can be splitted by using the
# dic, this is the same as word break I.
def check(self, s, dic):
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in dic:
                dp[i] = True
    return dp[-1]



import collections
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # running time: O(mn^2), n = len(s), m = len(wordDict)
        """
        Let‘s say the average word length in wordDict is k, so it takes n/k times to reach end.
        Each time, the helper function would be called and it's running time is O(m*n)
        So the whole runinng time  would be O( m*n*n/k), which is O(m*n^2)
        """
        dic = collections.defaultdict(list)

        def helper(s):
            if not s: return [None]
            if s in dic: return dic[s]
            res = []
            for word in wordDict:
                n = len(word)
                if word == s[:n]:
                    for each in helper(s[n:]):
                        if each:
                            res.append(word + " " + each)
                        else:
                            res.append(word)
                dic[s] = res
            return res

        return helper(s)



"""
Basic idea is starting from left most character of string, increase the index, 
if s[:idx+1] is a valid word, try generate all combinations of s[idx+1:]. 
Continue doing this until index reaches the end of string. This is a recursive solution, 
so each time all word break options are calculated, cache them.
"""


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.dict = dict
        self.cache = {}
        return self.break_helper(s)

    def break_helper(self, s):
        combs = []
        if s in self.cache:
            return self.cache[s]
        if len(s) == 0:
            return []

        for i in range(len(s)):
            if s[:i + 1] in self.dict:
                if i == len(s) - 1:
                    combs.append(s[:i + 1])
                else:
                    sub_combs = self.break_helper(s[i + 1:])
                    for sub_comb in sub_combs:
                        combs.append(s[:i + 1] + ' ' + sub_comb)

        self.cache[s] = combs
        return combs


#Bottom up DP
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        sentences = [[] for i in range(len(s))]
        wordLenList = set(map(len, dict))
        for startIndex in range(len(s) - 1, -1, -1):
            for wordLen in wordLenList:
                if startIndex + wordLen > len(s) or s[startIndex: startIndex + wordLen] not in dict:
                    continue
                if startIndex + wordLen == len(s):
                    sentences[startIndex].append(s[startIndex: startIndex + wordLen])
                else:
                    for sentence in sentences[startIndex + wordLen]:
                        sentences[startIndex].append(s[startIndex: startIndex + wordLen] + " " + sentence)
        return sentences[0]


class SolutionTony:
    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                list = self.helper(s[len(word):], wordDict, memo)
                for item in list:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res



s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

a = SolutionTony()
print(a.wordBreak(s, wordDict))


