# import itertools, heapq, contextlib
#
# inputs = ['t1.txt', 't2.txt', 't3.txt']
#
#
# def kayMapping(s):
#     t = s.split()
#     if len(t) < 1:
#         return ""
#     return s.split()[0]
#
# def dedup(file):
#     return [line for line, group in itertools.groupby(file)]
#
# with contextlib.ExitStack() as stack:
#     files = []
#     for file in inputs:
#         files.append(stack.enter_context(open(file)))
#     with open('output.txt', 'w') as f:
#         temp = dedup(heapq.merge(*files, key=kayMapping))
#         f.writelines(temp)
#
#
#
# indexes = [0,1,2,3,4,5,6,7,8,9]
# prices = [51,56,56,58,60,59,54,57,52,48]
# position = [0,0,0,1,2,2,2,1,1,1]
# temp = [0]
# for i in range(1, len(prices)):
#     if prices[i] - prices[i-1] > 0:
#         temp.append(1)
#     elif prices[i] - prices[i-1] < 0:
#         temp.append(-1)
#     else:
#         temp.append(0)
# print(temp)
# res = [0, 0]
# for i in range(2, len(temp)):
#     num = 0
#     if temp[i-1] == 1 and temp[i-2] == 1:
#         num += 1
#     if i > 2:
#         if temp[i - 1] == -1 and temp[i - 2] == -1 and temp[i-3] == 1:
#             num += 1
#     res.append(num)
#
# print(res)
#



# #get the sign, 1,0,-1
# def sign_func(x):
#     if x>0:return 1
#     if x<0:return -1
#     return 0
#
# sign_list = [[0,0] for i in range(len(prices))]
# for i in range(1,len(prices)):
#     sign_list[i] = [sign_func(prices[i]/prices[i-1]-1),i]
#
# filtered_list = list(filter(lambda x: x[0] != 0, sign_list))
# sign,index = list(zip(*filtered_list))
# sign = list(sign)
# index = list(index)
# b = len(buyIndicator)
# s = len(sellIndicator)
# change = [0 for i in range(len(prices))]
# for i in range(min(b,s)-1,len(sign)):
#     if i>b-2 and sign[i-b+1:i+1] == buyIndicator:
#         change[index[i]] = 1
#     if i>s-2 and sign[i-s+1:i+1] == sellIndicator:
#         change[index[i]] = -1
# np.cumsum(change)
#
#

"""

"""

"""
5 4 4 2 2 8 
3 2 2 0 0 6
1 0 0 0 0 4
0 0 0 0 0 3
0 0 0 0 0 0
"""
def remove(nums,val):
    res = []
    for num in nums:
        if num!= val:
            res.append(num)
    return res
def cutTheBamboo(nums):
    res = []
    while(len(nums) >0):
       #res += len(nums)
        res.append(len(nums))
        minVal = min(nums)
        nums = remove(nums,minVal)
        nums = [x - minVal for x in nums ]
    return res
nums= [1,1,3,4]
cutTheBamboo(nums)


def cutBamboo(nums):
    res = []
    while len(nums) > 0:
        mini = min(nums)
        temp = [num - mini for num in nums]
        temp = [num for num in temp if num > 0]
        nums = temp
        res.append(len(temp))

    return res

nums = [5, 4, 4, 2, 2, 8 ]
print(cutBamboo(nums))






#
# def cutBamboo(nums):
#     res = []
#     while(len(nums) >0):
#        #res += len(nums)
#         res.append(len(nums))
#         minVal = min(nums)
#         nums = remove1(nums,minVal)
#         nums = [x - minVal for x in nums ]
#     return res
#
# def remove1(nums,val):
#     res = []
#     for num in nums:
#         if num!= val:
#             res.append(num)
#     return res
#
#
# nums= [1,1,3,4]
# cutTheBamboo(nums)


import collections
import heapq

def findBestPath(n, m, max_t, beauty, u, v, t):
    # Write your code here
    graph = collections.defaultdict(list)
    for i, j in zip(u, v):
        graph[i].append(j)
        graph[j].append(i)


    for u, v in tickets:
        heapq.heappush(graph[u], v)
        start = 'JFK'
        res = []
        self.dfs(graph, start, res)
        return res[::-1]

    def dfs(self, graph, start, res):
        while graph[start]:
            node = heapq.heappop(graph[start])
            self.dfs(graph, node, res)
        res.append(start)



