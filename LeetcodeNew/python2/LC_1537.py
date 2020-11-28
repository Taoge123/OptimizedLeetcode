"""
X X X X O W W W
Y Y Y   O Z Z Z

1537.Get-the-Maximum-Score
本题是一个另类的双指针题。

我们可以认为上路和下路有若干个传送门。当你在某条支路非传送门的位置时，你别无选择，只能继续前进，并将该点的数值加入该支路的score。假设你从上路走到传送门的位置时累计的分数是score1，从下路走到同一个传送门的位置时累计的分数是score2，那么你无论之后选择走哪一条路，你都会以max(score1,score2)作为新的base。也就是说，如果score1更大，那么意味着在来到传送门之前，你应该选择的是上路；反之你应该选择的是下路。在传送门之前选择上路或者下路，完全不影响你之后的选择，因为传送门的转移是没有代价的。

于是我们为上下两路设计两个双指针。当到达传送门之前时，指针各自前进，但都会在同一个传送门的位置停下来。然后综合两者分数的取较大值。然后继续分别走上下两路。

那么如何让两个指针都恰好在传送门的位置停下来呢？简单的比较两个指针对应的数值大小就行了。如果nums1[i]更小就移动i指针，反之就移动j指针。最终i和j会在同一个传送门停下来。

注意，指针移动的过程中不能对M取模。必须上下两路都走完了，再在两个score里面取最大值后再取模。

"""


class Solution:
    def maxSum(self, nums1, nums2) -> int:
        i, j = 0, 0
        x, y = 0, 0
        m, n = len(nums1), len(nums2)
        mod = 10 ** 9 + 7

        while i < m or j < n:
            if i == m:
                y += nums2[j]
                j += 1
            elif j == n:
                x += nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                x += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                y += nums2[j]
                j += 1
            elif nums1[i] == nums2[j]:
                x = max(x + nums1[i], y + nums2[j])
                y = x
                i += 1
                j += 1

        return max(x, y) % mod



