"""
801.Minimum-Swaps-To-Make-Sequences-Increasing
对于第i轮的决策而言，是否交换A[i]和B[i]，完全取决于A[i-1]和B[i-1]是否交换以及它们所在的位置。显然这是第I类基本型的DP：第i轮的状态只与第i-1轮的状态有关，且每轮的“状态”只有两种：交换或者不交换。

我们定义changed[i]表示第i轮交换且满足递增性质的最少操作数，unchanged[i]表示第i轮不交换且仍满足递增性质的最少操作数。

我们更新unchanged[i]的时候，考虑第i-1轮是否交换这两种情况，并检验是否合法。也就说，如果第i-1轮不交换，第i轮不交换，那么需要检查是否A[i-1]<A[i] && B[i-1]<B[i]，
是的话，说明可以更新unchanged[i]=unchanged[i-1]。如果第i-1轮交换，第i轮不交换，那么需要检查是否B[i-1]<A[i] && A[i-1]<B[i]，是的话，说明可以更新unchanged[i]=changed[i-1]。

同理可以更新changed[i].

最终的答案就是最后一轮里changed和unchanged中的最大值。
"""

import math
import functools


class SolutionMemo:
    def minSwap(self, nums1, nums2) -> int:
        @functools.lru_cache(None)
        def dfs(i, prev1, prev2):
            if i >= len(nums1):
                return 0

            to_swap, no_swap = float('inf'), float('inf')

            if nums2[i] > prev1 and nums1[i] > prev2:
                to_swap = dfs(i + 1, nums2[i], nums1[i]) + 1

            if nums1[i] > prev1 and nums2[i] > prev2:
                no_swap = dfs(i + 1, nums1[i], nums2[i])

            return min(to_swap, no_swap)

        return dfs(0, -1, -1)


# DP - O(n)
class Solution:
    def minSwap(self, A, B) -> int:
        n = len(A)
        swap = [math.inf] * n
        noswap = [math.inf] * n

        swap[0] = 1
        noswap[0] = 0
        for i in range(1, n):
            # we stay last time swap this time / we swap last time stay this time
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap[i] = noswap[i - 1] + 1
                noswap[i] = swap[i - 1]

            # we stay this and last time / we swap this and last time
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                swap[i] = min(swap[i], swap[i - 1] + 1)
                noswap[i] = min(noswap[i], noswap[i - 1])

        return min(swap[-1], noswap[-1])



# DP - O(n)
# space optimiazation
class Solution2:
    def minSwap(self, A, B) -> int:
        n = len(A)
        swap = 1
        noswap = 0
        for i in range(1, n):
            # save temp copies
            pre_swap, pre_noswap = swap, noswap
            swap = no_swap = math.inf

            # we stay last time swap this time / we swap last time stay this time
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap = min(swap, pre_noswap + 1)
                noswap = min(no_swap, pre_swap)

            # we stay this and last time / we swap this and last time
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                swap = min(swap, pre_swap + 1)
                noswap = min(noswap, pre_noswap)

        return min(swap, noswap)





