
class Solution3:
    def numberOfSubarrays(self, nums, k: int) -> int:
        table = {0: 1}
        count = 0
        res = 0

        for i, num in enumerate(nums):
            if num % 2 == 1:
                count += 1

            if count - k in table:
                res += table[count - k]

            table[count] = table.get(count, 0) + 1

        return res


