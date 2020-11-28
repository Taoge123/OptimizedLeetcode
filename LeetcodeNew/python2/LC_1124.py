

"""
Intuition
If working hour > 8 hours, yes it's tiring day.
But I doubt if 996 is a well-performing interval.
Life needs not only 996 but also 669.


Explanation
We starts with a score = 0,
If the working hour > 8, we plus 1 point.
Otherwise we minus 1 point.
We want find the maximum interval that have strict positive score.

After one day of work, if we find the total score > 0,
the whole interval has positive score,
so we set res = i + 1.

If the score is a new lowest score, we record the day by seen[cur] = i.
seen[score] means the first time we see the score is seen[score]th day.

We want a positive score, so we want to know the first occurrence of score - 1.
score - x also works, but it comes later than score - 1.
So the maximum interval is i - seen[score - 1]


Complexity
Time O(N) for one pass.
Space O(N) in worst case if no tiring day.

https://www.youtube.com/watch?v=H76XMJmBfP0
"""


class Solution:
    def longestWPI(self, hours):
        res = summ = 0
        table = {}
        for i, h in enumerate(hours):
            summ = summ + 1 if h > 8 else summ - 1
            if summ > 0:
                res = i + 1
            if summ not in table:
                table[summ] = i
            #we look for summ - 1 since we need more positive number than negative number
            if summ - 1 in table:
                res = max(res, i - table[summ - 1])
        return res








