
class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost: int, runningCost: int) -> int:

        i = 1  # start at 1
        res = -1
        waiting = customers[0]
        onBoard = 0
        maxProfit = 0
        while i < len(customers) or waiting > 0:
            # get 4 or remainder + current passangers
            newToOnboard = min(4, waiting)
            # remove people waiting
            waiting -= newToOnboard
            # add people to go
            onBoard += newToOnboard
            # get profit of all to go
            profit = onBoard * boardingCost - i * runningCost

            # if profit is over max then reset the maxProfit
            if profit > maxProfit:
                maxProfit = profit
                res = i
            if i < len(customers):
                # stop adding customers once we finish list
                waiting += customers[i]
            i += 1
        return res




