"""
This is a sampling n elements without replacement problem. It is the same as the operation that random shuffe an array and then return the first n elements.

Here come the trick. When we random pick an element in the array we can store its new position in a hash table
instead of the array because n is extremely less than the total num. So we can accomplish this within O(1) time and O(k) space where k is the maxium call of flip.

"""
"""
3*3

1 2 3
4 5 6
7 8 9
rand = 4
start = 3
table = {4 : 3,
         6 : 1,
         7 : 2,
          
        }

res = 0 

"""

import random

class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.n = n_cols
        self.end = n_rows * n_cols - 1
        self.table = {}
        self.start = 0

    def flip(self):
        rand = random.randint(self.start, self.end)
        res = self.table.get(rand, rand)
        self.table[rand] = self.table.get(self.start, self.start)
        self.start += 1
        return divmod(res, self.n)

    def reset(self) -> None:
        self.table = {}
        self.start = 0



