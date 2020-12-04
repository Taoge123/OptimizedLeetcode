
class Solution:
    def removeKdigits(self, num, k):

        stack = []
        if k >= len(num):
            return "0"

        for item in num:
            while stack and k and stack[-1] > item:
                stack.pop()
                k -= 1
            stack.append(item)
        while k:
            stack.pop()
            k -= 1

        return str(int("".join(stack)))

