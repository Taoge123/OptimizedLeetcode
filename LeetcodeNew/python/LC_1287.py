import collections

class Solution:
    def findSpecialInteger(self, arr) -> int:
        n = len(arr)
        count = collections.Counter(arr)

        for k, val in count.items():
            if val > n // 4:
                return k


