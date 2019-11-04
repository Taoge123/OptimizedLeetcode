class Solution:
    def calculate(self, s: str) -> int:
        # https://blog.csdn.net/fuxuemingzhu/article/details/84133441
        res, num, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char in ["-", "+"]:
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif char == ")":
                res += sign * num
                # this will be sign
                res *= stack.pop()
                # this will be last calculated num
                res += stack.pop()
                num = 0
        return res + num * sign


s = "(1+(4+5+2)-3)+(6+8)"

a = Solution()
print(a.calculate(s))




