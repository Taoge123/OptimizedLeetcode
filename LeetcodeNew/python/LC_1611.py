"""
101011 -> 000000

101011 -> 1(10000) -> 0(10000) -> 0(00000)

minimumOneBitOperations(1xxxxx) = helper(xxxxx) + 1 + minimumOneBitOperations(100000)

helper(xxxxx) : the operations required to convert xxxxx to 10000
1. 1xxxx : minimumOneBitOperations(xxxx) + 1 + minimumOneBitOperations(1000)
2. 0(xxxx) -> 0(1000) -> 1(1000) -> 1(0000)

"""

import copy
import functools

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        s = bin(n)[2:]
        self.memo = {}
        self.memo2 = {}
        return self.dfs(list(s))

    def dfs(self, s):
        if len(s) == 1 and s[0] == '0':
            return 0
        if len(s) == 1 and s[0] == '1':
            return 1

        if tuple(s) in self.memo:
            return self.memo[tuple(s)]
        # remove leading 0
        if s[0] == '0':
            return self.dfs(s[1:])

        s2 = s[1:]
        # assign "1000000" and recurse
        p = copy.copy(s2)
        p[0] = '1'
        for i in range(1, len(p)):
            p[i] = '0'
        self.memo[tuple(s)] = self.helper(s2) + 1 + self.dfs(p)

        return self.memo[tuple(s)]

    def helper(self, s):
        if len(s) == 1 and s[0] == '0':
            return 1
        if len(s) == 1 and s[0] == '1':
            return 0

        if tuple(s) in self.memo2:
            return self.memo2[tuple(s)]

        # remove leading 1
        if s[0] == '1':
            self.memo2[tuple(s)] = self.dfs(s[1:])
        else:
            s2 = s[1:]
            p = copy.copy(s2)
            p[0] = '1'
            for i in range(1, len(p)):
                p[i] = '0'
            self.memo2[tuple(s)] = self.helper(s2) + 1 + self.dfs(p)
        return self.memo2[tuple(s)]


"""
First let's think of changing a power of 2 into 0. Let's say changing 2^k to 0.
There are 3 steps:

Change the right k-1 bits from 00..0 into 10..0.
Change the leftmost bit from 1 into 0.
Change the right k-1 bits from 10..0 into 00..0.
Notice that the step 1 and 3 are exactly the transformation of changing 2^(k-1) into 0.
Define bto0(k) as the number of operations to transform 2^k into 0. Then we have:

bto0(0) = 1
bto0(k) = 2 * bto0(k-1) + 1
Hence:

bto0(k) = 2^(k+1)-1
I think the key insight comes here: bto0(k) is basically the number of all the values that a (k+1) bits binary number can represent except 0, which means during the transformation from 2^k to 0, we have to go through every single number of all the k+1 bits binary numebrs.
So for any integer n (let's say it's k1 bits). It must be in the operations of changing 2^k2 (k2 > k1) into 0.

For the given integer n, let's say its leftmost bit is b1th bit, and call n without its leftmost bit as n'.
We can consider this integer n is just in the middle of the first step of changing 2^b1 into 0.
Here we get:

minimumOneBitOperations(n) = bto0(b1) - minimumOneBitOperations(n')
"""
import math

class Solution2:
    def minimumOneBitOperations(self, n: int) -> int:
        @functools.lru_cache(None)
        # change 2^b into 0
        def bto0(b):
            return (1 << b + 1) - 1

        @functools.lru_cache(None)
        # change integer n into 0
        def nto0(n):
            if n == 0:
                return 0
            b1 = int(math.log2(n))
            return bto0(b1) - nto0(n - (1 << b1))

        return nto0(n)



