
"""
https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235235/C%2B%2BJava-with-picture-prefixed-sliding-window


Given an array A of positive integers, call a (contiguous, not necessarily distinct)
subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.



Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""

"""
Intuition:
Write a helper using sliding window,
to get the number of subarrays with at most K distinct elements.
Then f(exactly K) = f(atMost K) - f(atMost K-1).

Of course, you can merge 2 for loop into ones, if you like.

Time Complexity:
O(N)
"""
import collections

class SolutionLee:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res


class Solution2:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        freq = {}
        start = 0
        start_k = 0
        res = 0
        for i, x in enumerate(A):
            freq[x] = freq.get(x, 0) + 1
            if len(freq) == K + 1:
                # remove the distinct at start_k, move start_k, start
                del freq[A[start_k]]
                start_k += 1
                start = start_k
            if len(freq) == K:
                # update start_k and res (Notice: K >= 1)
                while freq[A[start_k]] > 1:
                    freq[A[start_k]] -= 1
                    start_k += 1
                res += start_k - start + 1
        return res


"""
This idea is to find the basic valid sub-array and find all its derived ones. 
If a valid sub-array A1 appears, code will push the right bound to reach 
its all derived sub-array (group) by checking the next number is in the dictionary or not; 
code will also cut number(s) from the left side, if the cutting does not change the validity, 
there is another group of sub-arrays (right_bound - current_index) exists.
The good point is that the right bound will not back trace, also does the left bound. 
So the time complexity is O(N).
"""

class Solution3:
    def subarraysWithKDistinct(self, A, K):
        s = collections.Counter()
        l = r = ans = 0
        for i,num in enumerate(A):
            s[num] += 1
            if s[num] == 1 and len(s) == K:
                while r < len(A) and A[r] in s:
                    r += 1
                while len(s) == K:
                    ans += r-i
                    s[A[l]] -= 1
                    if s[A[l]] == 0: del s[A[l]]
                    l += 1
        return ans


"""
关键就在于这个思路，定义f(k)表示数组A中至多包含K个不同的数的子串个数
那么题目所求包含恰好k个不同的数的子串个数则可表示为f(k) - f(k-1)

显然，f(k)的计算是非常简单的，双指针思路如下：
对于每个A[j]，计算以A[j]结尾的最多包含k个不同的数的子串个数，然后求和即可。
"""

class Solution4:
    def subarraysWithKDistinct(self, A, K):
        def solve(A, K):
            i = 0
            res = 0
            d = collections.Counter()
            for j in range(len(A)):
                d[A[j]] += 1
                if d[A[j]] == 1: K -= 1
                while K < 0:
                    d[A[i]] -= 1
                    if d[A[i]] == 0: K += 1
                    i += 1
                res += j - i + 1
            return res
        return solve(A, K) - solve(A, K-1)


