
class Solution:
    def partitionLabels(self, S: str):
        res = []
        count = 0
        sum1, sum2 = 0, 0
        for a, b in zip(list(S), sorted(list(S))):
            sum1 += ord(a)
            sum2 += ord(b)
            count += 1
            if sum1 == sum2:
                res.append(count)
                count = 0
        return res



