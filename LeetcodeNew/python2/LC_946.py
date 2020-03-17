

class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        i = j = 0
        for num in pushed:
            pushed[i] = num
            while i >= 0 and pushed[i] == popped[j]:
                i = i - 1
                j = j + 1
            i += 1
        return i == 0



pushed = [1,2,3,4,5]

popped = [4,5,3,2,1]

a = Solution()
print(a.validateStackSequences(pushed, popped))


