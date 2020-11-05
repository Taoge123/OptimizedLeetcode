
class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for ch in s:
            if not res:
                res.append(ch)
            elif res[-1].isupper() and res[-1].lower() == ch:
                res.pop()
            elif res[-1].islower() and res[-1].upper() == ch:
                res.pop()
            else:
                res.append(ch)

        return "".join(res)


