
"""
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/166159/Clear-O(n)-Python
https://www.geeksforgeeks.org/maximum-sum-two-non-overlapping-subarrays-of-given-size/

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).

"""

"""
/**
 * High level: calculate left local max subarray with size k from left to right and right local max subarray
 * with size k from right to left. And use sliding window to do 3-sum from left to right
 *
 * Step 1: calculate prefix sum dp array
 * Step 2: calculate left local max subarray with size k
 * dp1: leftMaxPos[i] represents max subarray STARTING index with size k starting from i in the range [0, i - k]
 * dp2: rightMaxPos[i] represents max subarray STARTING index with siz k starting from i in the range [i, n - 1]
 *
 * Step 3: traverse from k to n - 2k, keep a window with size k, calculate "3sum" in every iteration, and return
 * the max one.
 * eg: for index i, we have max subarray starting index (leftMaxPos[i - 1]) on the left side of current window,
 * we also have max subarray starting index (rightMaxPos[i + k]) on the right side of current window. Then we are
 * able to find max 3sum by traversing all possible 3sums
 * */
"""
"""
The question asks for three non-overlapping intervals with maximum sum of all 3 intervals. 
If the middle interval is [i, i+k-1], where k <= i <= n-2k, the left interval has to be in subrange [0, i-1], 
and the right interval is from subrange [i+k, n-1].

So the following solution is based on DP.

posLeft[i] is the starting index for the left interval in range [0, i];
posRight[i] is the starting index for the right interval in range [i, n-1]; 
Then we test every possible starting index of middle interval, i.e. k <= i <= n-2k, and we can get the corresponding left and right max sum intervals easily from DP. And the run time is O(n).

Caution. In order to get lexicographical smallest order, when there are two intervals with equal max sum, 
always select the left most one. So in the code, the if condition is ">= tot" for right interval 
due to backward searching, and "> tot" for left interval. Thanks to @lee215 for pointing this out!
"""
"""
This solution is so cool and can be generally used to solve cut problems. Understand this is pretty useful and thanks very much for that. But in coding, you can use just one index to represent all windows and use tuple assignment in Python could make code much shorter, which can make this solution not that overwhelming .
Please see my code for reference.

oneWinSum, twoWinSum, threeWinSum, one, two, three = sum(nums[:k]), sum(nums[k:k2]), sum(nums[2k:3k]), [0], [0, k], [0, k, k2]
mone, mtwo, mthree = oneWinSum, oneWinSum + twoWinSum, oneWinSum + twoWinSum + threeWinSum
for i in range(1, len(nums) - k * 3 + 1):
oneWinSum, twoWinSum, threeWinSum = oneWinSum + nums[i+k-1] - nums[i-1], twoWinSum + nums[i+2k-1] - nums[i+k-1],threeWinSum + nums[i+3k-1] - nums[i+2*k-1]
if oneWinSum > mone:
mone, one = oneWinSum, [i]
if mone + twoWinSum > mtwo:
mtwo, two = mone + twoWinSum, one + [i+k]
if mtwo + threeWinSum > mthree:
mthree, three = mtwo + threeWinSum, two + [i + 2 * k]
return three"""

"""
A greedy solution using three sliding windows where you keep track of the best indexes/sums as you go.

O(n) time: Since we're only going through the list once and using no complex operations, this is O(n).
O(1) space: Just a fixed set of temp vars. We don't need the extra arrays that the DP solutions have.
"""
import sys

class Range:
    def maxSumOfThreeSubarrays(self, nums, k):
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k * 2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k * 2])
        seqThreeSum = sum(nums[k * 2:k * 3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k * 2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]

            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq


"""
1. Build sums array for each k size subarray summation
2. Compute maximum and index for [0, i] and [j, len(sums)-1]
3. For each value at i in sums, check the sums of sums[i] + dp_front[i-k] + dp_back[i+k] 
   and update maximum and index
"""

class Solution2:
    def maxSumOfThreeSubarrays(self, nums, k):
        if len(nums) < 3 * k: return []
        sums = [0] * (len(nums) - k + 1)
        sums[0] = sum(nums[:k])
        for i in range(1, len(nums)-k+1):
            sums[i] = sums[i-1] + nums[i+k-1] - nums[i-1]

        dp_front = [[0, 0] for _ in range(len(sums))]
        dp_back = [[0, 0] for _ in range(len(sums))]
        dp_front_max, dp_back_max = -sys.maxint, -sys.maxint
        for i in range(len(sums)):
            if sums[i] > dp_front_max:
                dp_front[i] = [sums[i], i]
                dp_front_max = sums[i]
            else:
                dp_front[i] = dp_front[i-1]
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] > dp_back_max:
                dp_back[i] = [sums[i], i]
                dp_back_max = sums[i]
            else:
                dp_back[i] = dp_back[i+1]

        ret, maxval = [], -sys.maxint
        for i in range(k, len(sums) - k):
            if sums[i] + dp_front[i - k][0] + dp_back[i + k][0] > maxval:
                ret = [dp_front[i - k][1], i, dp_back[i + k][1]]
                maxval = sums[i] + dp_front[i - k][0] + dp_back[i + k][0]
        return ret


