import heapq

class Solution:
    def stoneGameVI(self, aliceValues, bobValues) -> int:
        nums = []
        for i in range(len(aliceValues)):
            nums.append((-aliceValues[i] - bobValues[i], aliceValues[i], bobValues[i]))
        heapq.heapify(nums)
        alice, bob = 0, 0
        # n = len(nums)
        i = 0

        while nums:
            if i % 2 == 0:
                alice += heapq.heappop(nums)[1]
            else:
                bob += heapq.heappop(nums)[2]
            i += 1

        if alice > bob:
            return 1
        elif alice == bob:
            return 0
        else:
            return -1



