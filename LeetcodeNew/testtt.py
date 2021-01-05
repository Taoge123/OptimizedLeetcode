"""
1 2 4 8 16 32 64

[1,1,1,3,3,3,7]


"""

# import collections
#
# class Solution:
#     def countPairs(self, nums) -> int:
#         power = []
#         for i in range(1, 32):
#             power.append(2 ** i)
#
#         count = collections.Counter(nums)
#
#         res = 0
#         for num in set(nums):
#             for p in power:
#                 if p - num in count:
#                     print(num, p, p - num, count.keys())
#                     if num != (p - num):
#                         res += count[p - num]
#         return res
#


class Solution:
    def minOperations(self, s, t) -> int:
        m, n = len(s), len(t)

        def dfs(i, j):
            if i == m:
                return 0

            if j == n:
                return m - i

            if s[i] == t[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i, j + 1), dfs(i + 1, j)) + 1
                # return dfs(i+1, j+1) + dfs(i+1, j) + 1

        return dfs(0, 0)



s = [5,1,3]
t = [9,4,2,3,4]

a = Solution()
print(a.minOperations(s, t))



