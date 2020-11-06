
class SparseVector:
    def __init__(self, nums):
        self.nums = {}
        for i, num in enumerate(nums):
            if num:
                self.nums[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, num in vec.nums.items():
            if i in self.nums:
                res += num * self.nums[i]
        return res



# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)