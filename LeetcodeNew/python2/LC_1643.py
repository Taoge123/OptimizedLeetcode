"""
60. Permutation Sequence

"""

"""
HHHVV
H**** -> C(4, 2) = 6
V**** -> 3H + 1V 

1643.Kth-Smallest-Instructions
根据矩阵的行数和列数，我们就可以知道整个路径需要多少个H和多少个V。本题的本质就是求HHH..VVV...的k-th permutation，这和 060.Permutation-Sequence的解法相同。

我们假设有h个H和v个V。那么K-th permuation的第一个字母该是H还是V呢？考虑如果第一位是H，那么后面的n-1位就由h-1个H和v个V组成，这样的不同的字符串总共有多少个呢？答案就是组合数sum = C(h-1+v, h-1)。

如果k<=sum，那么必然第一位就是H，否则第一位以V开头的任何排列在字典序的次序必然大于sum。所以下一步求h-1个H和v个V组成的第k-th permutation。

反之如果k>sum，必然第一位就是V，我们接下来求h个H和v-1个V组成的第(k-sum)-th permutation。

递归的终止条件就是当h为零的时候，一定输出V；或者当v为零的时候，一定输出H。

"""
import math


class Solution:
    def kthSmallestPath(self, destination, k: int) -> str:
        V = destination[0]
        H = destination[1]
        n = H + V

        res = []
        for i in range(n):
            if H == 0:
                res.append('V')
                V -= 1
                continue
            elif V == 0:
                res.append('H')
                H -= 1
                continue

            summ = math.comb(H - 1 + V, V)
            if k <= summ:
                res.append('H')
                H -= 1
            else:
                V -= 1
                k -= summ
                res.append('V')

        return "".join(res)

    def comb(self, n, m):
        count = 1
        for i in range(m):
            count *= n - i
            count //= i + 1
        return count





