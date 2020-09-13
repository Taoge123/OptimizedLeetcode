"""
1531.String-Compression-II
第一印象时我会这样设计DP方案：dp[i][k]表示前i个字母里删除k个所能得到的最优解（即最短的行程长度编码）。突破口应该是考虑第k个删除的字母的位置j在哪里，所以状态转移方程大致是：

dp[i][k] = max{dp[j-1][k-1] + s[j+1:i]的行程长度编码} for j=1,2,...i
但是我们在跑第二个例子 s = "aabbaa", k = 2 的时候会发现问题：我们删除了中间的bb，则第一段aa和最后一段的aa会拼接起来。而上述的表达式中完全没有考虑到拼接的处理。

换句话说，dp[j-1][k-1]对应的原码，和s[j+1:i]这段原码，其run-length encode不是简单的长度相加关系，而是有可能拼接在一起，形成更短的run-length encode. 为了便于处理这种“拼接关系”，我们需要提供更多的信息接口。所以会有以下的想法：令dp[i][k][ch][num]表示前i个字母、删除k个字母、最后的字母是ch、最后的字母连续出现的次数是num，所对应的最优解（即最短的行程长度编码）。

那么求解dp[i][k][ch][num]的关键是找到哪合法的前驱状态dp[?][?][?][?]可以转移到它。实际写代码的过程中，发现这样实现比较复杂。我们可以用另外一种DP的写法，就是看dp[i][k][ch][num]能够影响哪些后继节点。事实上，它直接影响的就是dp[i+1][?][?][?]的状态，我们只要讨论dp[i+1][?][?][?]的取值可能性即可。

如果第i+1个元素我们是要删除的。那么dp[i][k][ch][num]的结果原封不动地传递给了dp[i+1][k+1][ch][num].也就是前i+1个元素里、我们删除k+1个字母、最后的字母是ch、最后的字母连续出现的次数是num，有一种解就是与dp[i][k][ch][num]的状态完全相同。
如果第i+1个元素我们要保留，说明我们有机会更新dp[i+1][k][s[i]-'a'][?]的值。注意，既然保留了第i+1个字母，显然最后的字母就是s[i+1]，所以我们只需要确定最后一个问号即可。这个“连续”数目显然取决于s[i+1]是否和ch是否相同。如果不同，那么说明无法拼接上，所以我们直接可以更新的是 dp[i+1][k][s[i]-'a'][1]。怎么更新？就是dp[i][k][ch][num]+1，即run-length encode单纯地加上1.
如果第i+1个元素我们要保留，并且s[i+1]和ch相同，那么说明dp[i][k][ch][num]的最后字母ch可以再拼接一个，也就是说我们可以更新的是dp[i][k][ch][num+1]。怎么更新，是简单地在dp[i][k][ch][num]基础上加1吗？并不一定。其实需要根据num分情况讨论（附上了例子）来确定增加的run-length encode的长度：
                            if (num==1) add = 1;  // e.g: a -> a2
                            else if (num>=2 && num<=8) add = 0; // e.g: a3->a4
                            else if (num==9) add = 1; // e.g: a9->a10;
                            else if (num>=10) add = 0; // e.g: a10->a11;
最终的结果是要求在所有n个字母中删去K个字母，所以需要再dp[n][K][?][?]中挑选一个最小值。

另外需要注意的一个技巧是，我们不需要把第四个维度开到100，事实上num>=10之后，即使再拼接相同的字母，run-length encode也都不会再改变。所以我们可以把所有num>=10的状态都归为同一个状态，来节省空间的开辟。



dp[i][k] : for s[1:i], with k letters removed, the optimal solution

XXXX j XX i

dp[i][k] = max{dp[j-1][k-1] + s[j+1:i] Run-length encoding} for j - 1,2,..., i

aab baa
有个问题, 拆成这样就不对了
还需要2个维度
dp[i][k][ch][num]: for s[1:i], with k letters removed, the last letter as ch, the repeating number of the last letter as num

dp[i][k][ch][num] = f(dp[?][?][?][?])

dp[i][k][ch][num] -> dp[i+1][?][?][?]

XXXXXXch ch ch    s[i+1]
1 ...        i
k letters removed

1. we delete s[1+1] 删除下一个字母
    dp[i+1][k+1][ch][num] - min(dp[i][k][ch][num])

2. we keep s[i+1]
    2.1 if ch != s[i+1]:
        dp[i+1][k][s[i+1]-'a'][1] = min(dp[i][k][ch][num] + 1)
    2.2 if ch == s[i+1]:
        dp[i+1][k][s[i+1]-'a'][num+1] = min(dp[i][k][ch][num] + add)   add = 0, 1
        (1) if (num==1)          add=1      //a -> a2
        (2) if (num==2..8)       add=2..8   //a2 -> a3
        (3) if (num==9)          add = 1    //a9->a10
        (4) if (num==10..98)     add = 0    //a10->a11

return dp[n][K][?][?]

"""

