
"""
rand()%N
M
rand()%M -- U[0, M-1]

1 2 (3) 4 5 6 7 (8) (9)
1 2 4 5 6 7 (3) (8) (9)


"""


"""
https://leetcode.com/problems/random-pick-with-blacklist/discuss/146533/Super-Simple-Python-AC-w-Remapping


1234567  234
    i
j
table[]
table = {2 : 5,
         3 : 6,
         4 : 7,
  }
self.length = 4

"""

import random

class Solution:
    def __init__(self, N: int, blacklist):
        blacklist = sorted(blacklist)
        self.blacklist = set(blacklist)
        self.table = {}
        self.length = N - len(blacklist)
        j = 0
        for i in range(self.length, N):
            if i not in self.blacklist:
                self.table[blacklist[j]] = i
                j += 1

    def pick(self) -> int:
        i = random.randint(0, self.length - 1)
        return self.table[i] if i in self.table else i




