
class Solution1:
    def trimMean(self, arr) -> float:
        n = len(arr)
        return sum(sorted(arr)[n // 20: -n // 20]) / (n * 9 // 10)


