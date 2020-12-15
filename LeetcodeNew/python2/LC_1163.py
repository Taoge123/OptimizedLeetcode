
class Solution2:
    # 不超时解法
    def lastSubstring(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        res = s
        maxchar = max(s)
        for i in range(1, len(s)):
            if s[i] == maxchar and s[i:] > res:
                res = s[i:]
        return res



class Solution:
    def lastSubstring(self, s: str) -> str:
        maxs = s
        for i in range(1, len(s)):
            maxs = max(maxs, s[i:])
        return maxs

