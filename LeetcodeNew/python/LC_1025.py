

"""
解题思路
如果N为偶数，则坚持选择x = 1，对方得到N - 1为大于0的奇数
如果N为奇数：

如果N > 1, 其因子必然也是奇数，所以无论选择任何x，N - x都将变为偶数
由于x < N，给予对方的N - x必然是 > 0的偶数
如果N = 1，直接失败。
综上，N为偶数时必然大于0，只需要坚持选择x = 1，最终对方会得到N = 1而失败。
所以N为偶数时返回true。
用Flip Game II的方法也可以。

示例代码 (cpp)
"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        self.cache = [-1] * (N + 1)
        return self.canWin(N)

    def canWin(self, N):
        if N == 1:
            return False

        if self.cache[N] != -1:
            return self.cache[N]

        win = False
        for i in range(1, N):
            if N % i == 0:
                win |= not self.canWin(N - i)

        self.cache[N] = win
        return self.cache[N]



"""
1025.Divisor-Game
解法1:
常规的策略问题，可以用DP或者递归处理。假设某人手中持有数字i，那么遍历所有i的因数j（不包括i本身），如果发现持有数字i-j必败的话，那么说明持有i就必胜。边界条件是持有1必败。

解法2:
数学思维。如果我当前持有偶数，那么就减去1，将一个奇数传给对手。对手在处理奇数的时候，只能找到同为奇数的因数，所以相减之后又回传递给我一个偶数。
我再重复之前的操作。直至对手拿到的是1，对手负。所以只要先手拿到的是偶数，必胜。

如果先手拿到的是奇数，那么传递给对手的就是偶数，对手同样回采用之前的策略。所以先手必败。
"""

class Solution2:
    def divisorGame(self, N: int) -> bool:
        dp = [0] * (N + 1)
        dp[1] = 0

        for i in range(1, N + 1):
            j = 1
            while j * 2 <= i:
                if i % j == 0 and dp[i - j] == 0:
                    dp[i] = 1
                    break
                j += 1
        return dp[N]


