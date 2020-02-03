"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""


"""
- 如果當前是數字，那麼更新計算當前數字；
- 如果當前是操作符+或者-，那麼需要更新計算當前計算的結果res，並把當前數字num設為0，sign設為正負，重新開始；
- 如果當前是(，那麼說明後面的小括號裡的內容需要優先計算，所以要把res，sign進棧，更新res和sign為新的開始；
- 如果當前是)，那麼說明當前括號裡的內容已經計算完畢，所以要把之前的結果出棧，然後計算整個式子的結果；
- 最後，當所有數字結束的時候，需要把結果進行計算，確保結果是正確的。
"""


class SolutionBest:
    def calculate(self, s):
        return self.helper(s, 0)

    def helper(self, s, i):
        res = 0
        num, sign = "", 1
        while (i < len(s)):
            # if s[i] in "0123456789"
            char = s[i]
            if char.isdigit():
                num += char
            elif char in "+-()":
                if num != "":
                    res += sign * int(num)
                num = ""
                if char == "+":
                    sign = 1
                elif char == "-":
                    sign = -1
                elif char == "(":
                    nxt, i = self.helper(s, i + 1)
                    res += sign * nxt
                elif char == ")":
                    return (res, i)
            i += 1
        if num != "":
            res += sign * int(num)
        return res



class SolutionBestToBeTested:
    def calculate(self, s):
        return self.helper(s, 0)

    def helper(self, s, i):
        res = 0
        num, sign = "", 1
        while (i < len(s)):
            char = s[i]
            if char.isdigit():
                num += char
            else:
                if num != "":
                    res += sign * int(num)
                num = ""
                if char == "+":
                    sign = 1
                elif char == "-":
                    sign = -1
                elif char == "(":
                    nxt, i = self.helper(s, i + 1)
                    res += sign * nxt
                elif char == ")":
                    return (res, i)
            i += 1
        if num != "":
            res += sign * int(num)
        return res



class Solution:
    def calculate(self, s):

        res, num, sign = 0, 0, 1
        stack = []
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char == "+" or char == "-":
                res = res + sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ")":
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num
        return res




class Solution2:
    def __init__(self):
        self.i = 0

    def calculate(self, s):
        return self.evaluation(s)

    def evaluation(self, s):
        sign, res = 1, 0

        while self.i < len(s):
            if s[self.i] == ' ':
                self.i += 1
                continue
            elif s[self.i] == '+':
                sign = 1
            elif s[self.i] == '-':
                sign = -1
            elif s[self.i] == '(':
                self.i += 1
                res += sign * self.evaluation(s)
                sign = 1
            elif s[self.i] == ')':
                return res
            else:  # s[i] is digit.
                curNum = int(s[self.i])
                while self.i + 1 < len(s) and s[self.i + 1].isdigit():
                    curNum = curNum * 10 + int(s[self.i + 1])
                    self.i += 1
                res += curNum * sign
                sign = 1
            self.i += 1

        return res



# s = "(22+(10+(4+5+2)-3)+(6+8))"
s = "-200-3-3-3"
a = SolutionBestToBeTested()
print(a.calculate(s))





