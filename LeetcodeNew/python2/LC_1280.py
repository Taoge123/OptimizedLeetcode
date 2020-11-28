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
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s]for s, l in count.items() for i in xrange(0, len(l), s)]


