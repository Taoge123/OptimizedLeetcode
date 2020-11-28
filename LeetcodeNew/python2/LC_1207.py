
import collections

class Solution:
    def uniqueOccurrences(self, arr) -> bool:

        count = collections.Counter(arr)
        freq = collections.Counter(count.values())

        return not any(val >= 2 for i, val in freq.items())


