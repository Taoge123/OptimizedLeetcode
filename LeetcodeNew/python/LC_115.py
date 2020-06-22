"""
010,097,072,712,727

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""

"""
dp[i][j]: the number of distinct subsequences of S[0:i] which equals T[0:j]

X X X X X X X X i
Y Y Y Y Y Y j

刷过一年的题之后，再做这道题就会很容易地看出这题属于two string convergence的套路。类似标签的题号有010,097,072,712,727.

令dp[i][j]表示s[1:i]中有多少个不同的子序列等于t[1:j]。

依照套路，我们首先分析如果s[i]==t[j]的情况。显然，这两个字符相等，我们就将注意力前移，集中在s[1:i-1]和t[1:j-1]上。
dp[i-1][j-1]表示s[1:i-1]中有多少个不同的子序列等于t[1:j-1]，两边分别加上s[i]和t[j]之后，
自然就有相同多数目的s[1:i]的不同子序列等于t[1:j]。所以算上这部分，dp[i][j]+=dp[i-1][j-1]。

如果s[i]!=t[j]的话，说明s[i]指望不上，我们就将注意力放在s[1:i-1]上，看里面有多少个不同子序列等于t[1:j]，直接拿过来用就行，
反正加上了s[i]也不管事。所以这种情况下，dp[i][j]+=dp[i-1][j].

注意：当s[i]==t[j]的时候，上述的第二种情况也是要累加进去的。原因也是显然的。

递推关系有了，那么边界条件呢？无非就是dp[0][j]和dp[i][0]的情况。显然，前者仍算是一种子序列，所以赋值为1，后者赋值为0.

"""


class SolutionTony:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[1 for j in range(n + 1)] for i in range(m + 1)]

        for j in range(1, n + 1):
            dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 0:
                    dp[i][j] = 0
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]




class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s) + 1, len(t) + 1
        dp = [[1] * n for i in range(m)]
        for j in range(1, n):
            dp[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * (s[i-1] == t[j-1])
        return dp[-1][-1]

class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s) + 1, len(t) + 1
        cur = [0] * n
        cur[0] = 1
        for i in range(1, m):
            pre = cur[:]
            for j in range(1, n):
                cur[j] = pre[j] + pre[j - 1] * (s[i - 1] == t[j - 1])
        return cur[-1]


import collections

class SolutionTest:
    def getFolderNames(self, names):
        table = collections.defaultdict(set)
        res = []
        for name in names:
            node = name.split('(')
            if len(node) == 1:
                k, v = node, 0
                if k[0] not in table:
                    table[k[0]].add(v)
                    res.append(name)
                else:
                    if v in table[k[0]]:
                        for num in range(len(table[k[0]])):
                            if num not in table[k[0]]:
                                table[k[0]].add(num)
                                res.append(k[0] + '(' + str(num) + ')')
                                break
                            num = len(table[k[0]])
                            table[k[0]].add(num)
                            res.append(k[0] + '(' + str(num) + ')')
                            break
                    else:
                        num = len(table[k[0]]) + 1
                        table[k].add(num)
                        res.append(k[0] + '(' + str(num) + ')')



            else:
                k, v = node
                if k not in table:
                    table[k].add(int(v[:-1]))
                    res.append(name)
                else:
                    if int(v[:-1]) in table[k]:
                        for num in range(len(table[k])):
                            if num not in table[k]:
                                table[k].add(num)
                                res.append(k + '(' + str(num) + ')')
                    else:
                        num = int(v[:-1])
                        table[k].add(num)
                        res.append(k + '(' + str(num) + ')')

        return res


class SolutionTest2:
    def avoidFlood(self, rains):
        zeros = 0
        res = []
        count = []
        flag = False
        table = collections.defaultdict(int)
        for i, num in enumerate(rains):
            if num == 0:
                zeros += 1
                flag = True
                res.append(0)
            elif num not in table:
                table[num] == 1
                res.append(-1)
            else:
                if flag and zeros <= 0:
                    return []
                if zeros < 0:
                    return []

                zeros -= 1
                count.append(num)
                res.append(-1)

        print(count)
        print(res)
        anotherCount = set([i for i in range(10**5)])
        anotherCount -= set(count)
        j = 0
        for i in range(len(res)):
            if res[i] == 0:
                if j < len(count):
                    res[i] = count[j]
                    j += 1
                else:
                    for node in range(1, 10**9):
                        if node in anotherCount:
                            res[i] = node
                            anotherCount.discard(node)
                            break
        return res




rains = [10,20,20]
a = SolutionTest2()
print(a.avoidFlood(rains))