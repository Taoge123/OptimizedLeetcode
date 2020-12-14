
class Solution:
    def movesToStamp(self, stamp: str, target: str):
        if stamp not in target:
            return []
        n, m = len(stamp), len(target)
        res = []

        def match(s, t):  # check whether s==t for all not '*' positions.
            return all(t[i] == '?' or s[i] == t[i] for i in range(len(s)))

        while True:
            updated = False
            for i in range(m):
                if i + n <= m and target[i:i + n] != '?' * n and match(stamp, target[i:i + n]):
                    updated = True
                    res.append(i)
                    target = target[:i] + '?' * n + target[i + n:]
            if target == '?' * m:
                return res[::-1]  # Done. return the res reservely
            if not updated:
                return []  # If no res can be updated, it means no solution.


