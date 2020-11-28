"""
https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid/solution/gei-n-x-3-wang-ge-tu-tu-se-de-fang-an-shu-by-leetc/


解题思路
本题一看答案很大要取余，再加上发现第i行的涂色方案实际上只受第i-1行的限制，因此想到可以用dp
初始的想法是，列出第i-1行每一个可能的涂色情况（共12种情况，示例一已经给出）下，对应的第i行可以有哪些涂色方案，这样就可以推导出第dp[i][case1..12]与dp[i-1][case1...12]关系了
于是开始老老实实地列举这12种情况下的下一行可能的涂色方案数，幸运地发现了新的规律：
这12种涂色方案可以分为两大类：对称的（例如红/黄/红）和不对称的（例如红/黄/绿）
对于对称的情况而言，它们的下一行可以有5种涂色方案，其中有三种对称的和两种不对称的，例如，红/黄/红的下一行可以是 黄/红/黄、绿/红/绿、黄/绿/黄、黄/红/绿、绿/红/黄
对于不对称的情况而言，它们的下一行可以有4种涂色方案，其中有两种对称的和两种不对称的，例如，红/黄/绿的下一行可以是 黄/红/黄、黄/绿/黄、黄/绿/红、绿/红/黄
因此我们只要知道i-1行网格的所有涂色方案中，最后一行为对称的方案的数量a，以及最后一行为不对称的方案的数量b，则i行网格的所有涂色方案数为5a+4b，而每次迭代a和b的变换公式为a=3a+2b, b=2a+2b

思路：
1.分为两种情况，
一种是最后一行有两种颜色的，记为a,举例xyx
一种是最后一行有三种颜色的，记为b,类似xyz，
a类添加下一行，可以加五种不同的，yxy,yxz,yzy,zxy,zxz,3种为a，2种为b
b类添加下一行，可以加四种不同的，yxy,yzx,yzy,zxy,2种为a，2种为b

那么我们可以得到
a[i] = 3 * a[i - 1] + 2 * b[i - 1];
b[i] = 2 * a[i - 1] + 2 * b[i - 1];
sum[i] = a[i] + b[i];

当然我们只用保存a和b就行了，返回a[n - 1] + b[n - 1] 就行了。
注意要用int64，要不会越界。

"""


class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        types = []
        # 预处理所有满足条件的type
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k:
                        types.append(i * 9 + j * 3 + k)

        count = len(types)
        # 找出所有可以作为相邻的type对
        related = [[0 for i in range(count)] for j in range(count)]
        for i, t1 in enumerate(types):
            # 得到types[i]三个位置的颜色
            a1, b1, c1 = t1 // 9, t1 // 3 % 3, t1 % 3
            for j, t2 in enumerate(types):
                # 得到types[i]三个位置的颜色
                a2, b2, c2 = t2 // 9, t2 // 3 % 3, t2 % 3
                # 对应位置不同色才能作为相邻行
                if a1 != a2 and b1 != b2 and c1 != c2:
                    related[i][j] = 1

        dp = [[0 for i in range(count)] for j in range(n + 1)]
        dp[1] = [1] * count
        for i in range(2, n + 1):
            for j in range(count):
                for k in range(count):
                    if related[k][j]:
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
        res = sum(dp[n]) % mod
        return res




