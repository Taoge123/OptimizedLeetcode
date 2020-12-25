"""
1691.Maximum-Height-by-Stacking-Cuboids
解法1
因为题目允许任意旋转长方体，我们尝试将每个长方体的六个旋转变种都考虑进来。这样总共有6n个cuboids。

因为从下往上堆叠的次序必须是按照长度递减的，所以我们自然会将所有的6n个cuboids按照长度降排列。那么对于长度相同的长方体呢？我们可以再按宽度降序排列；对于宽度也相同的长方体，按照高度降序排列。这样，符合要求的堆叠方案必然是这个序列的一个subsequece。注意，并不是说这个序列的任何一个subsequence都是符合要求的堆叠方案。

接下来，从这个降序序列里面找总高度最大的序列，类似于求LIS的做法。令dp[i]表示以i为最上层长方体的堆叠总高度。

for (int i=0; i<6*n; i++)
{
  dp[i] = height[i];
  for (int j=0; j<n; j++)
    if (length[j]<=length[j] && width[j]<=width[i] && height[j]<=height[i])
      dp[i] = max(dp[i], dp[j]+height[i]);
}
但此时有一个问题，如何保证我们选取的这个LIS里不含有同一个长方体的若干个变体呢？事实上，通常情况下这个并不会发生，因为同一个长方体c的任何两个变体c1和c2，不可能实现c1在c2上的顺利堆叠。举个例子，令长方体的三条边为L>M>S，那么我们按照高的选择分类为三种：

c1: base (L,M), height (S)
c2: base (L,S), height (M)
c3: base (M,S), height (L)
如果按照高度的约束来看，这三种变体的堆叠只能是c1在c2上、c2在c3上。但是从底面积的约束来看，必须是c3在c2上、c2在c1上。这个是矛盾的。所以在两层循环里，我们通常是无法找到一对符合条件i和j恰好是同一个长方体的变体。

但是以上有个问题，就是如果M==S的话，那么c1和c2就长得完全一样，那么仍有可能动态规划的时候会把c1放在c2之上。解决方案是给每个长方体带上原始的编号信息，并作为第四个下标参与排序。这样的话，两个相同的长方体变种一定会相邻，并且在探索i和j配对的时候通过这个编号信息(&&idx[i]!=idx[j])来排除这样的配对。

解法2
我们考虑一个合法的堆叠A(a1,a2,a3)可以放在B(b1,b2,b3)之上，即a1<=b1, a2<=b2, a3<=b3. 那么可以证明max(a1,a2,a3) <= max(b1,b2,b3), mid(a1,a2,a3) <= mid(b1,b2,b3), min(a1,a2,a3) <= min(b1,b2,b3). 第一个和第三个结论显然，第二个结论通过反正：如果不是的话，是无法同时存在条件中的三个不等式的。

于是我们发现，只要A可以放在B之上，那么A的变体(min(a1,a2,a3), mid(a1,a2,a3), max(a1,a2,a3))也一定可以放在B的变体(min(b1,b2,b3), mid(b1,b2,b3), max(b1,b2,b3))之上。所以对于任何一个合法的堆叠序列，我们都可以将其中的每个长方体变化为：最短边作为length、中等边作为width、最长边作为height。变化之后，原序列依然是一个合法的堆叠，而且总高度只增不减。所以重新考虑原题，最优的解一定是把每个长方体的最长边作为height。所以对于每种长方体，我们只需要选择如上的这一种变体即可，我们能够保证：一定有一个合法的堆叠序列，并且得到的序列总高度是最高的。

于是我们将所有n个长方体经过变形后（将最短边作为length、中等边作为width、最长边作为height）按照长度和宽度进行降序排列。接下来按照解法1的思想，用N^2的LIS DP方法找到最高的总堆叠高度。因为每个长方体我们只放了一个变种，所以不需要记录idx来避免同一个长方体的duplicate。

"""

import functools


class Solution:
    def maxHeight(self, cuboids) -> int:
        cuboids = sorted((sorted(x, reverse=True) for x in cuboids), reverse=True)

        # print(cuboids)
        @functools.lru_cache(None)
        def dfs(i, h, l, w):
            """Return max heights of stacking cuboids[i:]."""
            if i == len(cuboids):
                return 0  # no cuboids left
            hi, li, wi = cuboids[i]
            if hi <= h and li <= l and wi <= w:
                return max(hi + dfs(i + 1, hi, li, wi), dfs(i + 1, h, l, w))
            else:
                return dfs(i + 1, h, l, w)

        return dfs(0, float('inf'), float('inf'), float('inf'))



