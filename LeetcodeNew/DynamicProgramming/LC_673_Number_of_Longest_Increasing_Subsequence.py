
"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/107320/Python-DP-with-explanation-(Beats-88)

Similar question
No.549. Binary Tree Longest Consecutive Sequence II

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1,
and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

"""
"""
for those guys who are not quite familiar with this type of problem, please also check 
No.549. Binary Tree Longest Consecutive Sequence II to have a better understanding..
for each element in the array or on in the tree, they all carry three fields :
1) the maximum increasing / decreasing length ends at the current element,
2) its own value ,
3) the total number of maximum length,
and each time when we visit a element, we will use its 2) to update 1) and 3), 
the only difference is for array we use iteration while for tree we use recursion......
Also, for substring problem, we usually use only one for loop because for each index, 
we only care about the relationship between its two neighbors, while for subsequence problem, 
we use two for loops , because for each index, any other indexes can do something...
"""
"""
Intuition and Algorithm

Suppose for sequences ending at nums[i], we knew the length length[i] of the longest sequence, 
and the number count[i] of such sequences with that length.

For every i < j with A[i] < A[j], we might append A[j] to a longest subsequence ending at A[i].
It means that we have demonstrated count[i] subsequences of length length[i] + 1.

Now, if those sequences are longer than length[j], then we know we have count[i] sequences of this length. 
If these sequences are equal in length to length[j], 
then we know that there are now count[i] additional sequences to be counted of that length 
(ie. count[j] += count[i]).
"""
class Solution1:
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in xrange(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

"""
Complexity Analysis

Time Complexity: O(N^2)O(N 
2
 ) where NN is the length of nums. There are two for-loops and the work inside is O(1)O(1).

Space Complexity: O(N)O(N), the space used by lengths and counts.
"""
"""
The idea is to use two arrays len[n] and cnt[n] to record the maximum length of Increasing Subsequence 
and the coresponding number of these sequence which ends with nums[i], respectively. That is:

len[i]: the length of the Longest Increasing Subsequence which ends with nums[i].
cnt[i]: the number of the Longest Increasing Subsequence which ends with nums[i].

Then, the result is the sum of each cnt[i] while its corresponding len[i] is the maximum length.

"""

"""
If you have not solved the Longest Increasing Subsequence problem, you should do so before attempting this question. 
The approach is very similar and only requires augmentation of the DP array.

In the Longest Increasing Subsequence problem, the DP array simply had to store the longest length. 
In this variant, each element in the DP array needs to store two things: 
(1) Length of longest subsequence ending at this index and 
(2) Number of longest subsequences that end at this index. 
I use a two element list for this purpose.

In each loop as we build up the DP array, find the longest length for this index 
and then sum up the numbers at these indices that contribute to this longest length.

Here I provide two versions: (1) A slower but easier to understand version and 
(2) Much faster and optimized version

"""
class Solution2:
    def findNumberOfLIS(self, nums):

        dp, longest = [[1, 1] for i in range(len(nums))], 1
        for i, num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(curr_longest, longest)
        return sum([item[1] for item in dp if item[0] == longest])


"""
The counting step can be optimized such that we don't count from the start when we find a longer max_len. 
This improved the speed from 10% to 88%.
"""
class Solution(object):
    def findNumberOfLIS(self, nums):
        dp = [[1, 1] for i in range(len(nums))]
        max_for_all = 1
        for i, num in enumerate(nums):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    if dp[j][0] + 1 > max_len:
                        max_len = dp[j][0] + 1
                        count = 0
                    if dp[j][0] == max_len - 1:
                        count += dp[j][1]
            dp[i] = [max_len, max(count, dp[i][1])]
            max_for_all = max(max_len, max_for_all)
        return sum([item[1] for item in dp if item[0] == max_for_all])



"""
Well this question is based on problem #300 Longest Increasing Subsequence problem. 
In problem #300, dp solution is quite easy to come forward, which can be written as follow:

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp,ans = [1]* len(nums),1
        for i in range(1,len(nums)):
            dp[i]=max([dp[j]+1 for j in range(i) if nums[i]>nums[j]]+[1])
            ans=max(ans,dp[i])
        return ans
        
