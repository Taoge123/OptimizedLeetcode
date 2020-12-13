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


class SolutionTony2:
    def __init__(self):
        self.i = 0

    def calculate(self, s):
        stack = []
        num = 0
        op = '+'

        while self.i < len(s):
            ch = s[self.i]
            self.i += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch == '(':
                num = self.calculate(s)
            if self.i >= len(s) or ch == '+' or ch == '-' or ch == ')':
                if op == '+':
                    stack.append(num)
                else:
                    stack.append(-num)
                op = ch
                num = 0
            if ch == ')':
                break

        return sum(map(int, stack))



