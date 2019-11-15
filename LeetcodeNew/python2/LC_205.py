import collections

class Solution:
    def isIsomorphic(self, s, t):

        table = collections.defaultdict(str)

        for i, j in zip(s, t):
            if i in table:
                if table[i] != j:
                    return False
            else:
                if j in table.values():
                    return False
                else:
                    table[i] = j

        return True


