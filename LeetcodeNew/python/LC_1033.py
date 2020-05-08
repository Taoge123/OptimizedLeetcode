
class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        nums = [a, b, c]
        x = min(nums)
        z = max(nums)
        y = sum(nums) - x - z

        if z - x == 2:
            return [0, 0]

        if (y - x <= 2 or z - y <= 2):
            return [1, z - x - 2]

        return [2, z - x - 2]




