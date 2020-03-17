import collections
import bisect

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        table = collections.defaultdict(list)
        for i, char in enumerate(source):
            table[char].append(i)

        res = 1
        i = -1
        for char in target:
            if char not in table:
                return -1

            offset = table[char]
            j = bisect.bisect_left(offset, i)
            if j == len(offset):
                res += 1
                i = offset[0] + 1
            else:
                i = offset[j] + 1

        return res

source = "xyz"
target = "xzyxz"








