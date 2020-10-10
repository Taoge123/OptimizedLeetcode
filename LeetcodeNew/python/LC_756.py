import collections

class Solution:
    def pyramidTransition(self, bottom: str, allowed) -> bool:
        table = collections.defaultdict(set)

        for s in allowed:
            pre = s[:2]
            table[pre].add(s[2:])
        return self.helper(bottom, [], table, 1)

    def helper(self, cur, nxt, table, i):
        if len(cur) == 1:
            return True

        if len(nxt) + 1 == len(cur):
            return self.helper(nxt, [], table, 1)

        node = "".join(cur[i - 1:i + 1])
        for ch in table[node]:
            if self.helper(cur, nxt + [ch], table, i + 1):
                return True
        return False




