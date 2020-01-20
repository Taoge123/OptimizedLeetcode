# import bisect
#
# #max sum of pairs,
# #for the pairs, digit sum should be equal
# def solution(A):
#     d = {}
#     for i in range(len(A)):
#         digit_sum = sum([int(k) for k in str(A[i])])
#         if digit_sum not in d:
#             d[digit_sum] = [A[i]]
#         else:
#             bisect.insort(d[digit_sum], A[i])
#     ret = -float('inf')
#     for i in d.values():
#         if len(i)<2:
#             continue
#         else:
#             ret = max(ret,i[-2]+i[-1])
#     print(d)
#     if ret == -float('inf'):
#         return -1
#     return ret
#
#
#
# A = [51, 71,17,42, 33]
# print(solution(A))
#


import collections

def solution(A, B, N):
    graph = collections.defaultdict(set)
    for city1, city2 in zip(A, B):
        graph[city1].add(city2)
        graph[city2].add(city1)

    max_rank = 0
    for city1, city2 in zip(A, B):
        tmp_rank = len(graph[city1]) + len(graph[city2])
        if city2 in graph[city1]:
            tmp_rank -= 1
        max_rank = max(max_rank, tmp_rank)

    return max_rank

print(solution([1,2,3,3], [2,3,1,4], 4))
print(solution([1,2,4,5], [2,3,5,6], 6))


