
class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        res = []
        while s:
            for ch in sorted(set(s)):
                s.remove(ch)
                res.append(ch)
            for ch in sorted(set(s), reverse=True):
                s.remove(ch)
                res.append(ch)
        return "".join(res)


