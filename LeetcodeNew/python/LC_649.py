import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queueR = collections.deque()
        queueD = collections.deque()

        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                queueR.append(i)
            else:
                queueD.append(i)

        while queueR and queueD:
            d = queueD.popleft()
            r = queueR.popleft()
            if d < r:
                queueD.append(n)
            else:
                queueR.append(n)
            n += 1
        if len(queueR) > 0:
            return "Radiant"
        else:
            return "Dire"



