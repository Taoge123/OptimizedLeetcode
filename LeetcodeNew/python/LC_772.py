"""
https://leetcode.com/problems/basic-calculator-iii/discuss/113592/Development-of-a-generic-solution-for-the-series-of-the-calculator-problems


"""

import collections

class Solution1:
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
            node = s.popleft()
            if node.isdigit():
                num = num * 10 + int(node)
            if node == '(':
                # do recursion to calculate the sum within the next (...)
                num = self.helper(s)
            if len(s) == 0 or (node == '+' or node == '-' or node == '*' or node == '/' or node == ')'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / float(num))
                sign = node
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


