"""
stack or greedy

1541.Minimum-Insertions-to-Balance-a-Parentheses-String
本题和 921 Minimum Add to Make Parentheses Valid本质一样。区别只在于一个左括号必须和两个连续的右括号匹配。我们仍然可以沿用贪心法的思想，
用count来记录未被匹配的左括号的数目。变化在于：

我们需要连续两个右括号，才能试图与之前的一个左括号对消。如果不存在连续的两个右括号，我们必须先手工增加一个右括号，即ret++，然后再试图匹配左括号消减count。
如果最终有剩余未被匹配的左括号，我们需要增加两倍数目的右括号与之对应，即ret+=count*2.

count -> unmatched left parenthesis
1. must two consecutive ) cancel one (
2. at the end, res += count * 2

"""


class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        i = 0
        res = 0
        while i < len(s):
            if s[i] == '(':
                count += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    count -= 1
                    i += 1
                else:
                    # 需要补一个), 所以 res += 1
                    res += 1
                    count -= 1
            if count < 0:
                res += 1
                count = 0
            i += 1
        return res + count * 2









