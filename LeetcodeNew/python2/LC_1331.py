
class Solution:
    def arrayRankTransform(self, arr):
        table = {}
        rank = 1
        for num in sorted(set(arr)):
            table[num] = rank
            rank += 1

        return [table[num] for num in arr]


