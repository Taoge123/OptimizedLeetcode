import collections

class Solution:
    def minSetSize(self, arr) -> int:
        count = collections.Counter(arr)
        n = len(arr)
        res = 0
        for i, freq in enumerate(sorted(count.values(), reverse=True)):
            res += freq
            if res >= n // 2:
                return i + 1
        return n // 2


