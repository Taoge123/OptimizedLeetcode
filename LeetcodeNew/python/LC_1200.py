
class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        res = []
        diffs = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        target = min(diffs)

        for i, diff in enumerate(diffs):
            if diff == target:
                res.append([arr[i], arr[i + 1]])

        return res


