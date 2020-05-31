
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n = len(S)
        if K > 26 and K > n:
            return 0
        res = 0
        for i in range(n - K + 1):
            if len(set(S[i:i + K])) == K:
                res += 1
        return res

class Solution2:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        left = 0
        window = set()
        res = 0
        for right in range(len(S)):
            while S[right] in window:
                window.remove(S[left])
                left += 1
            window.add(S[right])
            res += right - left + 1 >= K

        return res





