"""
781. Rabbits in Forest
"""

import collections

class Solution:
    def groupThePeople(self, groupSizes):
        table = collections.defaultdict(list)
        res = []
        for i, num in enumerate(groupSizes):
            table[num].append(i)

        for k, v in table.items():
            if len(v) <= k:
                res.append(v)
            else:
                while len(v) > k:
                    res.append(v[:k])
                    v = v[k:]
                res.append(v)
        return res


class Solution2:
    def groupThePeople(self, groupSizes):
        table = collections.defaultdict(list)
        res = []
        for i, num in enumerate(groupSizes):
            table[num].append(i)
            if len(table[num]) == num:
                res.append(table[num])
                table[num] = []

        return res




"""
3,3,3,3,3,1,3
0 1 2 3 4 5 6

4 - [546] (6)
2 - [5]           (1)

while size > key:
    res.append([0,1,2,3], [4,6])

"""

