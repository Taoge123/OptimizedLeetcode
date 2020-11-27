import collections


class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:

        table = collections.Counter()
        for row in matrix:
            table[tuple(row)] += 1
            flip = [ 1 -c for c in row]
            table[tuple(flip)] += 1

        return max(table.values())




