
class Solution:
    def sumEvenAfterQueries(self, A, queries):
        cur = sum([num for num in A if num % 2 == 0])
        res = []
        for k, val in queries:
            if A[val] % 2 == 0:
                cur -= A[val]
            A[val] += k
            if A[val] % 2 == 0:
                cur += A[val]
            res.append(cur)

        return res



