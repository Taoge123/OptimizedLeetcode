import collections
import heapq

class Solution:
    def highFive(self, items):
        table = collections.defaultdict(list)
        for i, score in items:
            if len(table[i]) < 5:
                heapq.heappush(table[i], score)
            else:
                heapq.heappushpop(table[i], score)

        res = []
        for i, score in table.items():
            res.append([i, sum(score) // 5])
        return res



