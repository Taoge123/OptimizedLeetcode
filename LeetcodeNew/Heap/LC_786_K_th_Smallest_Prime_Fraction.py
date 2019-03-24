
"""
OMG
http://www.cnblogs.com/grandyang/p/6854825.html

https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378
https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm

1 - 373. Find K Pairs with Smallest Sums
2 - 378. Kth Smallest Element in a Sorted Matrix
3 - 668. Kth Smallest Number in Multiplication Table
4 - 719. Find K-th Smallest Pair Distance
5 - 786. K-th Smallest Prime Fraction

A sorted list A contains 1, plus some number of primes.
Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?
Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

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

public int kthSmallest(int[][] matrix, int k) {
    int n = matrix.length;

    int l = matrix[0][0];               // minimum element in the matrix
    int r = matrix[n - 1][n - 1];       // maximum element in the matrix

    for (int cnt = 0; l < r; cnt = 0) { // this is the binary search loop
        int m = l + (r - l) / 2;

        for(int i = 0, j = n - 1; i < n; i++)  {
            while (j >= 0 && matrix[i][j] > m)
                j--;  // the pointer j will only go in one direction
            cnt += (j + 1);
        }

        if (cnt < k) {
            l = m + 1;   // cnt less than k, so throw away left half
        } else {
            r = m;       // otherwise discard right half
        }
    }

    return l;
}
"""


"""
for each row i, all the numbers (call them A[j]) to the right of A[i]/m, 
are the ones such that A[i]/A[j] will be smaller than m.
sum them up so that you will know the total number of pairs A[i]/A[j] that are smaller than m. 
Find a proper m such that the total number equals K, 
and then you find the maximum A[i]/A[j] among all pairs that are smaller than A[i]/m, 
which is the Kth smallest number.
"""

import bisect
import heapq

class SolutionLee:
    def kthSmallestPrimeFraction(self, A, K):
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])

"""
这道题给了我们一个有序数组，里面是1和一些质数，说是对于任意两个数，都可以组成一个 [0, 1] 之间分数，
让我们求第K小的分数是什么，题目中给的例子也很好的说明了题意。那么最直接暴力的解法就是遍历出所有的分数，
然后再进行排序，返回第K小的即可。但是这种无脑暴力搜索的方法OJ是不答应的，无奈，只能想其他的解法。
我们想，由于数组是有序的，所以最小的分数肯定是由第一个数字和最后一个数字组成的，
而接下来第二小的分数我们就不确定是由第二个数字和最后一个数字组成的，还是由第一个数字跟倒数第二个数字组成的。
我们的想法是用一个最小堆来存分数，那么每次取的时候就可以将最小的分数取出来，由于前面说了，
我们不能遍历所有的分数都存入最小堆，那么我们怎么办呢，我们可以先存n个，哪n个呢？
其实就是数组中的每个数字都和最后一个数字组成的分数。由于我们需要取出第K小的分数，
那么我们在最小堆中取K个分数就可以了，第一个取出的分数就是那个由第一个数字和最后一个数字组成的最小的分数，
然后就是精髓所在了，我们此时将分母所在的位置前移一位，还是和当前的分子组成新的分数，
这里即为第一个数字和倒数第二个数字组成的分数，存入最小堆中，
那么由于之前我们已经将第二个数字和倒数第一个数字组成的分数存入了最小堆，所以不用担心第二小的分数不在堆中，
这样每取出一个分数，我们都新加一个稍稍比取出的大一点的分数，这样我们取出了第K个分数即为所求
"""


class Solution2:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        heap = [(A[0]/A[i], 0, i) for i in range(1, len(A))]
        heapq.heapify(heap)

        for i in range(K):
            frac, nume, deno = heapq.heappop(heap)

            if nume+1<deno:
                heapq.heappush(heap,(A[nume+1]/A[deno],nume+1,deno))

        return [A[nume],A[deno]]



class SolutionL1:
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
In Python, storing the fractions will be done with a tuple (fraction, i, j), 
representing the fraction fraction = primes[i] / primes[j]. When we use this fraction, 
we will push the next fraction (primes[i+1] / primes[j], i+1, j) onto the heap, 
assuming that the next fraction is valid (ie., that i+1 < j).

In Java, storing the fractions will be done as an int[2] of {i, j} (indexes, not elements of A),
and we use a custom comparator to ensure the right elements are pq.offered correctly.

With this detail out of the way, the solution is straightforward.

"""


class SolutionL2:
    #Note - this solution may TLE.
    def kthSmallestPrimeFraction(self, A, K):
        pq = [(A[0] / float(A[i]), 0, i) for i in range(len(A) - 1, 0, -1)]

        for _ in range(K-1):
            frac, i, j = heapq.heappop(pq)
            i += 1
            if i < j:
                heapq.heappush(pq, (A[i] / float(A[j]), i, j))

        return A[pq[0][1]], A[pq[0][2]]








