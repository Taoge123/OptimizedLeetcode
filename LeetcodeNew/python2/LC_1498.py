class SolutionBS:
    def numSubseq(self, nums, target: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        nums.sort()

        res = 0
        for i in range(n):
            j = -1
            left, right = i, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target - nums[i]:
                    j = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if j == -1:
                return res % mod
            res += pow(2, j - i, mod)

        return res % mod




class Solution:
    def numSubseq(self, nums, target: int) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        mod = 10 ** 9 + 7
        j = n - 1
        for i in range(n):
            while j>=i and nums[i] + nums[j] > target:
                j -= 1
            if j < i:
                break
            res += pow(2, j - i, mod)
            res %= mod

        return int(res)


