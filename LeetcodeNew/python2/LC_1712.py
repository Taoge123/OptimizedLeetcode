
"""

解法1：二分法
我们遍历第一个subarray的位置，假设截止到i。那么第二个subarray的右端点必然有一个下限j，需要满足sum[i+1:j]恰好大于sum[0:i]。
这样的j是可以用一个指针根据i单调地向右移动得到。

确定了下限，那么接下来考虑第二个subarray的右端点最远可以到哪里？假设这个位置是k。k太远的话必然会挤占第三个subarray的元素和。
所以k的极限需要满足sum[k+1:n-1]恰好大于sum[i+1:k]。对于区间和，我们必然会用前缀数组来实现，
即presum[n-1]-presum[k] >= presum[k]-presum[i]，变化一下得到我们要求最大的k，使得presum[k] <= 0.5 *(presum[n-1]+presum[i])

我们知道前缀数组presum是个单调序列。所以我们可以用二分法确定这个位置k，
也就是用upper_bound找到第一个大于0.5 *(presum[n-1]+presum[i])的位置，再往前移动一个，就是最大的、
小于等于0.5 *(presum[n-1]+presum[i])的位置。确定过了这个k，那么从j到k的所有位置，都可以是第二个区间的右端点，所以答案加上 j-i+1.

特别注意的是，以上的二分法中可能得到的k是n-1. 这样的话，第三个区间的大小变成了0，这个是不可以的。所以如果得到k==n-1的话，
我们需要把k往前再移动一位。

解法2：滑动窗口
事实上，在上面的解法中，我们可以单调地移动k来找到最大的k满足presum[k] <= 0.5 *(presum[n-1]+presum[i])。所以每固定一个i，
相应地j和k都是单调变动的。所以整体o(N)的复杂度就可以解决这题。


[X X X] {[X X X] X X X} X X X
     i       j       k
            lower  upper bound

sum[i+1:j] >= sum[0:i]
res += k - j + 1

find the largest k to satisfy below:
sum[i+1:k] <= sum[k+1:n-1]
presum[k] - presum[i] <= presum[n-1] - presum[k]
presum[k] <= 0.5 * (presum[i] + presum[n-1])

Tony
sum[:i] < sum[i+1:j] -> then we can get j, which will be the lower bound
sum[i+1:k] <= sum[k+1:] -> k will be the upper bound
presum[n-1] - presum[k] >= presum[k] - presum[i] -> then we are looking for k

"""



import bisect


class Solution:
   def waysToSplit(self, nums) -> int:
       """
       O(nlogn)/O(n)
       """
       presum = [0]
       for i in range(len(nums)):
           presum.append(presum[-1] + nums[i])
       res = 0

       for i in range(1, len(nums) - 1):
           first = presum[i]
           if 3 * first > presum[-1]: break

           low = bisect.bisect_left(presum, 2 * first, i + 1, len(nums))
           high = bisect.bisect_left(presum, (presum[-1] - first) // 2 + first + 1, low, len(nums))
           res += high - low
           res %= (10 ** 9 + 7)

       return res % (10 ** 9 + 7)



