import collections


class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:

        count = collections.Counter(tuple(sorted(pair)) for pair in dominoes)
        return sum([num * (num - 1) // 2 for num in count.values()])


