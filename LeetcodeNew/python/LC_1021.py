

"""
解题思路
用一个整型变量opened来记录左括号比右括号多出的数量
遍历S，遇到左括号++opened，遇到右括号--opened
除非遇到第一个左括号（opened = 1）或者最后一个右括号（opened = 0）
不然其余字符均加入最终结果res

"""
"""
Primitive string will have equal number of opened and closed parenthesis.

Explanation:
opened count the number of opened parenthesis.
Add every char to the result,
unless the first left parenthesis,
and the last right parenthesis.
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        opened = 0
        res = []

        for char in S:
            if char == "(":
                opened += 1
                if opened != 1:
                    res += char

            else:
                opened -= 1
                if opened != 0:
                    res += char

        return "".join(res)







