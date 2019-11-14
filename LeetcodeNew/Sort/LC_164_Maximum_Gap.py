
class Solution:
    def maximumGap(self, nums):

        if len(nums) < 2 or min(nums) == max(nums):
            return 0

        mini, maxi = min(nums), max(nums)

        gap = (maxi - mini) // (len(nums ) - 1) or 1

        bucket = [[None, None] for i in range((maxi - mini)//gap +1)]

        for num in nums:
            b = (num-mini) // gap

            bucket[b][0] = num if bucket[b][0] is None else min(bucket[b][0], num)
            bucket[b][1] = num if bucket[b][1] is None else max(bucket[b][1], num)

        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i-1][1] for i in range(1, len(bucket)))


nums = [3,6,9,1]
a = Solution()
print(a.maximumGap(nums))




















