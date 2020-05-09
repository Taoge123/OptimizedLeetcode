

class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        maxi = summ = tmp = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                summ += customers[i]                # sum of satisfied customers
                customers[i] = 0
            else:
                tmp += customers[i]            # sum of grumpy customers
            if i>= X:
                tmp -= customers[i - X]  # remove the leftmost element to keep the sliding window with # of X
            maxi = max(maxi, tmp)  # max # of satisfied grumpy customers with a secret technique
        return summ + maxi


class Solution2:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        n = len(customers)
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)
        maxi = add = sum(c for c, g in zip(customers[:X], grumpy[:X]) if g == 1)

        for i in range(X, n):
            add -= customers[i - X] * grumpy[i - X]
            add += customers[i] * grumpy[i]
            maxi = max(maxi, add)

        return base + maxi

