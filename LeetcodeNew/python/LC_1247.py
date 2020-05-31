"""
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/419874/Simply-Simple-Python-Solution-with-detailed-explanation

1. Get the count of "x_y" and "y_x"
2. If sum of both counts is odd then return -1. We need a pair to make the strings equal
3. Each 2 count of "x_y" needs just 1 swap. So add half of "x_y" count to the result
4. Each 2 count of "y_x" needs just 1 swap. So add half of "y_x" count to the result
5. if we still have 1 count of "x_y" and 1 count of "y_x" then they need 2 swaps so add 2 in result.
"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    x_y += 1
                else:
                    y_x += 1

        if (x_y + y_x) % 2 == 1:
            return -1
        # Both x_y and y_x count shall either be even or odd to get the result.
        # x_y + y_x should be even

        res = x_y // 2
        res += y_x // 2

        if x_y % 2 == 1:
            res += 2
        # If there count is odd i.e. we have "xy" and "yx" situation
        # so we need 2 more swaps to make them equal

        return res


