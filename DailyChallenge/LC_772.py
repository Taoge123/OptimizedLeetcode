
class Solution:
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
