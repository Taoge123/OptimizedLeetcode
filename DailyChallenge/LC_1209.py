
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
            else:
                if char == stack[-1][0]:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([char, 1])

        res = []
        for k, v in stack:
            res.append(k * v)
        return "".join(res)



