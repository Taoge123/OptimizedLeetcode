
class SolutionTony:
    def findAndReplacePattern(self, words, pattern: str):
        def generate_key(word):
            table = {}
            match = ""
            num = 10
            # start at 10, map distinct characters into keys
            for ch in word:
                if ch not in table:
                    table[ch] = num
                    num += 1
                match += str(table[ch])
            return match

        match = generate_key(pattern)
        res = []
        for word in words:
            key = generate_key(word)
            if key == match:
                res.append(word)
        return res



class SolutionRika:
    def findAndReplacePattern(self, words, pattern: str):
        # hashmap --> 用hashmap存每个word的pattern --> abc

        p = self.convert2code(pattern)

        res = []
        for word in words:
            code = self.convert2code(word)
            if code == p:
                res.append(word)

        return res

    def convert2code(self, word):
        num = 0
        seen = {}
        code = ""
        for ch in word:
            if ch not in seen:
                num += 1
                seen[ch] = chr(ord('a') + num)
                code += chr(ord('a') + num)
            else:
                code += seen[ch]
        return code

class Solution:
    def findAndReplacePattern(self, words, pattern):
        res = []

        for word in words:
            if (self.findAndReplacePatternForSingleWord(word, pattern)):
                res.append(word)

        return res

    def findAndReplacePatternForSingleWord(self, word, pattern):

        table1 = {}
        table2 = {}
        for i in range(len(pattern)):
            table1[word[i]] = pattern[i]
            table2[pattern[i]] = word[i]

        for i in range(len(pattern)):
            if (table1[word[i]] != pattern[i] or table2[pattern[i]] != word[i]):
                return False

        return word




