
"""
https://leetcode.com/problems/word-break/discuss/43903/Python-solutions-with-detailed-explanations
https://leetcode.com/problems/word-break/discuss/43947/4-liner-in-Python

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

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

"""
The idea is the following:

- d is an array that contains booleans

- d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

- s = "leetcode"

- words = ["leet", "code"]

- d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

- d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d."""

class Solution1:
    def word_break(slef, s, words):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]

class Solution2:
    def wordBreak(self, s, d):
        if not s:
            return s in d

        return self.dfs(s, d, 0, {})

    def dfs(self, s, d, idx, mem):
        if idx == len(s):
            return True

        if s[idx:] in mem:
            return mem[s[idx:]]

        for i in range(idx + 1, len(s) + 1):
            if s[idx:i] in d:
                if self.dfs(s, d, i, mem):
                    mem[s[idx:]] = 1
                    return True

        mem[s[idx:]] = 0
        return False


class Solution3:
    def wordBreak(self, s, d):
        if not s:
            return s in d

        n = len(s)
        f = [0] * (n + 1)
        for i in range(0, n + 1):
            f[i] = s[:i] in d
        for i in range(0, n + 1):
            for j in range(i, n + 1):
                f[j] |= f[i] and s[i:j] in d
        return f[-1]

class Solution4:
    def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1]


class TrieNode:
    def __init__(self, char=None, isWord=False):
        self.char = char
        self.isWord = isWord
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cache = {}

    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.isWord = True

    def cache(f):
        def method(obj, s):
            if s not in obj.cache:
                obj.cache[s] = f(obj, s)
            return obj.cache[s]
        return method

    @cache
    def search(self, s):
        root = self.root
        for i, char in enumerate(s):
            if char not in root.children:
                return False

            if root.children[char].isWord:
                if self.search(s[i + 1:]):
                    return True
            root = root.children[char]
        return root.isWord


class Solution5:
    def wordBreak(self, s, wordDict):
        trie = Trie()
        [trie.insert(word) for word in wordDict]

        return trie.search(s)

# Not sure why this is so fast. This prunes indices whose suffix can't be decomposed.
class Solution6:
    def _word_break(self, s, words, start, seen):
        if start == len(s):
            return True
        if start in seen:
            return False
        for i in range(start+1, len(s)+1):
            if i in seen:
                continue
            sub = s[start:i]
            if sub in words and self._word_break(s, words, i, seen):
                return True
        seen.add(start)
        return False

    def wordBreak(self, s, words):
        return self._word_break(s, set(words), 0, set())


class Solution7:
    def wordBreak(self, s, wordDict):
        l = len(s)
        dp = [[False] * l for i in range(l)]
        for n in range(0, l):
            for i in range(0, l - n):
                j = i + n
                if s[i:j + 1] in wordDict:
                    dp[i][j] = True
                else:
                    for k in range(i, j):
                        if dp[i][k] and dp[k + 1][j]:
                            dp[i][j] = True
                            break
        return dp[0][l - 1]



