import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        table = {}
        for i in range(len(s) - minSize + 1):
            word = s[i:i+minSize]
            if word in table:
                table[word] += 1
            else:
                count = collections.Counter(word)
                if len(count) <= maxLetters:
                    table[word] = 1

        return max(table.values()) if table else 0



