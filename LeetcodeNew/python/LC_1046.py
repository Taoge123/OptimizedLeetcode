import bisect


class Solution:
    def lastStoneWeight(self, stones) -> int:
        nums = sorted(stones)
        for i in range(len(nums ) -1):
            x = nums.pop()
            y = nums.pop()
            # nums.append(abs(x - y))
            # nums.sort()
            bisect.insort_left(nums, abs(x - y))

        return nums[0]



