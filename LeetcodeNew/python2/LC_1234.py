"""
https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/409056/Python-Sliding-Window-with-Explanation-Same-with-76

Intuition
We want a minimum length of substring,
which leads us to the solution of sliding window.
Specilly this time we don't care the count of elements inside the window,
we want to know the count outside the window.


Explanation
One pass the all frequency of "QWER".
Then slide the windon in the string s.

Imagine that we erase all character inside the window,
as we can modyfy it whatever we want,
and it will always increase the count outside the window.

So we can make the whole string balanced,
as long as max(count[Q],count[W],count[E],count[R]) <= n / 4.


Important
Does i <= j + 1 makes more sense than i <= n.
Strongly don't think, and i <= j + 1 makes no sense.

Answer the question first:
Why do we need such a condition in sliding window problem?

Actually, we never need this condition in sliding window solution
(Check all my other solutions link at the bottom).

Usually count the element inside sliding window,
and i won't be bigger than j because nothing left in the window.

The only reason that we need a condition is in order to prevent index out of range.
And how do we do that? Yes we use i < n

1. Does i <= j + 1 even work?
2. When will i even reach j + 1?
3. Does i <= j + 1 work better than i <= j?

解法１：
比赛的时候我用的是二分法，尝试我们需要移除的substring的宽度ｋ，它的范围是[0,n]．二分的过程中，每次确定一个ｋ，就在ｓ上划过一个固定长度ｋ的窗口，查看是否在哪个位置的时候可行．

我当时写的判定标准是：如果剩余的（除去滑动窗口之外）的词频统计sum里，假设最多的频率是t，
那么我们检查diff=t*4-sum['Q']-sum['W']-sum['E']-sum['R']，
这个diff表示我们还需要多少个＂万能字符＂去填充这个＂直方图＂使得它平齐.如果diff<=k,那么就说明ｋ可行（事实上，其中多余的k-diff个万能字符我们其实可以弃用）．

这个复杂度其实是nlog(n).

解法２：
本题其实用双指针来做更简单，时间复杂度为o(n).

我们提前计算好，理想情况下，最终每个字符出现的次数都应该是x=s.size()/4.

我们其实只要找到一段窗口，使得窗口外的词频统计sum满足每个字母的频率都小于ｋ即可！

基于这种算法，滑窗的两个指针其实是可以交替移动的．比如说当慢指针为i,快指针移动到j，满足条件．那么下一步慢指针移动到i+1,
而快指针则不用动．为什么快指针不需要考察小于ｊ的位置呢？其实如果窗口[i+1,k]满足条件的话（k<j)，那么一定有[i,k]也满足条件，
所以快指针根本就不会走到j的位置了．所以我们可以保证，并没有一个k<j使得[i+1,k]满足条件．所以快指针不需要回调．

"""

import collections

class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        n = len(s)
        res = float('inf')

        i = 0
        for j, char in enumerate(s):
            count[char] -= 1
            # 由于任意一个右端点j，都有一个左端点i，满足条件
            while i < n and all(count[char] <= n//4 for char in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1

        return res




