
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

    def solve(self, dict, i):
        table = collections.defaultdict(list)
        for word in dict:
            table[self.abbr(word, i)].append(word)
        for abbr, words in table.items():
            if len(words) == 1:
                self.res[words[0]] = abbr
            else:
                self.solve(words, i + 1)

    def wordsAbbreviation(self, dict):
        self.res = {}
        self.solve(dict, 0)
        print(self.res)
        res = []
        for word in dict:
            if word in self.res.keys():
                res.append(self.res[word])
            else:
                res.append(word)
        return res



dict = ["like", "god", "intenal", "me", "internet", "interval", "intension", "face", "intrusion"]
a = Solution()
print(a.wordsAbbreviation(dict))


