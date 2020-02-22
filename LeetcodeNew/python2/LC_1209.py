
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for char in s:
            print(stack)
            if stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return "".join(char * k for char, k in stack)


"""
[['#', 0], ['d', 1]]
[['#', 0], ['d', 1], ['e', 1]]
[['#', 0], ['d', 1], ['e', 2]]
[['#', 0], ['d', 1]]
[['#', 0], ['d', 2]]
[['#', 0], ['d', 2], ['b', 1]]
[['#', 0], ['d', 2], ['b', 2]]
[['#', 0], ['d', 2], ['b', 2], ['c', 1]]
[['#', 0], ['d', 2], ['b', 2], ['c', 2]]
[['#', 0], ['d', 2], ['b', 2]]
[['#', 0], ['d', 2]]
[['#', 0]]
[['#', 0], ['a', 1]]
[['#', 0], ['a', 2]]
"""


s = "deeedbbcccbdaa"
k = 3
a = Solution()
print(a.removeDuplicates(s, k))


