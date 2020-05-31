"""
https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/358419/Confused-by-this-problem-I-was-too-but-here-is-how-it-became-crystal-clear...

"""


class Solution:
    def maxDepthAfterSplit(self, seq: str):
        res = []
        depth = 0
        for i in range(len(seq)):
            if seq[i] == '(':
                depth += 1

            res.append(depth % 2)

            if seq[i] == ')':
                depth -= 1

        return res


"""
Solution 2: Split by Half
Count the number of level of whole string.
Then split it by half.
Group 0: the part under the half height
Group 1: the part above the half height
"""


class Solution2:
    def maxDepthAfterSplit(self, seq: str):
        depth = cur = 0
        res = [0] * len(seq)

        for char in seq:
            if char == '(':
                cur += 1
                depth = max(depth, cur)
            else:
                cur -= 1

        half = depth / 2

        for i, char in enumerate(seq):
            if char == '(':
                cur += 1
                if cur > half:
                    res[i] = 1
            else:
                if cur > half:
                    res[i] = 1
                cur -= 1

        return res




