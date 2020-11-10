class Solution:
    def minStickers(self, stickers, target: str) -> int:
        n = len(target)
        N = (1 << n)
        dp = [float('inf') for i in range(N)]
        dp[0] = 0
        for i in range(N):
            if dp[i] == float('inf'):
                continue
            for word in stickers:
                # 状态 j + word 得到状态 i
                j = self.findNextState(i, word, target)
                dp[j] = min(dp[j], dp[i] + 1)

        if dp[N - 1] == float('inf'):
            return -1
        else:
            return dp[N - 1]

    def findNextState(self, state, word, target):
        n = len(target)
        for char in word:
            for k in range(n):
                # 如果state的第k位是空的, char可以填补上
                if ((state >> k) & 1) == 0 and target[k] == char:
                    state += (1 << k)
                    break
        return state

