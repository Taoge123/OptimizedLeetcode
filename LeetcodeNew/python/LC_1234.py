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

"""

import collections

class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        n = len(s)
        res = float('inf')

        left = 0
        for right, char in enumerate(s):
            count[char] -= 1
            while left < n and all(count[char] <= n//4 for char in 'QWER'):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1

        return res




