

class Solution:
    def maxWidthRamp(self, A) -> int:
        stack = []
        for i, num in enumerate(A):
            if not stack or num < A[stack[-1]]:
                stack.append(i)
        res = 0
        for i in range(len(A)-1, -1, -1):
            while stack and A[i] >= A[stack[-1]]:
                res = max(res, i - stack.pop())
        return res

