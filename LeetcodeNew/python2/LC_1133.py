import collections

class Solution:
    def largestUniqueNumber(self, A) -> int:
        count = collections.Counter(A)
        nums = []
        for k, times in count.items():
            if times == 1:
                nums.append(k)

        return max(nums) if nums else -1





