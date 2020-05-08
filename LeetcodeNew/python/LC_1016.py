"""
Solution 1
Intuition:
The construction of S is a NP problem,
it's time consuming to construct a short S.
I notice S.length <= 1000, which is too small to make a big N.

This intuition lead me to the following 1-line python solution,
which can be implemented very fast.


Explanation:
Check if S contains binary format of N,
If so, continue to check N - 1.


Time Complexity
Have a look at the number 1001 ~ 2000 and their values in binary.

1001 0b1111101001
1002 0b1111101010
1003 0b1111101011
...
1997 0b11111001101
1998 0b11111001110
1999 0b11111001111
2000 0b11111010000

The number 1001 ~ 2000 have 1000 different continuous 10 digits.
The string of length S has at most S - 9 different continuous 10 digits.
So S <= 1000, the achievable N <= 2000.
So S * 2 is a upper bound for achievable N.
If N > S * 2, we can return false directly in O(1)

Note that it's the same to prove with the numbers 512 ~ 1511, or even smaller range.

N/2 times check, O(S) to check a number in string S.
The overall time complexity has upper bound O(S^2).
"""

"""
解题思路
这道题最重要的是估计N的上限，超过上限全都是false了。
由于题目中给了S.length最大为1000，我们考虑11位二进制数（也就是1024 - 2047）总共有 > 1000个
然而长度为1000的字符串，取连续的11位数（即长度为11的子串），
总共只能取1000 - 10 = 990种 < 1000 => 不可能包含所有11位binary，所以N最多也就是11位数，其上限为2^11 = 2048
一般来说（分析时间复杂度会用到）：2^(k+1) - 2^k <= S.length => 2^k <= S.length, 上限为2^(k+1)次也就是2 * S.length
知道了这一上限，我们直接暴力求解即可: 将1 - N每一个转化为二进制，然后在S中寻找看是否能找到。
另外有一个优化是：我们只需要算 > N/2的数，因为如果一个数k的二进制是S的子串，那么k/2只不过少了一位，一定也是S的子串，没有必要再算。

"""

class Solution:
    def queryString(self, S, N):
        for i in range(N, 0, -1):
            if bin(i)[2:] not in S:
                return False

        return True





