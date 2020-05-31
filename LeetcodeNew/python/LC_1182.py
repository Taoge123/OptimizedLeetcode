import collections
import bisect

class Solution:
    def shortestDistanceColor(self, colors, queries):
        table = collections.defaultdict(list)
        # group all indexes by color
        for i, val in enumerate(colors):
            table[val].append(i)

        res = []
        for i, color in queries:
            if color in table:
                # search where the element can be inserted
                index = bisect.bisect_left(table[color], i)
                if index == 0:
                    res.append(abs(i - table[color][0]))

                elif index >= len(table[color]):
                    res.append(i - table[color][-1])

                else:
                    res.append(min(abs(i - table[color][index - 1]), abs(table[color][index] - i)))
            else:
                res.append(-1)
        return res






