import collections


class Solution:
    def canBeEqual(self, target, arr) -> bool:
        return collections.Counter(target) == collections.Counter(arr)



