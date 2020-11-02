
class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        product = 1
        summ = 0
        for ch in str(n):
            summ += int(ch)
            product *= int(ch)
        return product - summ



