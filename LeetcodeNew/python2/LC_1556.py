class SolutionTony:
    def thousandSeparator(self, n: int) -> str:
        stack = list(str(n))

        res = []
        while len(stack) > 3:
            res.append(stack.pop())
            res.append(stack.pop())
            res.append(stack.pop())
            res.append('.')

        while stack:
            res.append(stack.pop())

        return "".join(res)[::-1]


class Solution:
    def thousandSeparator(self, n):
        if not n:
            return "0"
        ret, part = [], ""
        while n:
            part = str(n % 10) + part
            n //= 10
            if len(part) == 3:
                ret.append(part)
                part = ""
        if part:
            ret.append(part)
        return ".".join(ret[::-1])

