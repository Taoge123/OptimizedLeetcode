
class Solution:
    def maxLength(self, ribbons, k):

        left, right = 1, max(ribbons) + 1
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if self.count(ribbons, mid) >= k:
                left = mid
            else:
                right = mid

        if self.count(ribbons, right) >= k:
            return right
        if self.count(ribbons, left) >= k:
            return left
        return 0


    def count(self, nums, size):
        count = 0
        for num in nums:
            count += num // size
        return count


