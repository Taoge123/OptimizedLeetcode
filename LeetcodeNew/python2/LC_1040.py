
"""
https://leetcode.com/problems/moving-stones-until-consecutive-ii/discuss/289357/c%2B%2B-with-picture

一步到位
rightmost - leftmost == n - 1

min
1 2 4 5 10
1 2 3 4 5 - one step

1 2 3 4 10 - cant move 10 because its the edge. you cant move the edge
2 3 4 6 10 - 1 move to 6 and move 10 to 5

解题思路
题目要求求出让石头堆连续排列的最大和最小移动步数。我们需要将最大和最小移动步数分成两个问题考虑。将总共的石头堆的数目用n表示。另外，我们首先需要做预处理，将给我们的array做个排序。

对最大移动步数，用贪心的思想，要么都移动到最左端，要么都移动到最右端。我们需要考察stones[n-2]到stones[0]和stones[n-1]到stones[1]的间距，进行比较。在这两个选择中。
选择空的position最多的那个。同时，因为一开始需要将一个endpoint做一次移动，所以需要额外加上这次步骤。

对最小移动步数，用sliding window 的方法。window的长度是n。计算每个window中，最多已经被填满的空间数量。剩下的未被填满的空间就是最小的移动数目。

需要额外注意的是，这里存在一种corner case违背了上述的结论，需要特殊处理。举例如下：
如果石头堆是1，2，3，6, 那么n是4，对于第一个window，它有一个空位置，在4， 但是6不能移动到4，这不是一个valid move，所以必须将1 移动到5，6移动到4，必须至少2步才能完成要求。

也就是说，当一个window的长度是n，它包含了连续的n-1个非空位，同时这n-1个非空位在原来石头堆的位置也是连续的，那我们就需要2步才能完成石头堆的最小移动


max

"""

class Solution:
    def numMovesStonesII(self, stones):
        nums = sorted(stones)
        n = len(nums)
        low = n
        i = 0
        for j in range(n):
            while nums[j] - nums[i] + 1 > n:
                i += 1

            already = j - i + 1
            if already == n - 1 and nums[j] - nums[i] + 1 == n - 1:
                low = min(low, 2)
            else:
                low = min(low, n - already)

        high = max(nums[n - 1] - nums[1] - n + 2, nums[n - 2] - nums[0] - n + 2)
        return [low, high]




class SolutionXingXing:
    def numMovesStonesII(self, stones):
        stones.sort()
        i, n, lower = 0, len(stones), len(stones)
        upper = max(stones[-1] - n + 2 - stones[1], stones[-2] - stones[0] - n + 2)
        for j in range(n):
            while stones[j] - stones[i] >= n: i += 1
            if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
                lower = min(lower, 2)
            else:
                lower = min(lower, n - (j - i + 1))
        return [lower, upper]


