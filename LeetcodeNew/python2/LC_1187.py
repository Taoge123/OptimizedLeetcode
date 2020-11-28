"""
801. Minimum Swaps To Make Sequences Increasing
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1187.Make-Array-Strictly-Increasing

考虑到本题给予了一种替换操作的“权力”，从动态规划的套路经验可以尝试，以使用这种“权力”的次数作为状态。
因此我们设计dp[i][k]表示：如果我们可以使用k次替换操作使得前i个元素严格递增，此时第i个元素可以选择的最小值。
注意，这个dp状态变量的“值”的定义和我们以往套路不同的地方在于，并没有照搬题目的问题"minimum operations"，
因为操作数已经用dp的下标k标示了。我们之所以选择“此时第i个元素可以选择的最小值”作为值，是有点贪心的思想。
因为我们想要使得这个递增序列能够接的更长的话，必然会让第i个元素尽可能地小。

我们如何更新dp[i][k]呢，显然突破口就在于第i个元素是否使用替换操作的“权力”。

如果第i个元素我们不替换。那么显然要求前i-1个元素用k次操作已经保持递增，并且arr1[i]能够顺利地再接上去。即

if (arr1[i] > dp[i-1][k])
  dp[i][k] = arr1[i]
如果第i个元素我们做了替换。那么显然要求前i-1个元素用k-1次操作已经保持递增，并且能把arr1[i]替换后的数再顺利地再接上去。
那么我们想替换成什么数呢？显然应该是arr2里面恰好比dp[i-1][k-1]大一点点的那个数。注意下面的代码只在k>=1的时候有效。

auto iter = upper_bound(arr2.begin(), arr2.end(), dp[i-1][k-1]);
if (iter!=arr2.end())
  dp[i][k] = *iter;
以上两种情况都需要考虑。因此我们是用两个值来试图更新dp[i][k]，取较小的那个。如果两种情况都无法满足，
即都无法更新dp[i][k]，那么我们会默认dp[i][k]为无穷大，表示“我们无法使用k次替换操作使得前i个元素严格递增”。


Similar to Longest-increasing-sub-sequence problem.
Record the possible states of each position and number of operations to get this state.
When we check i-th element in the arr1, dp record the possible values we can place at this position, and the number of operations to get to this state.
Now, we need to build dp for (i+1)-th position, so for (i+1)-th element,
if it's larger than the possible state from i-th state, we have two choices:
1, keep it so no operation needs to be made.
2, choose from arr2 a smaller element that is larger than i-th element and add one operation.
If it's not larger than the i-th state, we definitely need to make a possible operation.

"""

import collections
import bisect
from functools import lru_cache

"""
dp[i][k] : arr1[1:i] using k operations to make them strictly increasing,
            the minimum value of arr[i]

dp[i-1][k] < arr1[i] => dp[i][k] = arr1[i]
dp[i-1][k-1] < replace(arr1[i]) => dp[i][k] = replace(arr1[i])

"""

"""

1187.Make-Array-Strictly-Increasing
考虑到本题给予了一种替换操作的“权力”，从动态规划的套路经验可以尝试，以使用这种“权力”的次数作为状态。因此我们设计dp[i][k]表示：
如果我们可以使用k次替换操作使得前i个元素严格递增，此时第i个元素可以选择的最小值。注意，这个dp状态变量的“值”的定义和我们以往套路不同的地方在于，
并没有照搬题目的问题"minimum operations"，因为操作数已经用dp的下标k标示了。我们之所以选择“此时第i个元素可以选择的最小值”作为值，是有点贪心的思想。
因为我们想要使得这个递增序列能够接的更长的话，必然会让第i个元素尽可能地小。

我们如何更新dp[i][k]呢，显然突破口就在于第i个元素是否使用替换操作的“权力”。

如果第i个元素我们不替换。那么显然要求前i-1个元素用k次操作已经保持递增，并且arr1[i]能够顺利地再接上去。即

if (arr1[i] > dp[i-1][k])
  dp[i][k] = arr1[i]
如果第i个元素我们做了替换。那么显然要求前i-1个元素用k-1次操作已经保持递增，并且能把arr1[i]替换后的数再顺利地再接上去。那么我们想替换成什么数呢？
显然应该是arr2里面恰好比dp[i-1][k-1]大一点点的那个数。注意下面的代码只在k>=1的时候有效。

auto iter = upper_bound(arr2.begin(), arr2.end(), dp[i-1][k-1]);
if (iter!=arr2.end()) 
  dp[i][k] = *iter; 
以上两种情况都需要考虑。因此我们是用两个值来试图更新dp[i][k]，取较小的那个。如果两种情况都无法满足，即都无法更新dp[i][k]，那么我们会默认dp[i][k]为无穷大，
表示“我们无法使用k次替换操作使得前i个元素严格递增”。


dp[i][j] : for the index of j in arr1, if we changed i times and then maintain a strickly increasing array from 0 to j , 
the minimal value for index of j is dp[i][j](we want to make the front numbers as small as possible); 
if dp[i][j] = Integer.MAX_VALUE, means there is no way to maintain a strictly increasing array with i times from 0 to j. 
For the last index arr1.length - 1, return the smallest i we can get since it means the minimal steps of change for the whole arr1.
"""




class SolutionTony:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        n = len(arr1)
        if n == 1:
            return 0
        dp = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
        arr2.sort()

        dp[0][0] = float('-inf')
        for i in range(1, n + 1):
            for k in range(i + 1):
                if arr1[i - 1] > dp[i - 1][k]:
                    dp[i][k] = arr1[i - 1]
                if k > 0:
                    idx = bisect.bisect_right(arr2, dp[i - 1][k - 1])
                    if idx < len(arr2):
                        dp[i][k] = min(dp[i][k], arr2[idx])

                    if i == n and dp[i][k] != float('inf'):
                        return k
        return -1


class Solution:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        dp = {-1: 0}
        arr2 = sorted(arr2)
        for num in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if num > key:
                    tmp[num] = min(tmp[num], dp[key])
                replace = bisect.bisect_right(arr2, key)
                if replace < len(arr2):
                    tmp[arr2[replace]] = min(tmp[arr2[replace]], dp[key] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1


class Solution2:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        arr2 = sorted(set(arr2))
        changes = self.dfs(tuple(arr1), tuple(arr2), 0, float('-inf'))
        return changes if changes != float('inf') else -1

    @lru_cache(None)
    def dfs(self, arr1, arr2, i, prev):
        if i >= len(arr1):
            return 0
        j = bisect.bisect_right(arr2, prev)
        swap = 1 + self.dfs(arr1, arr2, i + 1, arr2[j]) if j < len(arr2) else float('inf')
        noswap = self.dfs(arr1, arr2, i + 1, arr1[i]) if arr1[i] > prev else float('inf')
        return min(swap, noswap)


class Solution22:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        l = sorted(set(arr2))

        @lru_cache(None)
        def min_changes(i, cur_min):
            if i >= len(arr1):
                return 0

            j = bisect.bisect_right(l, cur_min)
            swap_cost = 1 + min_changes(i + 1, l[j]) if j < len(l) else float("+inf")
            keep_cost = min_changes(i + 1, arr1[i]) if arr1[i] > cur_min else float("+inf")

            return min(swap_cost, keep_cost)

        changes = min_changes(0, float("-inf"))
        return changes if changes != float("+inf") else -1



a = Solution2()
arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]
a.makeArrayIncreasing(arr1, arr2)

