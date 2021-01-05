
import bisect


class Solution:
   def waysToSplit(self, nums) -> int:
       """
       O(nlogn)/O(n)
       """
       presum = [0]
       for i in range(len(nums)):
           presum.append(presum[-1] + nums[i])
       res = 0

       for i in range(1, len(nums) - 1):
           first = presum[i]
           if 3 * first > presum[-1]: break

           low = bisect.bisect_left(presum, 2 * first, i + 1, len(nums))
           high = bisect.bisect_left(presum, (presum[-1] - first) // 2 + first + 1, low, len(nums))
           res += high - low
           res %= (10 ** 9 + 7)

       return res % (10 ** 9 + 7)



