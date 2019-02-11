class Solution:
    def generateAbbreviations(self, word):
        l, res = len(word), []
        def dfs(s, i):
            if i == l:
                res.append(s)
            else:
                dfs(s + word[i], i + 1)
                if not s or s[-1] > "9":
                    for j in range(i + 1, l + 1):
                        dfs(s + str(j - i), j)
        dfs("", 0)
        return res



# We can observe that the rule is to replace substring with length
# but two consecutive replacement are illegal.

class Solution(object):
    def generateAbbreviations(self, word):
        res = []
        self.dfs(word, 0, res)
        return res

    def dfs(self, word, index, r):
        r.append(word)
        for s in range(1, len(word) + 1):
            for i in range(index, len(word)):
                if len(word) - i >= s:
                    self.dfs(word[:i]+str(s)+word[i+s:], i+len(str(s))+1, r)


#With cache (408 ms):
class Solution(object):
    def __init__(self):
        self._cache = {}

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]
        if word in self._cache:
            return self._cache[word]
        n = len(word)
        abbs = []
        for i in range(n, 0, -1):
            abbs.extend(str(i) + a for a in self.generateAbbreviations(word[i:]) if not a or not a[0].isdigit())
        abbs.extend(word[0] + a for a in self.generateAbbreviations(word[1:]))
        self._cache[word] = abbs
        return abbs


#Without cache (816 ms):
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        return self._helper(word)

    def _helper(self, word, prev_is_num=False):
        if not word:
            return [""]
        n, abbs = len(word), []
        if not prev_is_num:
            for i in range(n, 0, -1):
                abbs.extend(str(i) + a for a in self._helper(word[i:], True))
        abbs.extend(word[0] + a for a in self._helper(word[1:]))
        return abbs

    



