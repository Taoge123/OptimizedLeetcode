"""
Intialize the answer to numBottles because we know that is the minimum number of bottles that can be drank.
After that in a while loop with condition that you have equal to or more emptyBottles than the exchange rate, just keep exchanging the empty bottles and add the exchanged bottles to answer and to the emptyBottles count.
divmod will help you with clean code here. Quotient is the new full bottles recevied after the exchange and the remainder is the empty bottles that could not be exchanged.
After the loop ends, answer is the number of bottles that can be drunk.
Time complexitiy: O(log(numBottles))
Space complexity: O(1)

"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            numBottles, empty = divmod(numBottles, numExchange)
            res += numBottles
            numBottles += empty
        return res




