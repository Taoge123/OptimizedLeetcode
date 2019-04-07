"""

373. Find K Pairs with Smallest Sums
378. Kth Smallest Element in a Sorted Matrix
668. Kth Smallest Number in Multiplication Table
719. Find K-th Smallest Pair Distance
786. K-th Smallest Prime Fraction

https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378
https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm

A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.
"""
import heapq
import bisect

class Solution1:
    def kthSmallestPrimeFraction(self, primes, K):
        from fractions import Fraction
        def under(x):
            # Return the number of fractions below x,
            # and the largest such fraction
            count = best = 0
            i = -1
            for j in range(1, len(primes)):
                while primes[i+1] < primes[j] * x:
                    i += 1
                count += i+1
                if i >= 0:
                    best = max(best, Fraction(primes[i], primes[j]))
            return count, best

        # Binary search for x such that there are K fractions
        # below x.
        lo, hi = 0.0, 1.0
        while hi - lo > 1e-9:
            mi = (lo + hi) / 2.0
            count, best = under(mi)
            if count < K:
                lo = mi
            else:
                ans = best
                hi = mi

        return ans.numerator, ans.denominator


"""
Algorithm

In Python, storing the fractions will be done with a tuple (fraction, i, j), 
representing the fraction fraction = primes[i] / primes[j]. 
When we use this fraction, we will push the next fraction (primes[i+1] / primes[j], i+1, j) 
onto the heap, assuming that the next fraction is valid (ie., that i+1 < j).

In Java, storing the fractions will be done as an int[2] of {i, j} (indexes, not elements of A), 
and we use a custom comparator to ensure the right elements are pq.offered correctly.

With this detail out of the way, the solution is straightforward.
"""
class Solution(object):
    #Note - this solution may TLE.
    def kthSmallestPrimeFraction(self, A, K):
        pq = [(A[0] / float(A[i]), 0, i) for i in range(len(A) - 1, 0, -1)]

        for _ in range(K-1):
            frac, i, j = heapq.heappop(pq)
            i += 1
            if i < j:
                heapq.heappush(pq, (A[i] / float(A[j]), i, j))

        return A[pq[0][1]], A[pq[0][2]]


class SolutionLee:
    import bisect as bi
    class Solution(object):
        def kthSmallestPrimeFraction(self, A, K):
            l, r, n = 0.0, 1.0, len(A)
            while True:
                m = (l + r) / 2
                border = [bisect.bisect(A, A[i] * m) for i in range(n)]
                cur = sum(border)
                if cur > K:
                    r = m
                elif cur < K:
                    l = m
                else:
                    return max([[A[j - 1], A[i]] for i, j in enumerate(border) if j > 0], key=lambda x: float(x[0]) / x[1])

