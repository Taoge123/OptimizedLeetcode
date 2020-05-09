
class Solution:
    def heightChecker(self, heights) -> int:
        return sum(i != j for i, j in zip(heights, sorted(heights)))