from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # this decorator automatically use memo with key = (start, last, last_count, left)
        @lru_cache(None)
        def dp(start, last, last_count, left):  # count the cost of compressing from the start
            if left < 0:
                return float('inf')  # this is impossible
            if start >= len(s):
                return 0
            if s[start] == last:
                # we have a stretch of the last_count of the same chars, what is the cost of adding one more?
                add = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                # no need to delete here, if we have a stretch of chars like 'aaaaa' - we delete it from the beginning in the else delete section
                return add + dp(start + 1, last, last_count + 1, left)  # we keep this char for compression
            else:
                # keep this char for compression - it will increase the result length by 1 plus the cost of compressing the rest of the string
                keep = 1 + dp(start + 1, s[start], 1, left)
                # delete this char
                delete = dp(start + 1, last, last_count, left - 1)
                return min(keep, delete)
        return dp(0, "", 0, k)




class Solution0:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i, last, last_count, left):  # count the cost of compressing from the start
            if left < 0:
                return float('inf')  # this is impossible
            if i >= len(s):
                return 0
            if s[i] == last:
                add = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                return add + dp(i + 1, last, last_count + 1, left)  # we keep this char for compression
            else:
                keep = 1 + dp(i + 1, s[i], 1, left)
                delete = dp(i + 1, last, last_count, left - 1)
                return min(keep, delete)

        return dp(0, "", 0, k)


"""
dp[i][k] : for s[1:i], with k letters removed, the optimal solution

XXXX j XX i

dp[i][k] = max{dp[j-1][k-1] + s[j+1:i] Run-length encoding} for j - 1,2,..., i

aab baa
有个问题, 拆成这样就不对了
还需要2个维度
dp[i][k][ch][num]: for s[1:i], with k letters removed, the last letter as ch, the repeating number of the last letter as num

dp[i][k][ch][num] = f(dp[?][?][?][?])

dp[i][k][ch][num] -> dp[i+1][?][?][?]

XXXXXXch ch ch    s[i+1]
1 ...        i
k letters removed

1. we delete s[1+1] 删除下一个字母
    dp[i+1][k+1][ch][num] - min(dp[i][k][ch][num])

2. we keep s[i+1]
    2.1 if ch != s[i+1]:
        dp[i+1][k][s[i+1]-'a'][1] = min(dp[i][k][ch][num] + 1)
    2.2 if ch == s[i+1]:
        dp[i+1][k][s[i+1]-'a'][num+1] = min(dp[i][k][ch][num] + add)   add = 0, 1
        (1) if (num==1)          add=1      //a -> a2
        (2) if (num==2..8)       add=2..8   //a2 -> a3
        (3) if (num==9)          add = 1    //a9->a10
        (4) if (num==10..98)     add = 0    //a10->a11

return dp[n][K][?][?]

"""



class SolutionWisdom:
    def getLengthOfOptimalCompression(self, s: str, K: int) -> int:
        n = len(s)
        s = "#" + s
        dp = [[[[0 for i in range(11)] for j in range(27)] for k in range(101)] for _ in range(101)]
        for i in range(n + 1):
            for k in range(K + 1):
                for ch in range(27):
                    for num in range(11):
                        dp[i][k][ch][num] = float('inf')

        # 26 代表不存在的编译字母
        dp[0][0][26][0] = 0

        for i in range(n):
            # 删除字母最多i个
            for k in range(min(K + 1, i) + 1):
                for ch in range(27):
                    for num in range(11):
                        cur = dp[i][k][ch][num]
                        if cur == float('inf'):
                            continue

                        # delete s[i+1]
                        dp[i + 1][k + 1][ch][num] = min(dp[i + 1][k + 1][ch][num], cur)

                        # keep
                        if ord(s[i + 1]) - ord('a') != ch:
                            dp[i + 1][k][ord(s[i + 1]) - ord('a')][1] = min(dp[i + 1][k][ord(s[i + 1]) - ord('a')][1],
                                                                            cur + 1)
                        else:
                            add = 0
                            if num == 1:
                                add = 1
                            elif num >= 2 and num <= 8:
                                add = 0
                            elif num == 9:
                                add = 1
                            elif num >= 10:
                                add = 0
                            dp[i + 1][k][ch][min(num + 1, 10)] = min(dp[i + 1][k][ch][min(num + 1, 10)], cur + add)

        res = float('inf')
        for ch in range(27):
            for num in range(11):
                res = min(res, dp[n][K][ch][num])
        return res



