

class Solution:
    def countLetters(self, S: str) -> int:
        res = 1
        count = 1
        for i in range(1, len(S)):
            if S[i - 1] == S[i]:
                count += 1
            else:
                count = 1
            res += count
        return res


