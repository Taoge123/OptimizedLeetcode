import collections

class Solution:
    def minSumOfLengths(self, arr, target: int) -> int:
        table = {0: -1}
        prefix = 0
        dp = [float('inf') for i in range(len(arr) + 1)]

        res = float('inf')

        for i, num in enumerate(arr):
            prefix += num
            dp[i + 1] = min(dp[i + 1], dp[i])
            if prefix - target in table:
                res = min(res, i - table[prefix - target] + dp[table[prefix - target] + 1])
                dp[i + 1] = min(dp[i + 1], i - table[prefix - target])

            table[prefix] = i

        if res != float('inf'):
            return res
        else:
            return -1


class Solution2:
    def minSumOfLengths(self, arr, target: int) -> int:
        table = collections.defaultdict(lambda : float('inf'))
        left = 0
        presum = 0
        res = float('inf')
        for right in range(len(arr)):
            presum += arr[right]
            while presum > target:
                presum -= arr[left]
                left += 1

            if presum == target:
                table[right] = right - left + 1
                res = min(res, table[left -1] + right - left + 1)

            table[right] = min(table[right], table[right -1])

        return -1 if res == float('inf') else res


