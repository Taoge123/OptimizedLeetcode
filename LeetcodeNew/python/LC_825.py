import collections
import bisect

class Solution:
    def numFriendRequests(self, ages) -> int:
        count = collections.Counter(ages)
        res = 0
        for ageA, countA in count.items():
            for ageB, countB in count.items():
                if (0.5 * ageA + 7) < ageB <= ageA:
                    res += countA * countB
                    if ageA == ageB:
                        res -= countA
        return res




class Solution2:
    def numFriendRequests(self, ages) -> int:
        res = 0
        ages = sorted(ages)
        for num in ages:
            left = num // 2 + 8
            right = num
            start = bisect.bisect_left(ages, left)
            end = bisect.bisect_right(ages, right)
            val = end - start - 1
            res += val if val > 0 else 0
        return res


class SolutionBest:
    def numFriendRequests(self, ages) -> int:

        res = 0
        numInAge = [0] * 121
        sumInAge = [0] * 121

        for age in ages:
            numInAge[age] += 1

        for i in range(1, 121):
            sumInAge[i] = numInAge[i] + sumInAge[i - 1]

        for i in range(15, 121):
            if numInAge[i] == 0:
                continue

            count = sumInAge[i] - sumInAge[i // 2 + 7]
            res += count * numInAge[i] - numInAge[i]

        return res



