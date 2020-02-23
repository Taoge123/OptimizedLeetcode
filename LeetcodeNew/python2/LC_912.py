

class Solution:
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums, left, high):
        pivot = nums[high]
        i = left
        for j in range(left, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

    def quicksort(self, nums, left, high):
        if left < high:
            pivot = self.partition(nums, left, high)
            self.quicksort(nums, left, pivot - 1)
            self.quicksort(nums, pivot + 1, high)








