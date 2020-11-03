
class Solution:
    def minDeletionSize(self, A) -> int:

        res = 0
        for i in range(len(A[0])):
            s = []
            for j in range(len(A)):
                s.append(A[j][i])
            if not self.check(s):
                res += 1
        return res

    def check(self, s):
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                return False
        return True





