
class Solution:
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) < sum(cost):
            return -1

        result = 0
        count = 0
        for i in range(len(gas)):
            count += gas[i] - cost[i]
            if count < 0:
                count = 0
                result = (i + 1) % len(gas)
        return result




