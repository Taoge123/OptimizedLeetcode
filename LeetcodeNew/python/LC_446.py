"""
https://github.com/wisdompeak/LeetCode/tree/master/Hash/446.Arithmetic-Slices-II-Subsequence

好，既然决定要用DP了，那么首先就要确定dp数组的定义了，刚开始我们可能会考虑使用个一维的dp数组，
然后dp[i]定义为范围为[0, i]的子数组中等差数列的个数。定义的很简单，OK，
但是基于这种定义的状态转移方程却十分的难想。我们想对于(0, i)之间的任意位置j，
如何让 dp[i] 和 dp[j] 产生关联呢？是不是只有 A[i] 和 A[j] 的差值diff，
跟A[j]之前等差数列的差值相同，才会有关联，所以差值diff是一个很重要的隐藏信息Hidden Information，
我们必须要在dp的定义中考虑进去。所以一维dp数组是罩不住的，必须升维，但是用二维dp数组的话，
差值diff那一维的范围又是个问题，数字的范围是整型数，所以差值的范围也很大，为了节省空间，
我们建立一个一维数组dp，数组里的元素不是数字，而是放一个HashMap，建立等差数列的差值和当前位置之前差值相同的数字个数之间的映射。
我们遍历数组中的所有数字，对于当前遍历到的数字，又从开头遍历到当前数字，计算两个数字之差diff，
如果越界了不做任何处理，如果没越界，我们让dp[i]中diff的差值映射自增1，
因为此时A[i]前面有相差为diff的A[j]，所以映射值要加1。然后我们看dp[j]中是否有diff的映射，
如果有的话，说明此时相差为diff的数字至少有三个了，已经能构成题目要求的等差数列了，
将dp[j][diff]加入结果res中，然后再更新dp[i][diff]，这样等遍历完数组，res即为所求。

我们用题目中给的例子数组 [2，4，6，8，10] 来看，因为2之前没有数字了，所以我们从4开始，
遍历前面的数字，是2，二者差值为2，那么在dp[1]的HashMap就可以建立 2->1 的映射，
表示4之前有1个差值为2的数字，即数字2。那么现在i=2指向6了，遍历前面的数字，第一个数是2，
二者相差4，那么在dp[2]的HashMap就可以建立 4->1 的映射，第二个数是4，二者相差2，
那么先在dp[2]的HashMap建立 2->1 的映射，由于dp[1]的HashMap中也有差值为2的映射，
2->1，那么说明此时至少有三个数字差值相同，即这里的 [2 4 6]，我们将dp[1]中的映射值加入结果res中，
然后当前dp[2]中的映射值加上dp[1]中的映射值。这应该不难理解，比如当i=3指向数字8时，
j=2指向数字6，那么二者差值为2，此时先在dp[3]建立 2->1 的映射，
由于dp[2]中有 2->2 的映射，那么加上数字8其实新增了两个等差数列 [2,4,6,8] 和 [4,6,8]，
所以结果res加上的值就是 dp[j][diff]，即2，并且 dp[i][diff] 也需要加上这个值，
才能使得 dp[3] 中的映射变为 2->3 ，后面数字10的处理情况也相同，这里就不多赘述了，
最终的各个位置的映射关系如下所示：


2     4     6     8     10
     2->1  4->1  6->1  8->1
           2->2  4->1  6->1
                 2->3  4->2
                       2->4


最终累计出来的结果是跟上面红色的数字相关，分别对应着如下的等差数列：


2->2：[2,4,6]

2->3：[2,4,6,8]    [4,6,8]

4->2：[2,6,10]

2->4：[2,4,6,8,10]    [4,6,8,10]    [6,8,10]

"""

import collections
import functools


class SolutionMemo:
    def numberOfArithmeticSlices(self, nums) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, diff):
            res = 0
            for j in table[i][diff]:
                res += 1 + dfs(j, diff)
            return res

        table = [collections.defaultdict(list) for i in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                table[i][nums[j] - nums[i]].append(j)

        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res += dfs(j, nums[j] - nums[i])
        return res


class SolutionMemoTLE:
    def numberOfArithmeticSlices(self, nums) -> int:

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i, diff):
            if i >= n - 1:
                return 0
            nes = 0
            for j in range(i + 1, n):
                next_diff = nums[j] - nums[i]
                if diff == next_diff:
                    nes += 1 + dfs(j, next_diff)
            return nes

        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res += dfs(j, nums[j] - nums[i])
        return res


class Solution:
    def numberOfArithmeticSlices(self, A) -> int:

        res = 0
        dp = [collections.defaultdict(int) for a in A]
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    res += dp[j][diff]
        return res



class SolutionSlow:
    def numberOfArithmeticSlices(self, A) -> int:

        n = len(A)
        dp = collections.defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[(i, diff)] += dp[(j, diff)] + 1
                res += dp[(j, diff)]
        return res



A = [2, 4, 6, 8, 10]
a = Solution()
print(a.numberOfArithmeticSlices(A))




