import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        table = collections.defaultdict(list)
        maxi = 0
        for num in range(1, n + 1):
            size = sum([int(i) for i in str(num)])
            table[size].append(num)
            maxi = max(maxi, len(table[size]))

        res = 0
        for k, val in table.items():
            if len(val) == maxi:
                res += 1
        return res


