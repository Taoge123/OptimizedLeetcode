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





class Solution:
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
