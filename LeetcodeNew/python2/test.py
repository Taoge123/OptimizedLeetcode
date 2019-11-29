# def test(bids):
#     temp = sorted(bids, key=lambda x: (x[-2], -x[-1]), reverse=True)
#     table = collections.defaultdict(list)
#     for i, item in enumerate(temp):
#         if item[2] not in table:
#             table[item[2]].append([item[3], [1, item[1]]])
#         else:
#             node = table[item[2]]
#             id = [node[0][0]].append([item[3]])
#             del table[item[2]]
#             table[item[2]].append([id, [node[0][-1][0] + 1, node[0][-1][1] + item[1]]])
#
#     for i, j in table.items():
#         print(i, j)
#     heapq.heapify(bids)
#     print(bids)



import heapq
import collections

bids = [
        [3, 7, 5, 3],
        [3, 7, 5, 2],
        [3, 7, 5, 1],
        [1, 5, 5, 0],
        [2, 7, 8, 1],
        [4, 10,3, 3],
        ]

# def test(bids, totalShare):
#     temp = sorted(bids, key=lambda x: (x[-2], -x[-1]), reverse=True)
#     res = []
#     table = collections.defaultdict(list)
#     for i, item in enumerate(temp):
#         if item[2] not in table:
#             table[item[2]]  = [[item[0], item[1]]]
#         else:
#             table[item[2]].append([item[0], item[1]])
#
#     for k, v in table.items():
#         heapq.heappush(res, (-k, v))
#
#     final = []
#     for i in range(len(res)):
#         final.append(heapq.heappop(res)[-1])
#
#     for i in final:
#         print(i)
#
#     for i, node in enumerate(final):
#         lower = len(node)
#         upper = sum(i[1] for i in node)
#
#         if totalShare < lower:
#             return [node[0] for node in final[i][totalShare:]] + [i[0] for node in final[i+1:] for i in node ]
#         elif lower <= totalShare <= upper:
#             return [i[0] for node in final[i+1:] for i in node ]
#         else:
#             totalShare -= upper


totalShares = 17
bids.sort(key=lambda x: x[2], reverse=True)
# 8,5,5,3
ret = []
i = 0

while i < len(bids):
    # start the new price list
    curr_min_price = bids[i][2]
    curr_price_list = []
    while i < len(bids) and bids[i][2] == curr_min_price:
        curr_price_list.append(bids[i])
        i += 1
    ret.append(curr_price_list)

for i in ret:
    i.sort(key=lambda x: x[3])

remain = totalShares
final_idx = []

for i in range(len(ret)):
    curr_lower = len(ret[i])
    curr_upper = sum([e[1] for e in ret[i]])
    if remain < curr_lower:  # e.g. 3, 4
        final_idx += [e[0] for e in ret[i][remain:]] + [e[0] for k in ret[i + 1:] for e in k]
        break
    elif curr_lower <= remain <= curr_upper:
        final_idx = [e[0] for k in ret[i + 1:] for e in k]
        break
    elif remain > curr_upper:
        remain -= curr_upper
print(final_idx)



"""
http:request



"""




