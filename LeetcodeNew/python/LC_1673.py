"""
402. Remove K Digits

1 3 5 7 9

1 3 5 7 9 6 -> then we will remove 7 and 9

1 3 5 6


"""
import functools


class SolutionTony:
    def mostCompetitive(self, nums, k: int):
        k = len(nums) - k
        # if k >= len(nums):
        #     return []
        stack = []
        for num in nums:
            while stack and k and stack[-1] > num:
                stack.pop()
                k -= 1
            stack.append(num)

        while k:
            stack.pop()
            k -= 1
        return stack



class SolutionDFS:
    def mostCompetitive(self, num, k: int):

        n = len(num)
        @functools.lru_cache(None)
        def dfs(num, k):
            if k == n:
                return 0
            if k == 0:
                # remove_leading_zero(num)
                return num

            i = 0
            while i < len(num) - 1 and num[i] <= num[i + 1]:
                i += 1

            return dfs(num[:i] + num[i + 1:], k - 1)
        res = dfs(tuple(num), n-k)
        return res



class SolutionTonyIncorrect:
    def maxNumber(self, nums1, nums2, k: int):
        # 1081.Smallest-Subsequence-of-Distinct-Characters (M+)
        def mostCompetitive(nums, k: int):
            k = len(nums) - k
            if k >= len(nums):
                return 0
            stack = []
            for num in nums:
                while stack and k and stack[-1] < num:
                    stack.pop()
                    k -= 1
                stack.append(num)

            while stack and k:
                stack.pop()
                k -= 1

            nums = list(stack)
            res = 0
            for num in stack:
                res = res * 10 + num
            return res

        m, n = len(nums1), len(nums2)

        @functools.lru_cache(None)
        def dfs(i, j, k):
            # print(i, j, k)
            if k <= 0:
                return 0
            if i >= m and j >= n:
                return 0
            if i >= m:
                # print("tony - ", i, j, nums2[j:], k)
                num = mostCompetitive(nums2[j:], k)
                # print("tony -- ", num)
                return num
            if j >= n:
                # print("tony = ", i, j, nums1[i:] , k)
                num = mostCompetitive(nums1[i:], k)
                # print("tony == ", num)
                return num

            a = dfs(i + 1, j, k)
            b = dfs(i, j + 1, k)
            c = dfs(i + 1, j, k - 1) * 10 + nums1[i]
            d = dfs(i, j + 1, k - 1) * 10 + nums2[j]

            return max(a, b, c, d)

        return map(int, list(str(dfs(0, 0, k))))

