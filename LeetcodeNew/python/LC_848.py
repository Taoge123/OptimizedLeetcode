
class Solution:
    def shiftingLetters(self, S: str, shifts) -> str:
        summ = 0
        chars = list(S)
        for i in reversed(range(len(shifts))):
            cur = ord(chars[i]) - ord('a')
            summ += shifts[i] % 26
            cur += summ
            chars[i] = chr(ord('a') + cur % 26)

        return "".join(chars)



