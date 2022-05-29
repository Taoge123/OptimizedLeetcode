
class Solution:
    def maximumScore(self, nums, k: int) -> int:
        n = len(nums)
        l, r = k, k

        minn = nums[k]
        res = 0

        while l >= 0 or r < n:
            while r < n and nums[r] >= minn:
                r += 1
            while l >= 0 and nums[l] >= minn:
                l -= 1
            res = max(res, (r - l - 1) * minn)

            # update minn value
            if l < 0 and r == n:  # 遍历完数组，退出循环
                break
            if l >= 0 and r <= n - 1:  # 贪心，更新nums[k]为左右边界中的较大者
                minn = max(nums[l], nums[r])
            elif l < 0:
                minn = nums[r]
            else:  # r >= n
                minn = nums[l]
        return res
