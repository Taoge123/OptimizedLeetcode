import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        table = {}
        for i in range(len(s) - minSize + 1):
            # smaller the word, higher the frequency
            word = s[i:i+minSize]
            if word in table:
                table[word] += 1
            else:
                # if the word never occurred, add it to table if it has <= maxLetters unique letters
                count = collections.Counter(word)
                if len(count) <= maxLetters:
                    table[word] = 1

        return max(table.values()) if table else 0



