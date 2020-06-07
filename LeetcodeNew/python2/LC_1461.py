
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        nums = {s[i: i +k] for i in range(len(s ) - k +1)}
        return len(nums) == 2 ** k


