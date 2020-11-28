
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        table = {}
        for i in range(len(keyboard)):
            table[keyboard[i]] = i
        res = 0
        prev = 0
        for ch in word:
            res += abs(table[ch] - prev)
            prev = table[ch]
        return res
