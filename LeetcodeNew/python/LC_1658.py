
"""

   a          b
prefix[a] + suffix[b] = x

suffix[i] -> i

"""

"""

"""

class SolutionPrefix:
    def minOperations(self, nums, x: int) -> int:
        n = len(nums)
        if sum(nums) < x:
            return -1

        summ = 0
        prefix = {}
        for i in range(n):
            summ += nums[i]
            if summ > x:
                break
            prefix[summ] = i + 1

        summ = 0
        suffix = {}
        for i in range( n -1, -1, -1):
            summ += nums[i]
            if summ > x:
                break
            suffix[summ] = n - i

        res = min(prefix.get(x, float('inf')), suffix.get(x, float('inf')))

        for summ in prefix:
            if x - summ in suffix:
                res = min(res, prefix[summ] + suffix[x - summ])

        if res != float('inf'):
            return res
        else:
            return -1



class SolutionSlidingWindow:
    def minOperations(self, nums, x: int) -> int:
        n = len(nums)
        res = -1
        target = sum(nums) - x
        left, right = 0, 0
        summ = 0
        while left < n and right < n:
            if right < n:
                summ += nums[right]
                right += 1
            while summ > target and left < n:
                summ -= nums[left]
                left += 1

            if summ == target:
                res = max(res, right - left)

        return n - res if res >= 0 else -1











