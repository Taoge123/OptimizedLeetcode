#
# def checkValidity(a, b, c):
#     if (a + b <= c) or (a + c <= b) or (b + c <= a) :
#         return 'No'
#     else:
#         return 'Yes'
#
# def solution(a, b, c):
#     array = []
#     for i in zip(a, b, c):
#         array.append([i[0], i[1], i[2]])
#     res = []
#     for i in array:
#         res.append(checkValidity(i[0], i[1], i[2]))
#
#     return res
#
# a = [7,10,7]
# b = [2,3,4]
# c = [2,7,4]
# print(solution(a,b,c))
#
#

"""
[1,2,2,3]
[1,3,5,8]
[8,7,5,3]
"""
#
# def solution2(nums):
#     n = len(nums) - 1
#     left = [nums[0]] + [0] * (n)
#     right = [0] * (n) + [nums[-1]]
#
#     for i in range(1, n+1):
#         left[i] += left[i-1] + nums[i]
#
#     for i in range(n-1, -1, -1):
#         right[i] = right[i+1] + nums[i]
#
#     count = 0
#     res = 0
#     for i, j in zip(left, right):
#         if i == j:
#             res = count
#         count += 1
#
#     return res
#
#
# nums = [1,2,2,3]
# print(solution2(nums))
#
#
#
import collections
import heapq
nums = [3,3,3,3,3,1,3]
# nums = [1,2,3,4,5,6,7,8,9,10]
# {3: 0,1,2,3,4,6
#  1: 5
#  }
table = collections.defaultdict(list)
temp = []
res = []
for i, num in enumerate(nums):
    heapq.heappush(table[num], i)
    if len(table[num]) == num:
        res.append(table[num])
        table[num] = []

for k, v in table.items():
    if v:
        res.append(v)

res = sorted(res, key=lambda x : x[0])


# res = []
# for num in temp:
#     key = num
#     val = table[num]
#
#     while len(val) > key:
#         res.append(val[:key])
#         val = val[key:]
#
#     res.append(val)


for i in res:
    print(" ".join(map(str, i)), end='\n')




