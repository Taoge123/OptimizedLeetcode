"""
解题思路：几乎和【leetcode】719. Find K-th Smallest Pair Distance 的方法一样。
只不过一个是减法一个是乘法，还有一点区别是【leetcode】719.
Find K-th Smallest Pair Distance中i-j和j-i只算一个元素，而本题中i*j与j*i算两个元素。

这道题跟之前那道Kth Smallest Element in a Sorted Matrix没有什么太大的区别，
这里的乘法表也是各行各列分别有序的。那么之前帖子里的方法都可以拿来参考
"""
"""

https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/discuss/262279/Python-Binary-Search-Need-to-Return-the-Smallest-Candidate

Nearly every one have used the Multiplication Table.
But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table,
and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]
"""
import heapq

class Solution1:
    def findKthNumber(self, m, n, k):
        heap = [(i, i) for i in range(1, m+1)]
        heapq.heapify(heap)

        for _ in range(k):
            val, root = heapq.heappop(heap)
            nxt = val + root
            if nxt <= root * n:
                heapq.heappush(heap, (nxt, root))

        return val


"""
To find the kth smallest number in a multiplication table, 
a brute force way is to iterate from 1 to m * n and check whether there are k numbers no larger than it. 
If it isn't, we keep iterating until it is. Then we find the kth smallest number.

Since we have low end (1) and high end (m * n) of our search space, we can use binary search here. 
The key function is to check there are k numbers in M table no larger than our current searching value x:

def check(x):
	cnt = 0
	for r in range(1, m+1):
		cnt += min(x//r, n)  # 'x//r' ensure 'x' is included so that fits 'no larger than'
		if cnt >= k: return False
	return True
"""
"""
For example, m=n=4

1  2  3  4
2  4  6  8
3  6  9  12
4  8  12 16
x=4, cnt=4+2+1+1=8, there are 8 number less or equal than 4.
So if k <= 8, check(4) return False; if k > 8, check(4) return True.

Each check(x) costs O(m). And sum(min(mid//r, n) for r in range(1,m+1)) < k 
produced the same result as check(x) but just doesn't break earlier. 
And we can implement our binary search in this way:

"""
class Solution2:
    def findKthNumber(m, n, k):
        if m > n: m, n = n, m
        lo, hi = 1, m * n
        while lo < hi:
            mid = lo + hi >> 1
            if sum(min(mid // r, n) for r in range(1, m + 1)) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


"""
And you can notice that we don't return mid when sum(...) == k 
but keep binary searching until lo < hi. This is because we need to return the smallest candidate.

This is tricky.
For example, m=34, n=42, k=401. You will find both 126 and 127 fit criteria 
that there are 401 numbers no larger than 126 and 127. This is because 127 is not in the multiplication table!. 
127 is a prime and its only factorization is 1 * 127 which is out of the boundary of 34 * 42. 
And that's the reason we need to return the smallest candidate: To ensure our candidate is in M table.

So why the smallest candidate is in M table?
Because if the smallest candidate(no smaller than k numbers in M table), saying x, is not in M table, 
then x-1 will also be a candidate(no smaller than k numbers in M table) since x is not in the table. 
Then x is not the smallest candidate. For example, we have such range in our flattern sorted M table:

Val: 1,..., xi,  xi, xj,  xj,  ...
Seq: 1,..., p-1, p,  p+1, p+2, ...

When k=p, {xi, xi+1,..., xj-1} are all valid candidates. 
There are p numbers no larger than xi or xi+1or xj-1 becasue {xi+1,..., xj-1} are not in M table. 
And we need to return xi which is in the M table and the smallest candidate as well.
When k=p+1, the smallest candidate would be xj.

As for time complexity, it would be log(mn) times of binary search so total is O(mlog(mn)).
And we can swap m, n if m > n and ensure time complexity to be O(min(m,n) * log(mn))

Hope above explanation is clear to you. This is a good example to show the tricky issue in binary search design.
"""

class Solution3:
    def findKthNumber(self, m, n, k):
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
                l = mid + 1
            else:
                r = mid
        return l


class Solution4:
    def findKthNumber(self, m, n, k):
        l, h = 1, m*n
        while l < h:
            mid = (l + h) // 2
            cnt = 0
            for i in range(1, m+1):
                cnt += min(mid // i, n)
            if cnt >= k:
                h = mid
            else:
                l = mid + 1
        return l

class Solution5:
    def findKthNumber(self, m, n, k):
        def binary(num):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(n, num / i)
            return cnt
        left, right = 0, m * n + 1
        while right - left > 1:
            mid = (left + right) >> 1
            if binary(mid) < k:
                left = mid
            else:
                right = mid
        return left + 1

"""
解题思路：
从1到k进行二分枚举，上下界分别为lo, hi，记当前枚举数字为mid

利用O(n)的代价求乘法表中有多少个数字不大于mid，记为count

  若count >= k，则令hi = mid - 1

  否则，令lo = mid + 1

最后返回lo"""

class Solution6:
    def findKthNumber(self, m, n, k):

        count = lambda t: sum(min(m, t / x) for x in range(1, n + 1))
        lo, hi = 1, k
        while lo <= hi:
            mid = (lo + hi) / 2
            if (count(mid)) >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

