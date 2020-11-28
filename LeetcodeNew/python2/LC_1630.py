
class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        res = []
        for i in range(len(l)):
            if len(nums[l[i]: r[i] + 1]) <= 1:
                res.append(True)
            else:
                if check(nums[l[i]: r[i] + 1]):
                    res.append(True)
                else:
                    res.append(False)
        return res




