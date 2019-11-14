
class Solution:
    def calculate(self, s):
        num = 0
        stack = []
        sign = "+"

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = s[i]
        return sum(stack)


s = "3+2*2+2*2+2"
a = Solution()
print(a.calculate(s))














