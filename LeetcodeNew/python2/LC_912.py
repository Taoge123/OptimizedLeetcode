

class Solution:
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def quicksort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.quicksort(nums, left, pivot - 1)
            self.quicksort(nums, pivot + 1, right)