"""
I must admit that those start and end points of for loops are really disgusting due to problem :)
We first calculate sum(nums[i:i + k]), sum of one single subarray, for suitable indexes and store them in "single" dictionary.
After that from right to left we match next max subarray for each suitable subarray and store two subarrays information in "double" dictionary.
Finally, we match next max subarray couple (double) for each suitable subarray and change result if current subarray + couple bigger than result (sm).
Return result
"""
class Solution3:
    def maxSumOfThreeSubarrays(self, nums, k):
        single, double, sm, n, cur = {}, {}, 0, len(nums), sum(nums[:k - 1])
        for i in range(k - 1, n):
            cur += nums[i]
            single[i - k + 1] = cur
            cur -= nums[i - k + 1]
        cur = n - k, single[n - k]
        for i in range(n - k, k * 2 - 1, -1):
            if single[i] >= cur[1]:
                cur = i, single[i]
            double[i - k] = cur[1] + single[i - k], i - k, cur[0]
        cur = double[n - 2 * k]
        for i in range(n - 2 * k, k - 1, -1):
            if double[i][0] >= cur[0]:
                cur = double[i]
            if single[i - k] + cur[0] >= sm:
                sm, res = single[i - k] + cur[0], [i - k, cur[1], cur[2]]
        return res

"""
1, Convert nums to windws
That is, convert array of numbers into array of sum of windows. For example:

    nums = [1, 2, 3], w_size = 2
    windows = [1 + 2, 2 + 3] = [3, 5]
So the problem now is to choose 3 values from the window array and the difference of the indexes of these values must >=k

2, Define 3 arrays
    take1[i]= biggest result we can get if only take 1 value from win[0] ... win[i]
    take2[i]= biggest result we can get if only take 2 values from win[0] ... win[i]
    take3[i]= biggest result we can get if only take 3 values from win[0] ... win[i]
3, Update 3 arrays dynamically
    For take1, because only 1 window can be taken, so we just choose the current value or the previous value, depends on which one is bigger.
    So take1[i] = max(take1[i - 1], win[i])

    For take2, we need to select 2 windows, so we can either keep the previous selection, or we can take the current window and the biggest window in [0 ~ i - k], which is take1[i - k].
    So take2[i] = max(take2[i - 1], win[i] + take1[i - k])

    Same idea, take3[i] = max(take3[i - 1], win[i] + take2[i - k])

4, Remember the selection
    If the problem is to return the biggest value, then step1~3 would be suffice, but we need to return the selection, so we need to remember not only the biggest value but also the index of selected window.

    Just modify to array to be:

        take = [value, [indexes]]
    and when we update the value, we update the [indexes] too.
"""
class Solution4:
    def maxSumOfThreeSubarrays(self, nums, k):
        subsum = sum(nums[:k])
        take1 = [(0, ()) for _ in range(len(nums))]
        take2 = [(0, ()) for _ in range(len(nums))]
        take3 = [(0, ()) for _ in range(len(nums))]

        for i in range(k - 1, len(nums)):
            subsum = subsum - nums[i - k] + nums[i]

            # update take 1
            if subsum > take1[i - 1][0]:
                take1[i] = (subsum, (i - k + 1,))
            else:
                take1[i] = take1[i - 1]

            # update take 2
            if subsum + take1[i - k][0] > take2[i - 1][0]:
                newval = subsum + take1[i - k][0]
                newidx = take1[i - k][1] + (i - k + 1,)
                take2[i] = (newval, newidx)
            else:
                take2[i] = take2[i - 1]

            # update take 3
            if subsum + take2[i - k][0] > take3[i - 1][0]:
                newval = subsum + take2[i - k][0]
                newidx = take2[i - k][1] + (i - k + 1,)
                take3[i] = (newval, newidx)
            else:
                take3[i] = take3[i - 1]

        return take3[-1][1]


