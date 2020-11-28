
class Solution:
    def minTaps(self, n: int, nums) -> int:
        intervals = []

        for i, num in enumerate(nums):
            start, end = i - nums[i], i + nums[i]
            intervals.append((start, end))
        intervals = list(set(intervals))
        intervals = [list(i) for i in intervals]
        intervals = sorted(intervals)
        count = 0
        res = []
        res.append(intervals[0])
        for i, interval in enumerate(intervals[1:]):
            if interval[0] <= 0 and interval[1] >= len(nums) - 1:
                return 1

            if res[-1][1] < interval[0]:
                res.append(interval)
            elif res[-1][0] == interval[0]:
                res[-1][1] = interval[1]
            elif interval[0] <= res[-1][1] < interval[1]:
                res[-1][1] = interval[1]
                count += 1
            else:
                pass


        finalRes = len(res) + count
        if finalRes == len(nums):
            return -1
        else:
            return finalRes




n = 9
nums = [0,5,0,3,3,3,1,4,0,4]


a = Solution()
print(a.minTaps(n, nums))






