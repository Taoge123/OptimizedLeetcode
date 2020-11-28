
"""
https://www.youtube.com/watch?v=uzfsrChj8dM
https://leetcode.com/problems/stone-game-iii/discuss/564342/JavaC%2B%2BPython-Dynamic-Programming
https://medium.com/algorithm-solving/leetcode-1406-stone-game-iii-e575add6530b
https://blog.csdn.net/qq_17550379/article/details/105402637


Solution 1: DP
dp[i] means, if we ignore before A[i],
what's the highest score that Alex can win over the Bob？

There are three option for Alice to choose.
Take A[i], win take - dp[i+1]
Take A[i] + A[i+1], win take - dp[i+2]
Take A[i] + A[i+1] + A[i+2], win take - dp[i+3]
dp[i] equals the best outcome of these three solutions.


Complexity
Time O(N^)
Space O(N)

"""



