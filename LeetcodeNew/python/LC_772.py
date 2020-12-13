"""
https://leetcode.com/problems/basic-calculator-iii/discuss/113592/Development-of-a-generic-solution-for-the-series-of-the-calculator-problems


"""

import collections
import math


class SolutionTony1:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        num = 0

        while self.i < len(s):
            ch = s[self.i]
            self.i += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch == '(':
                num = self.calculate(s)
            if self.i >= len(s) or ch in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))

                op = ch
                num = 0

            if ch == ')':
                break
        return sum(map(int, stack))




class SolutionWisdom:
    def calculate(self, s: str) -> int:
        stack = []
        curStr = ""
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(curStr)
                curStr = ""
            elif s[i] == ')':
                curRes = self.calc(curStr)
                curStr = stack.pop() + str(curRes)
            else:
                curStr += s[i]
        return self.calc(curStr)

        # +5--4+3*-2-2-3-+3
    def calc(self, s):
        S = '+'
        for ch in s:
            if ch == ' ':
                continue
            S += ch
            if ch == '(':
                S += "+"
        s = S
        nums = []
        i = 0
        while i < len(s):
            if s[i] in '+-':
                j = i + 1
                if s[j] in '+-':
                    j += 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i + 1:j])
                if s[i] == '+':
                    nums.append(num)
                else:
                    nums.append(-num)
                i = j - 1

            elif s[i] in '*/':
                j = i + 1
                if s[j] in '+-':
                    j += 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i + 1:j])
                if s[i] == '*':
                    nums[-1] *= num
                else:
                    nums[-1] /= num
                    #only for python
                    nums[-1] = math.ceil(nums[-1]) if nums[-1] < 0 else math.floor(nums[-1])
                i = j - 1
            i += 1

        return sum(nums)


class SolutionTony:
    def calculate(self, s):
        s = collections.deque(s)
        return self.helper(s)

    def helper(self, s):
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        while len(s) > 0:
            char = s.popleft()
            if char.isdigit():
                num = num * 10 + int(char)
            if char == '(':
                # do recursion to calculate the sum within the next (...)
                num = self.helper(s)
            if len(s) == 0 or (char == '+' or char == '-' or char == '*' or char == '/' or char == ')'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / float(num))
                sign = char
                num = 0
                if sign == ')':
                    break
        return sum(stack)



class SolutionBest:
    def calculate(self, s):
        s = s + "$"
        return self.helper(s, [], 0)

    def helper(self, s, stack, i):
        num = 0
        sign = '+'
        while i < len(s):
            char = s[i]
            if char == " ":
                i += 1
                continue
            if char.isdigit():
                num = 10 * num + int(char)
                i += 1
            elif char == '(':
                num, i = self.helper(s, [], i + 1)
            else:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(int(stack.pop() / num))
                i += 1
                if char == ')':
                    return sum(stack), i
                num = 0
                sign = char
        return sum(stack)




s = "(3+5 / 2 - (6*7) )"
a = SolutionBest()
print(a.calculate(s))