"""
"""
Here dp[i] represents the length of the longest subsequence in nums[:i+1] && ended with index i. 
And when I calculate array dp, I just update the result, stored in ans.

So now let's back to this problem, 
the biggest difference here is that we also need to find the number of the longest subsequence. 
A basic idea is to use another array to memorize the number, so the code is as follow:
"""

"""
Number of Longest Increasing Subsequence https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

DP Solution

1. Use the DP solution for LIS. Maintain an array called LIS and cnt. 
   LIS[i] is the length of longest subsequence ending at index i. 
   cnt[i] is the number of longest subsequences ending at index i.

2. When we find a new LIS for index i, update cnt[i] with cnt[j]. 
   Otherwise if the LIS[i] is the same as LIS[j]+1, simply add cnt[j] to cnt[i].

3. Return the sum of frequencies of the maximum LIS.
4. Time complexity is O(N^2) and Space complexity is O(N).

"""
class Solution3:
    def findNumberOfLIS(self, nums):
        if nums == []:
            return 0
        LIS, cnt = [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    if LIS[i] == LIS[j]+1:
                        cnt[i] += cnt[j]
                    elif LIS[i] < LIS[j]+1:
                        cnt[i] = cnt[j]
                        LIS[i] = LIS[j]+1
        return sum((y for x,y in zip(LIS, cnt) if x==max(LIS)))

"""
two O(n^2) dp problems back to back

dp1[j] = longest subsequence ending at index j (including j)
dp2[j] = how many different longest subsequences ending at index j
final answer sum(dp2[j] if dp1[j] == max(dp1) for j in range(n)
"""
class Solution4:
    def findNumberOfLIS(self, nums):
        dp1 = [1] * len(nums)
        for j in range(1, len(nums)):
            dp1[j] = max([1 + dp1[i] for i in range(j) if nums[i] < nums[j]] or [1])

        dp2 = [0] * len(nums)
        for j in range(len(nums)):
            dp2[j] = 1 if dp1[j] == 1 else sum(dp2[i] for i in range(j) if nums[i] < nums[j] and dp1[i] + 1 == dp1[j])

        m = max(dp1 or [0])
        return sum([dp2[i] for i in range(len(nums)) if dp1[i] == m] or [0])


"""
题目大意：
给定未排序的整数，计算最长递增子序列的个数。

解题思路：
动态规划（Dynamic Programming）

数组dp[x]表示以x结尾的子序列中最长子序列的长度

数组dz[x]表示以x结尾的子序列中最长子序列的个数

状态转移方程见代码
"""
class Solution5:
    def findNumberOfLIS(self, nums):

        maxLIS= ans = 0
        size = len(nums)
        dp = [1] * size
        dz = [1] * size
        for x in range(size):
            for y in range(0, x):
                if nums[x] > nums[y]:
                    if dp[y] + 1 > dp[x]:
                        dp[x] = dp[y] + 1
                        dz[x] = dz[y]
                    elif dp[y] + 1 == dp[x]:
                        dz[x] += dz[y]
        maxLIS = max(dp + [0])
        ans = 0
        for p, z in zip(dp, dz):
            if p == maxLIS:
                ans += z
        return ans

"""
题目大意
这个题是最长递增子序列的变种。求最长的子序列有多少个。

解题方法
首先肯定还是使用dp去求。不过，我们得对dp的数组进行改进，我们在每个位置记录当前的LIS和能得到该LIS长度的子序列数目。
在对每个位置进行计算的时候，我们都要找到该位置的LIS长度，并对能得到该长度的子序列的个数进行求和。

最后，我们需要对所有位置等于LIS长度的进行统计。
"""

class Solution6:
    def findNumberOfLIS(self, nums):

        dp, longest = [[1, 1] for _ in range(len(nums))], 1
        for i in range(1, len(nums)):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < nums[i]:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(longest, curr_longest)
        return sum([item[1] for item in dp if item[0] == longest])




