

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, nums, target):
        nums += [2*31-1]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if target-1 < nums[mid]:
                r = mid
            else:
                l = mid+1
        return l