"""
three windows size==k:w1,w2,w3,can just keep 3 adjacent windows move.
update maxw1 if w1>maxw1-> update maxw2 if maxw1+w2>maxw2->update maxw3 if maxw2+w3>maxw3
"""
class SolutionSlidingWindow:
    def maxSumOfThreeSubarrays(self,nums, k):
        n=len(nums)
        w1,w2,w3=sum(nums[i] for i in range(k)),sum(nums[i] for i in range(k,2*k)),sum(nums[i] for i in range(2*k,3*k))
        mw1,mw2,mw3=w1,w1+w2,w1+w2+w3
        mw1index,mw2index,mw3index=[0],[0,k],[0,k,2*k]#mw1,mw2,mw3's index.
        for i in range(1,n-3*k+1):#last index for w1 window will be n-3k
            w1+=nums[i-1+k]-nums[i-1]
            w2+=nums[i-1+2*k]-nums[i-1+k]
            w3+=nums[i-1+3*k]-nums[i-1+2*k]
            if w1>mw1:
                mw1,mw1index=w1,[i]
            if mw1+w2>mw2:
                mw2,mw2index=mw1+w2,mw1index+[i+k]
            if mw2+w3>mw3:
                mw3,mw3index=mw2+w3,mw2index+[i+2*k]
        return mw3index

"""
解题方法
看题目的数据知道需要用O(N)的解法，另外优化最值问题一般都是DP。具体怎么做呢？

把三个数组分别看做左侧，中间，右侧的数组。我们指定了中间数组的位置之后，就在这个位置左侧和右侧分别求一个和最大的子数组，
然后三个数组和相加，就得到了总体最大的和。

使用sums数组保存到每个位置的累积和。这样做的好处是我们可以直接根据两个位置相减求出子数组的和。另外需要两个DP数组left和right。

left[i]表示在区间[0, i]范围内长度为k且和最大的子数组的起始位置

right[i]表示在区间[i, n - 1]范围内长度为k且和最大的子数组的起始位置

left的求法是从左到右遍历，right的求法是从右到左遍历。遍历刚开始的K个位置内由于子数组长度小于k，所以left的值是0，right的值是N - k，
代表的是能取子区间的边缘情况下索引。更新过程也不难，就是和已有的子数组最大和比较，然后更新索引位置就行了。

求出了每个位置左边和右边的长度为k的子数组之后，需要再次用一个窗口遍历数组，这个窗口就是我们中间的数组。这就成为了在确定中间数组位置的情况下，
左边和右边的最大数组和问题，因为我们已经知道了left和right，那么就相当于查表得到位置。

这个题对sums是添加了头部0的，这样的好处是求到目前为止的和的时候可以直接从nums第0个数组开始找前面一个sums+当前的数字。

这个题最难的地方应该在于铺天盖地的索引值吧……反正我是被搞晕了。

时间复杂度是O(N)，空间复杂度是O(N)。
"""
class Solution5:
    def maxSumOfThreeSubarrays(self, nums, k):
        N = len(nums)
        sums = [0]
        left = [0] * N
        right = [N - k] * N
        mx = 0
        res = [0, 0, 0]
        for i, num in enumerate(nums):
            sums.append(sums[-1] + num)
        total = sums[k] - sums[0]
        for i in range(k, N):
            if sums[i + 1] - sums[i - k + 1] > total:
                left[i] = i - k + 1
                total = sums[i + 1] - sums[i - k + 1]
            else:
                left[i] = left[i - 1]
        total = sums[N] - sums[N - k]
        for j in range(N - k - 1, -1, -1):
            if sums[j + k] - sums[j] >= total:
                right[j] = j
                total = sums[j + k] - sums[j]
            else:
                right[j] = right[j + 1]
        for i in range(k, N - 2 * k + 1):
            l, r = left[i - 1], right[i + k]
            total = (sums[i + k] - sums[i]) + (sums[l + k] - sums[l]) + (sums[r + k] - sums[r])
            if total > mx:
                mx = max(mx, total)
                res = [l, i, r]
        return res


"""
题目大意：
给定正整数数组nums，计算其中不想交的3段子数组的最大和。每段子数组的长度为k。

解题思路：
预处理，时间复杂度O(n)

构造K项和数组sums，sums[i] = sum(nums[i - k + 1 .. i])

从左向右构造K项和最大值及其下标数组maxa，其元素记为va, ia

从右向左构造K项和最大值及其下标数组maxb，其元素记为vb, ib

在[k, nsize - k)范围内枚举中段子数组的起点x

则3段子数组和 = sums[x] + va + vb
"""

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        size = len(nums)
        nsize = size - k + 1
        sums = [0] * nsize
        maxa = [0] * nsize
        maxb = [0] * nsize
        total = 0

        for x in range(size):
            total += nums[x]
            if x >= k - 1:
                sums[x - k + 1] = total
                total -= nums[x - k + 1]

        maxn, maxi = 0, 0
        for x in range(nsize):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxa[x] = (maxn, maxi)

        maxn, maxi = 0, nsize - 1
        for x in range(nsize - 1, -1, -1):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxb[x] = (maxn, maxi)

        ansn, ansi = 0, None
        for x in range(k, nsize - k):
            va, ia = maxa[x - k]
            vb, ib = maxb[x + k]
            if sums[x] + va + vb > ansn:
                ansn = sums[x] + va + vb
                ansi = [ia, x, ib]

        return ansi



