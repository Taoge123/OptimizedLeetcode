import bisect
#
# class Solution:
#     def test(self, nums):
#         nums.sort()
#         nums2 = [[j, i] for i, j in nums]
#         nums2.sort()
#
#         res = 0
#         n = len(nums)
#         for i, j in nums:
#             left = bisect.bisect_left(nums, [i + 1, 0])
#             if left == n:
#                 continue
#             temp = nums2[left:]
#             nn = len(temp)
#             print([j+1, 0])
#             right = bisect.bisect_left(temp, [j + 1, 0])
#             if right == nn:
#                 continue
#             res += 1
#
#         return res
#
# # nums = [[2,2], [3,3]]
# # 1
# nums = [[5,5], [6,3], [3,6]]
# # 0
# # nums = [[1,5], [10, 4], [4,3]]
# # 2
# # nums = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
# # nums = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
# # nums = [[4,10],[2,2],[8,8],[10,2],[5,5],[9,10],[2,6]]
#
# a = Solution()
# print(a.test(nums))
#
import collections


class Solution:
    def test(self, nums):
        table = collections.defaultdict(int)
        days = collections.defaultdict(list)
        pos = 0
        day = 0
        visited = set()
        while True:
            print(pos)
            table[pos] += 1
            visited.add(pos)
            if table[pos] % 2 == 1:
                days[pos].append(day)
                pos = nums[pos]
            else:
                days[pos].append(day)
                pos += 1
            if len(visited) == len(nums):
                return day

            res += 1
            res %= (10**9 + 7)

nums = [0,0,0,0,0,0,0,0,0,0,0]
a = Solution()
print(a.test(nums))
