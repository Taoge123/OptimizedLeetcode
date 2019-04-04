
"""
https://leetcode.com/problems/subarray-sum-equals-k/description/

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""

"""
Count the occurrence of all prefix sum.

I didn't notice that the array contains only 0 and 1.
As @davidluoyes suggest, we can use an array with length = N + 1,
to improve the run time.
"""
import collections

class SolutionOfficial:
    def numSubarraysWithSum(self, A, S):
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in range(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i+1] - indexes[i] - 1
                ans += w * (w+1) / 2
            return ans

        for i in range(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i-1]
            right = indexes[j+1] - indexes[j]
            ans += left * right
        return ans


class SolutionLee:
    def numSubarraysWithSum(self, A, S):
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res


"""
There are countless similar question to this, named subarrays bla bla, so solution is no-brainer.
Just look at this question for example; https://leetcode.com/problems/subarray-sum-equals-k/description/
Why do LC even ask same question over and over again ?
"""

class Solution1:
    def numSubarraysWithSum(self, A, S):
        res, sm, sums = 0, 0, collections.defaultdict(int)
        for a in A:
            sm += a
            res += sums[sm - S] + (sm == S)
            sums[sm] += 1
        return res


"""
The intuition is if S == 0, then for continous zeros split by 1, 
we can get (1+n)*n/2 different combinations to get zero where n is the number of continous zeros. 
If S > 0, then we need S ones, and for the left most one and right most one, 
we can expand the solutions with zeros, and the number of combination is (left+1) * (right+1) 
where left is the number of contious zeros before the left most one and right 
is the number of continous zerons after the right most one.

"""

class Solution2:
    def numSubarraysWithSum(self, A, S):

        idx_ones = [i for i in range(len(A)) if A[i]]
        num_zeros = list(map(len, ''.join(map(str, A)).split('1')))
        if S < 0:
            return 0
        if S == 0:
            return sum((1+i)*i//2 for i in num_zeros)
        ans = 0
        for i in range(len(idx_ones)-S+1):
            ans += (num_zeros[i]+1) * (num_zeros[i+S]+1)
        return ans


