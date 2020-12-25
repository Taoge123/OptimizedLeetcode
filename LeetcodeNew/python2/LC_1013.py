"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/discuss/261384/Python-O(n)

"""


class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:

        summ = sum(arr)
        if summ % 3 != 0:
            return False

        target = summ // 3

        parts = 0
        cur = 0
        pastsum = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            if parts == 3:
                pastsum += arr[i]
                continue

            cur += arr[i]

            if cur == target:
                parts += 1
                cur = 0

        return parts == 3 and pastsum == 0




class Solution2:
    def canThreePartsEqualSum(self, arr):
        summ = sum(arr)
        if summ / 3 != summ // 3:
            return False

        target = summ // 3

        if target == 0 and len(arr) // 2 >= 3:
            return True

        presum = 0
        count = 0
        for i, num in enumerate(arr):
            presum += num
            if presum == target:
                count += 1
                presum = 0

        if count == 3:
            return True

        return False




