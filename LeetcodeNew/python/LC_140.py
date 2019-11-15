
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
                res.append(word)
            else:
                rest = self.helper(s[len(word):], wordDict, memo)
                for item in rest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res

        return res





