

"""
Similar to 418

Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2
if we can remove some characters from s2 such that it becomes s1.
For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long)
and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2,
where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""

"""
In my code, the first function defined what "contain" is and the second function is to find maximum m.

We know that, in the best case:
S1 = s1n1
S2 = s2n2
We compute the quotient of lengths of S1 and S2, which is M in the code and M is the best repetition we can get.
And count down from M, return the repetition as long as S1 contains S2.

For example:
if the length of S1 is 12, and S2's length is 3, the largest (best) m could be 4, or less,
if 4*S2 can't meet the condition, then let m be 3, and check again.
This way, we only check 4 times at worst.

"""
import collections

class Solution1:
    def Contain(self, L1, L2):
        for i in range(len(L2)):
            if L2[i] in L1:
                L1 = L1[L1.index(L2[i]):]
            else:
                return False
        return True

    def getMaxRepetitions(self, s1, n1, s2, n2):
        S1 = s1 * n1
        S2 = s2 * n2
        M = int(len(S1) // len(S2))
        for m in range(M, 1, -1):
            if self.Contain(S1, S2 * m):
                return m


"""
题目大意：
定义S = [s,n] 表示字符串S由字符串s重复n次构成。 例如["abc", 3] ="abcabcabc"

另一方面，我们定义字符串s1可以从s2得到，如果我们可以通过从s2中移除一些字符得到s1。例如根据定义，“abc”可以从“abdbec”得到，但是“acbbe”则不行。

给定两个非空字符串s1和s2（每个最多100个字符），两个整数 0 ≤ n1 ≤ 10^6 和 1 ≤ n2 ≤ 10^6。
现在考虑字符串S1和S2，其中S1=[s1,n1] 并且 S2=[s2,n2]。计算满足[S2,M]可以从S1得到的最大整数M。

解题思路：
贪心算法 + 寻找循环节

利用贪心算法计算s1与s2对应字符的匹配位置，由于s1与s2的循环匹配呈现周期性规律，因此可以通过辅助数组dp进行记录

记l1, l2为s1, s2的长度；x1, x2为s1, s2的字符下标

令y1, y2 = x1 % l1, x2 % l2

当s1[y1] == s2[y2]时：

  若dp[y1][y2]不存在，则令dp[y1][y2] = x1, x2

  否则，记dx1, dx2 = dp[y1][y2]，循环节为s1[dx1 ... x1], s2[dx2 ... x2]

"""

class Solution2:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if not set(s2) <= set(s1):
            return 0
        l1, l2 = len(s1), len(s2)
        dp = collections.defaultdict(dict)
        x1 = x2 = 0
        while x1 < l1 * n1:
            while s1[x1 % l1] != s2[x2 % l2]:
                x1 += 1
            if x1 >= l1 * n1:
                break
            y1, y2 = x1 % l1, x2 % l2
            if y2 not in dp[y1]:
                dp[y1][y2] = x1, x2
            else:
                dx1, dx2 = dp[y1][y2]
                round = (l1 * n1 - dx1) / (x1 - dx1)
                x1 = dx1 + round * (x1 - dx1)
                x2 = dx2 + round * (x2 - dx2)
            if x1 < l1 * n1:
                x1 += 1
                x2 += 1
        return x2 / (n2 * l2)







