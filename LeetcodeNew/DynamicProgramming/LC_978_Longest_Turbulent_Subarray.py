
"""
peaks or valleys
There are several related questions to this concept like
376. Wiggle Subsequence
324. Wiggle Sort II.

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1


Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
"""

"""
Approach 1: Sliding Window
Intuition

Evidently, we only care about the comparisons between adjacent elements. 
If the comparisons are represented by -1, 0, 1 (for <, =, >), 
then we want the longest sequence of alternating 1, -1, 1, -1, ... (starting with either 1 or -1).

These alternating comparisons form contiguous blocks. We know when the next block ends: 
when it is the last two elements being compared, or when the sequence isn't alternating.

For example, take an array like A = [9,4,2,10,7,8,8,1,9]. 
The comparisons are [1,1,-1,1,-1,0,-1,1]. The blocks are [1], [1,-1,1,-1], [0], [-1,1].

Algorithm

Scan the array from left to right. If we are at the end of a block (last elements OR it stopped alternating), 
then we should record the length of that block as our candidate answer, 
and set the start of the new block as the next element.
"""

class Solution1:
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans


"""
A subarray is turbulent if the comparison sign alternates between consecutive elements 
(ex. nums[0] < nums[1] > nums[2] < nums[3] > ... ). Looking at the structure of the array, 
this means every element of a turbulent subarray must belong to either a peak 
(A[i-2] < A[i-1] > A[i]) or a valley (A[i-2] > A[i-1] < A[i]) structure.

The algorithm works as follows. Keep track of the length of the longest run ending at index i. 
This is tracked in a variable named clen. If the last three elements form a peak or a valley, 
we can extend the previous run length by 1 (meaning clen += 1). 
Otherwise, we can no longer extend this run and need to reset clen to the length of the longest run ending at index i. 
This run length will be 1 if the previous and current elements are the same (Ex: [2,2,2]), 
or 2 if the previous and current elements differ (Ex: [2,4,6]). The answer is the length of the best run found.
"""

class Solution2:
    def maxTurbulenceSize(self, A):
        best = clen = 0

        for i in range(len(A)):
            if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
                clen += 1
            elif i >= 1 and A[i - 1] != A[i]:
                clen = 2
            else:
                clen = 1
            best = max(best, clen)
        return best



class Solution3:
    def maxTurbulenceSize(self, nums):
        dp = [1] * len(nums)  # the shortest length is 1

        for i in range(len(nums)):
            if i >= 2:  # we update dp once all 3 numbers satisfy the turbulent condition
                if nums[i - 2] < nums[i - 1] > nums[i] or nums[i - 2] > nums[i - 1] < nums[i]:
                    dp[i] = dp[i - 1] + 1
                    continue
            if i >= 1:  # if two numbers are not the same, update dp to 2
                if nums[i - 1] != nums[i]:
                    dp[i] = 2
            #This condition can be removed
            # if nums[i - 1] == nums[i]:  # don't touch it if two numbers are the same
            #     continue

        return max(dp)


"""
题意分析：
找一个数组的子串，使得其满足任意 (A[i]-A[i+1]) * (A[i-1]-A[i]) < 0

思路分析：
这里采用双指针法，用j-i+1代表子串的长度，当满足(A[j-1]-A[j])*(A[j]-A[j+1]) < 0时j向右移动。
单独处理了数组中只有一个元素的情况！
"""
class Solution4:
    def maxTurbulenceSize(self, A):
        if len(A) <= 2: return len(A)
        # 全是相同元素
        if A.count(A[0]) == len(A):
            return 1
        i,j = 0,1
        res = 1
        while j < len(A)-1:
            if (A[j-1]-A[j])*(A[j]-A[j+1]) < 0:
                j += 1
            else:
                res = max(res, j-i+1)
                i,j = j, j+1
        return max(res, j-i+1)


class Solution5:
    def maxTurbulenceSize(self, A):

        mx = 1  # at least 1
        asc, desc = 1, 1  # max len of ascending and descending ending at idx i

        for i in range(1, len(A)):
            old = asc
            asc = 1 if A[i] <= A[i - 1] else desc + 1
            desc = 1 if A[i] >= A[i - 1] else old + 1
            mx = max(mx, max(asc, desc))
        return mx






