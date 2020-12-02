
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        i = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(pushed)
