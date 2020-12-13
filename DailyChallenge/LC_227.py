



class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = char
        return sum(stack)