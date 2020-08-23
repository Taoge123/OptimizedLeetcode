
class Solution2:
    def validateStackSequences(self, pushed, popped) -> bool:
        i = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(pushed)


class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        i = j = 0
        for num in pushed:
            pushed[i] = num
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1
            i += 1
        return i == 0



pushed = [1,2,3,4,5]

popped = [4,5,3,2,1]

a = Solution()
print(a.validateStackSequences(pushed, popped))


