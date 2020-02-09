# # def test(bids):
# #     temp = sorted(bids, key=lambda x: (x[-2], -x[-1]), reverse=True)
# #     table = collections.defaultdict(list)
# #     for i, item in enumerate(temp):
# #         if item[2] not in table:
# #             table[item[2]].append([item[3], [1, item[1]]])
# #         else:
# #             node = table[item[2]]
# #             id = [node[0][0]].append([item[3]])
# #             del table[item[2]]
# #             table[item[2]].append([id, [node[0][-1][0] + 1, node[0][-1][1] + item[1]]])
# #
# #     for i, j in table.items():
# #         print(i, j)
# #     heapq.heapify(bids)
# #     print(bids)
#
#
#
# import heapq
# import collections
#
# bids = [
#         [3, 7, 5, 3],
#         [3, 7, 5, 2],
#         [3, 7, 5, 1],
#         [1, 5, 5, 0],
#         [2, 7, 8, 1],
#         [4, 10,3, 3],
#         ]
#
# # def test(bids, totalShare):
# #     temp = sorted(bids, key=lambda x: (x[-2], -x[-1]), reverse=True)
# #     res = []
# #     table = collections.defaultdict(list)
# #     for i, item in enumerate(temp):
# #         if item[2] not in table:
# #             table[item[2]]  = [[item[0], item[1]]]
# #         else:
# #             table[item[2]].append([item[0], item[1]])
# #
# #     for k, v in table.items():
# #         heapq.heappush(res, (-k, v))
# #
# #     final = []
# #     for i in range(len(res)):
# #         final.append(heapq.heappop(res)[-1])
# #
# #     for i in final:
# #         print(i)
# #
# #     for i, node in enumerate(final):
# #         lower = len(node)
# #         upper = sum(i[1] for i in node)
# #
# #         if totalShare < lower:
# #             return [node[0] for node in final[i][totalShare:]] + [i[0] for node in final[i+1:] for i in node ]
# #         elif lower <= totalShare <= upper:
# #             return [i[0] for node in final[i+1:] for i in node ]
# #         else:
# #             totalShare -= upper
#
#
# totalShares = 17
# bids.sort(key=lambda x: x[2], reverse=True)
# # 8,5,5,3
# ret = []
# i = 0
#
# while i < len(bids):
#     # start the new price list
#     curr_min_price = bids[i][2]
#     curr_price_list = []
#     while i < len(bids) and bids[i][2] == curr_min_price:
#         curr_price_list.append(bids[i])
#         i += 1
#     ret.append(curr_price_list)
#
# for i in ret:
#     i.sort(key=lambda x: x[3])
#
# remain = totalShares
# final_idx = []
#
# for i in range(len(ret)):
#     curr_lower = len(ret[i])
#     curr_upper = sum([e[1] for e in ret[i]])
#     if remain < curr_lower:  # e.g. 3, 4
#         final_idx += [e[0] for e in ret[i][remain:]] + [e[0] for k in ret[i + 1:] for e in k]
#         break
#     elif curr_lower <= remain <= curr_upper:
#         final_idx = [e[0] for k in ret[i + 1:] for e in k]
#         break
#     elif remain > curr_upper:
#         remain -= curr_upper
# print(final_idx)
#
#
#
# """
# http:request
#
#
#
# """
#
#
#
#


#
# A = [1,2,3,4,5,6,7,8]
#
# for i in range(len(A)):
#     left = A[:i:-1]
#     right = A[:i]
#     print(left, right)


# def countPairs(arr, k):
#     # Write your code here
#     arr = sorted(arr)
#
#     left = 0
#     right = len(arr) - 1
#     res = 0
#
#     while left < right:
#         summ = arr[left] + arr[right]
#         if summ < k:
#             left += 1
#         elif summ > k:
#             right -= 1
#         else:
#             res += 1
#             while left <= right and arr[left + 1] == arr[left]:
#                 res += 1
#                 left += 1
#                 break
#             while left <= right and arr[right - 1] == arr[right]:
#                 res += 1
#                 right -= 1
#                 break
#         left += 1
#         right -= 1
#
#     return res


def countPairs(arr, k):
    n = len(arr)
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                count += 1

    return count


# arr = [5,7,9,13,11,6,6,3,3]
# k = 12
arr = [1,3,46,1,3,9]
k = 47

print(countPairs(arr, k))




