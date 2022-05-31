class SolutionTony:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:

        count = 0
        n = len(customers)
        for i, j in zip(customers, grumpy):
            if j == 0:
                count += i

        res = 0
        for right in range(n):
            if grumpy[right] == 1:
                count += customers[right]
            if right - minutes >= 0:
                if grumpy[right - minutes] == 1:
                    count -= customers[right - minutes]
            res = max(res, count)
        return res



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




