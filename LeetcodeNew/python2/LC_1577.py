
import collections

class SolutionTony:
    def numTriplets(self, nums1, nums2) -> int:
        res1 = self.helper(nums1, nums2)
        res2 = self.helper(nums2, nums1)
        return res1 + res2

    def helper(self, nums1, nums2):
        set1 = [num ** 2 for num in nums1]
        set2 = []
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                set2.append(nums2[i] * nums2[j])

        count = collections.Counter(set2)
        res = 0
        for num in set1:
            res += count[num]
        return res






