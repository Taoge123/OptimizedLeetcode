import collections

class Solution:
    def advantageCount(self, A, B):

        n = len(A)
        res = [0] * n
        A = collections.deque(sorted(A))
        B = collections.deque(sorted((b, i) for i, b in enumerate(B)))

        for i in range(n):
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            res[b[1]] = a

        return res

