
"""
https://www.bilibili.com/video/BV1HV411i7id?vd_source=c5928795c3e6210df961484faf790a47

'l2e' = {list: 1} ['like']
'god' = {list: 1} ['god']
'i6l' = {list: 2} ['internal', 'interval']
'me' = {list: 1} ['me']
'i6t' = {list: 1} ['internet']
'i7n' = {list: 2} ['intension', 'intrusion']
'f2e' = {list: 1} ['face']
"""

import collections


class Solution:
    def abbr(self, word, i):
        if len(word) - i <= 3:
            return word
        return word[:i + 1] + str(len(word) - i - 2) + word[-1]

    def solve(self, words, i):
        table = collections.defaultdict(list)
        for word in words:
            table[self.abbr(word, i)].append(word)

        for k, vals in table.items():
            if len(vals) == 1:
                self.res[vals[0]] = k
            else:
                self.solve(vals, i + 1)

    def wordsAbbreviation(self, words):
        self.res = {}
        self.solve(words, 0)
        res = []
        for word in words:
            if word in self.res.keys():
                res.append(self.res[word])
            else:
                res.append(word)
        return res


class SolutionRika:
    def wordsAbbreviation(self, words):
        # 先把所有的abb的单词放到一起，{abb:word1, word2.. }
        # 检查是否有哪个abb个数超过了2, 用recursion来计算下一个abb

        word2abbr = {}  # {word: abbr}
        self.getUniqueAbbrs(word2abbr, words, 0)  # abbr --> start from word[0] + size + word[-1]

        res = []
        for word in words:
            res.append(word2abbr[word])
        return res

    def getUniqueAbbrs(self, word2abbr, words, i):
        table = collections.defaultdict(list)  # {abbr: word}

        for word in words:
            abbr = self.getAbbr(word, i)
            table[abbr].append(word)

        for abbr, wordlist in table.items():
            if len(wordlist) == 1:
                word2abbr[wordlist[0]] = abbr
            else:
                self.getUniqueAbbrs(word2abbr, wordlist, i + 1)

    def getAbbr(self, word, i):
        if len(word) - i <= 3:
            return word
        return word[:i + 1] + str(len(word) - i - 2) + word[-1]


dict = ["like", "god", "intenal", "me", "internet", "interval", "intension", "face", "intrusion"]
a = Solution()
print(a.wordsAbbreviation(dict))


