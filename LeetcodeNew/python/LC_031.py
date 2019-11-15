
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        small, n = -1, len(nums)

        for i in range( n -1, 0, -1):
            if nums[ i -1] < nums[i]:
                small = i- 1
                break

        if small == -1:
            nums[:] = nums[::-1]
            return

        for i in range(n - 1, small - 1, -1):
            if nums[i] > nums[small]:
                nums[small], nums[i] = nums[i], nums[small]
                break

        nums[:] = nums[:small + 1] + nums[small + 1:][::-1]








