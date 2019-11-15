class Solution:
    def rotate(self, nums, k):

        k = k % len(nums)
        n = len(nums)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


"""[1,2,3,4,5,6,7] 

[4 3 2 1  7 6 5]
56 7 1 2 3 4 
and k = 3
[5,6,7,1,2,3,4]"""

