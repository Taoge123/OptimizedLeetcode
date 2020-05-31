import collections

class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted: int, use_limit: int) -> int:
        count = collections.Counter()
        res = 0
        for val, label in sorted(zip(values, labels))[::-1]:
            if count[label] < use_limit:
                res += val
                count[label] += 1
                num_wanted -= 1

            if num_wanted == 0:
                break

        return res



