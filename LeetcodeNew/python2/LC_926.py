
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        if not S:
            return 0

        ones = 0
        flip = 0

        for ch in S:
            if ch == '0':
                if ones != 0:
                    flip += 1
                else:
                    continue
            else:
                ones += 1

            # flip = min(flip, ones)
            if flip > ones:
                flip = ones

        return flip



