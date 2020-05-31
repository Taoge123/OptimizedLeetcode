
"""
P = [3, 1, 2, 4, 5 ]

     1  2  3  4  5
     0  1  2  3  4

"""

import collections

class Solution:
    def processQueries(self, queries, m: int):

        res = []
        queue = collections.deque(list(range(1, m+ 1)))
        for num in queries:
            res.append(queue.index(num))
            queue.remove(num)
            queue.appendleft(num)

        return res

