

class Solution:
    def addBoldTag(self, s, words):
        status = [False] * len(s)
        res = ""
        for word in words:
            start = s.find(word)
            end = len(word)
            while start != -1:
                for i in range(start, start + end):
                    status[i] = True
                start = s.find(word, start + 1)
        i = 0
        while i < len(s):
            if status[i]:
                res += "<b>"
                while i < len(s) and status[i]:
                    res += s[i]
                    i += 1
                res += "</b>"
            else:
                res += s[i]
                i += 1
        return res





