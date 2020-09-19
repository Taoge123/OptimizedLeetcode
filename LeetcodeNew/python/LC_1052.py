

class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        summ = 0
        n = len(customers)

        for i in range(n):
            if grumpy[i] == 0:
                summ += customers[i]
        res = 0
        for i in range(n):
            if grumpy[i] == 1:
                summ += customers[i]
            if i- X >= 0 and grumpy[i - X] == 1:
                summ -= customers[i - X]

            res = max(res, summ)
        return res




