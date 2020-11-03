"""
Similar to the problem 503. Next Greater Element II
"""


class Solution:
    def finalPrices(self, prices):
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices


