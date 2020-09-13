
"""
2 options

1. subarray[i:j] sum = preSum[j] - preSum[i]
   subarray[i:j] XOR = preXOR[j] ^ preXOR[i]

2. DP
X X X X X X X i
dp[i]: the subarray ending at i which bitwise AND is closest to target
X X X X [X X X i]
      j

dp[i] = dp[i-1]
dp[i] = dp[j] for j= 0,, 1, ...,i-1

dp[i] = best {A[i], A[i-1:i], A[i-2:i], ..., A[1:i]}           => max number 32
dp[i-1] = best {A[i-1], A[i-2:i-1], A[i-3:i], ..., A[1:i-1]}   => max number 32


"""

class Solution:
    def closestToTarget(self, arr, target: int) -> int:
        n = len(arr)
        dp = set()
        res = float('inf')

        for i in range(n):
            dp2 = set()
            for x in dp:
                dp2.add(x & arr[i])
            dp2.add(arr[i])

            for x in dp2:
                res = min(res, abs(x - target))
            dp = dp2

        return res

