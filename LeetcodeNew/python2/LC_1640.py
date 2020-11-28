
class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        table = {nums[0]: nums for nums in pieces}
        res = []

        for num in arr:
            res += table.get(num, [])
        return res == arr

