import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        table = collections.Counter(s)

        odds = 0
        for count in table.values():
            odds += count % 2

        return odds <= k


