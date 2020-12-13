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
"""
典型的栈的应用。需要设置两个栈

  stack<int>nums;
  stack<int>sign;
nums用来存储数值，sign用来存储符号。这里需要有个小技巧，在字符串最开始添加一个+入栈，遇到'('也添加一个+入栈，这样保证每个数字（和小括号产生的中间结果）都在sign中有一个对应的符号位。

具体的算法是：遇到'('就将当前结果curResult入栈并清零。遇到')'就将当前结果与sign的栈顶元素结合形成新数（然后sign退栈），并加上nums的栈顶元素结合形成新数（然后nums退栈）。遇到符号就加入sign的栈。遇到纯数字就取出sign的栈顶元素结合
"""


class SolutionTony:
    def calculate(self, s):
        stack = []
        res = 0
        sign = 1
        n = len(s)

        i = 0
        while i < n:
            ch = s[i]
            if ch.isdigit():
                print(ch)
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                # i++ later
                i -= 1
                res += sign * num

            elif ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif ch == ')':
                res *= stack.pop()
                res += stack.pop()

            i += 1
        return res





class SolutionWisdom:
    def calculate(self, s: str) -> int:
        S = "+"
        for ch in s:
            if ch == ' ':
                continue
            S += ch
            if ch == '(':
                S += '+'
        s = S
        nums = []
        signs = []
        res = 0
        sign = 0
        i = 0
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                sign = 1 if s[i] == '+' else -1

            elif s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                # 当前平行单项式
                res += num * sign
                # i已经指向了最后一位num的下一位, 要回去一位
                i = j - 1

            elif s[i] == '(':
                # 记录下一层之前的结果和符号
                nums.append(res)
                signs.append(sign)
                res = 0

            elif s[i] == ')':
                #之前存的sign再加上之前的res(在nums里面)
                res = nums.pop() + signs.pop() * res
            i += 1
        return res


"""
+(1+(+4+5+2)-3)+(+6+8)
"""

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
# s = "-200-3-3-3"
s = "2147483647"
a = SolutionTony()
print(a.calculate(s))





